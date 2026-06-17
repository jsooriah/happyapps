---
type: post
title: RAG In Content Moderation
description: Retrieval-augmented generation (RAG) has become a common architecture for AI systems that need to ground their outputs in an existing body of knowledge. Rather than relying solely on a model parametric memory, RAG retrieves relevant documents from a database at inference time and injects them into the model context. The model reasons from those retrieved examples rather than from rules encoded during training. This pattern has found applications in question-answering, legal research, customer support, and increasingly in content moderation. The appeal in a moderation context is straightforward - moderation decisions are inherently precedent-driven. Given a new piece of content, the question is whether it resembles cases previously flagged as violations — and if so, which ones. A retrieval-augmented system formalises this by embedding the incoming content, finding the most similar past cases in a policy library, and using those analogues to guide the decision. This approach is sometimes described as embedding-driven development - building decision logic from the structure of a vector space rather than from hand-authored rules. The practical advantage over traditional rule-based approaches — keyword filters, regex patterns, manually maintained taxonomies — is that embedding-based retrieval generalises from examples. It can adapt to novel phrasings and new harm types without requiring explicit rule updates, and it produces interpretable outputs in the form of retrieved precedents. The critical dependency in this setup is the embedding model itself. The quality of retrieval — how consistently it surfaces policy-relevant analogues — depends entirely on how the embedding model structures its vector space. A model that clusters content by surface vocabulary rather than by policy intent will retrieve plausible-looking but policy-irrelevant matches, undermining everything downstream.
publication: 2026-06-17 10:46:53
tags: rag content mdoeration
authors:
  - joel-sooriah
featured: false
redirects:
    - from: rag-in-content-moderation
---

## Context

Retrieval-augmented approaches to AI content moderation depend on embedding models that can surface policy-analogous cases from a violation database. We evaluate a three-stage pipeline — retrieval, rule induction, and downstream classification — comparing moderation-aware embeddings (HateBERT, trained on banned Reddit communities) against general-purpose embeddings (BGE-M3). Using the Aegis AI Content Safety Dataset across six violation categories, we find that BGE-M3 consistently outperforms HateBERT on retrieval (Precision@10), by an average of 8.7 pp on explicit violations and 6.4 pp on implicit violations. We term this the **policy-semantics gap**: the divergence between domain-specific classification objectives and the representational quality needed for policy-grounded retrieval. However, when the retrieved analogues are used to induce moderation rules via Claude Sonnet, and those rules are injected into Claude Haiku for classification, HateBERT's rules produce higher macro F1 (72.9% vs 68.2%). This inversion — better retrieval leading to worse downstream classification — reveals that retrieval quality and rule usability are distinct dimensions that can conflict. Our results caution against optimising retrieval in isolation and highlight the need for end-to-end evaluation of retrieval-augmented moderation pipelines.

## Glossary of Terms

**Embedding model** — a neural network that maps a text input to a fixed-dimensional real-valued vector. Proximity in the vector space is intended to reflect semantic similarity between inputs.

**Vector / embedding** — the numerical representation output by an embedding model. BGE-M3 produces 1024-dimensional vectors; HateBERT produces 768-dimensional vectors.

**L2 normalisation** — scaling each vector to unit length so that cosine similarity equals the inner product (dot product). Applied to all embeddings in this work.

**Cosine similarity** — a measure of the angle between two vectors, ranging from −1 (opposite) to 1 (identical direction). After L2 normalisation, equivalent to the dot product.

**FAISS (IndexFlatIP)** — a Meta library for fast nearest-neighbour search. `IndexFlatIP` performs exact inner product search over all database vectors. Used to retrieve the top-k most similar database items for each query.

**Masked language modelling (MLM)** — a pre-training objective where random tokens are masked and the model learns to predict them from context. Optimises for understanding the token distribution of the training corpus, not for structuring the embedding space by semantic category. HateBERT uses this objective.

**Contrastive learning** — a training objective that explicitly pulls similar items closer together and pushes dissimilar items further apart in embedding space. Directly optimises for retrieval quality. BGE-M3 uses this objective.

**CLS token** — a special token prepended to every BERT input. Its final hidden state is used as a fixed-size summary representation of the whole sequence. Used to extract sentence embeddings from HateBERT.

**Precision@k (P@k)** — of the top-k retrieved items for a query, the fraction whose policy label matches the query label. Averaged across all queries within a category. Random retrieval over 6 balanced categories yields ~16.7%.

**Policy-semantics gap** — the divergence between semantic similarity (proximity in embedding space) and policy similarity (sharing the same violation category). The central construct of this paper.

**Rule induction** — prompting a large language model with a set of labelled examples and asking it to articulate the policy rule that explains why those examples are violations. Used in Phase 6 to convert retrieved analogues into moderation rules.

**Macro F1** — the unweighted average of per-category F1 scores. Treats all categories equally regardless of class frequency. The primary downstream classification metric in Phase 7.

**Retrieval-augmented moderation** — a moderation pipeline in which a new content item is matched against a database of prior cases using embedding-based retrieval, and the retrieved analogues are used to ground a moderation decision (via direct scoring, few-shot prompting, or rule induction).

---

## 1. Introduction

AI content moderation at scale increasingly relies on retrieval-augmented pipelines: a piece of user-generated content is embedded, its nearest neighbours are retrieved from a policy case library, and those analogues are used to ground a moderation decision — whether by direct similarity scoring, few-shot prompting of a language model, or structured rule induction Lu et al. [2026].

The quality of this retrieval step is determined by the embedding model: specifically, whether its notion of "similarity" aligns with "policy similarity" — i.e., whether semantically proximate items in embedding space share the same violation category. We call the divergence between these two notions the **policy-semantics gap**.

A natural prior is that embedding models fine-tuned on harmful content would better represent the policy-relevant structure of that content space. HateBERT [Caselli et al., 2021], trained on text from banned Reddit communities, is the canonical example of such a model. Yet its training objective — masked language modelling on hate-adjacent corpora — optimises for representation of the harmful content distribution, not for the intra-category discriminative structure needed for retrieval.

We present a controlled end-to-end evaluation of HateBERT and BGE-M3 [Chen et al., 2024] across a three-stage retrieval-augmented moderation pipeline over the Aegis AI Content Safety Dataset [Ghosh et al., 2024]. Our contributions are:

1. A reproducible evaluation framework spanning retrieval quality (P@10), rule induction quality, and downstream classification (macro F1) for content moderation.
2. Evidence that general-purpose embeddings outperform moderation-specific ones on policy-grounded retrieval across all tested violation categories.
3. A demonstration that retrieval quality and downstream classification performance are non-monotonically related: HateBERT's lower-quality retrievals induce rules that produce higher classification accuracy.
4. A characterisation of the policy-semantics gap as a multi-layer phenomenon spanning retrieval, rule precision, and rule usability.

---

## 2. Related Work

### 2.1 Retrieval-Augmented Content Moderation

Case-based reasoning approaches to content moderation treat policy enforcement as analogical reasoning: find the most similar prior cases, apply their outcomes. This mirrors the legal tradition of precedent and has been formalised in several recent systems. Lu et al. [2026] (CHAIRO) propose an end-to-end framework that jointly optimises retrieval, rule induction, and classification, demonstrating that analogical example-driven methods outperform static RAG pipelines on moderation accuracy and rule interpretability. Chen et al. [2024b] (Class-RAG) extend a base LLM with a dynamically updatable retrieval library, showing that RAG-based classifiers outperform fine-tuned models and are more robust to adversarial inputs, with performance scaling with library size. At production scale, Yew et al. [2026] deploy a hybrid framework for livestream moderation combining supervised classification with reference-based similarity matching, achieving 76% recall at 80% precision on novel violations that evade traditional classifiers.

Our work differs from these in focus: rather than proposing a new pipeline architecture, we isolate and evaluate how the choice of embedding model affects retrieval quality and propagates through the pipeline to downstream classification performance.

### 2.2 Embedding Models for Harmful Content

HateBERT [Caselli et al., 2021] demonstrated that domain-adaptive pre-training on harmful content corpora improves performance on hate speech detection benchmarks. However, these evaluations focus on classification, not retrieval. Shi et al. [2025] address the retrieval setting directly, training a suite of embedding models using Supervised Contrastive Learning (SCL) specifically for content moderation on a short-video platform, improving retrieval ROC-AUC from 0.85 to 0.99 and reducing operational costs by over 80%. Their results demonstrate that domain-specific *contrastive* training — as opposed to domain-specific MLM pre-training — substantially improves retrieval quality for moderation, a key distinction from HateBERT's training objective and a motivation for our future work direction.

### 2.3 General-Purpose Dense Embeddings

BGE-M3 [Chen et al., 2024] is a multi-lingual, multi-granularity embedding model trained on diverse corpora, achieving state-of-the-art performance on BEIR [Thakur et al., 2021] retrieval benchmarks. Its strong general retrieval performance makes it a natural baseline for any retrieval task.

### 2.4 The Aegis Dataset

Aegis [Ghosh et al., 2024] is a human-annotated AI content safety dataset released by NVIDIA, covering six violation categories (hate, sexual, profanity, harassment, confessions/self-harm, harmless) with fine-grained severity annotations. It is designed to evaluate content safety classifiers for large language models.

---

## 3. Methodology

### 3.1 Dataset Preparation

We use the Aegis AI Content Safety Dataset (v1.0), filtering to six categories: `hate`, `sexual`, `profanity`, `harassment`, `confessions`, and `harmless`. We cap each category at 400 items to mitigate class imbalance, then apply a stratified 70/30 split to produce a **database** (items to be retrieved from) and a **query set**.

Final counts: 1,896 database items, 814 query items.

We conceptually partition categories into:

- **Explicit violations**: hate, sexual, profanity — typically identifiable through surface-level signals (slurs, explicit terms)
- **Implicit violations**: harassment, confessions — often encoded in subtext, context-dependent language, or coded phrasing
- **Neutral**: harmless

### 3.2 Embedding Models

**BGE-M3** (`BAAI/bge-m3`): Loaded via `sentence-transformers`. Embeddings are L2-normalised; cosine similarity is computed as inner product. Max sequence length: 512 tokens.

**HateBERT** (`GroNLP/hateBERT`): Loaded via `transformers`. We extract the CLS token from the final hidden layer and L2-normalise. Max sequence length: 512 tokens. The MLM prediction head is discarded.

### 3.3 Index and Retrieval

For each model, we embed the full database and build a FAISS `IndexFlatIP` (exact inner product search). At query time, we embed each query and retrieve the top K+1 nearest neighbours, excluding any result whose ID matches the query ID (to prevent self-retrieval in the event of overlap).

### 3.4 Retrieval Metric

We report **Precision@k** (P@k) for k ∈ {1, 3, 5, 10}:

$$P@k = \frac{1}{k} \sum_{i=1}^{k} \mathbf{1}[\text{label}(r_i) = \text{label}(q)]$$

where $r_1, \ldots, r_k$ are the top-k retrieved items for query $q$. We average P@k across all queries within each category.

The primary metric is **P@10**, as retrieval-augmented moderation pipelines typically consume 5–10 analogues per query.

### 3.5 Rule Induction

For a sample of five queries per category (harassment, hate, profanity), we prompt Claude Sonnet 4.6 with the query text and its top-10 retrieved analogues (labelled with their policy category), and ask it to synthesise a moderation rule explaining the violation pattern. This yields five per-query rules per model. We then aggregate each model's five rules into a single master rule per category via a second Claude Sonnet call, producing six master rules in total (three categories × two models).

The system prompt instructs the model to produce rules that: (1) are specific enough to classify unseen content, (2) capture intent and harm pattern rather than surface vocabulary, and (3) distinguish the target category from adjacent ones.

### 3.6 Downstream Classification

We evaluate three conditions using Claude Haiku 4.5 as the classifier:

- **Zero-shot**: Haiku receives brief descriptions of each category (no retrieved examples, no induced rules).
- **BGE-M3 rules**: Haiku receives the master rules induced from BGE-M3 retrievals.
- **HateBERT rules**: Haiku receives the master rules induced from HateBERT retrievals.

In all conditions, Haiku is prompted to classify each item into exactly one of the three evaluated categories and respond with the category name only.

We evaluate on 367 held-out queries (harassment: 145, hate: 145, profanity: 77) excluding the 15 used for rule induction. The primary metric is **macro F1**, computed per category and averaged equally across categories to account for class imbalance.

---

## 4. Results

Table 1 shows P@10 per category for both models and the absolute difference (Δ = HateBERT − BGE-M3).

**Table 1: Precision@10 by category (%)**


| Category         | Type     | n   | BGE-M3   | HateBERT | Δ        |
| ---------------- | -------- | --- | -------- | -------- | -------- |
| hate             | explicit | 150 | 59.3     | 56.7     | -2.6     |
| sexual           | explicit | 132 | 63.9     | 61.1     | -2.8     |
| profanity        | explicit | 82  | 48.2     | 27.3     | -20.9    |
| harassment       | implicit | 150 | 47.9     | 39.3     | -8.6     |
| confessions      | implicit | 150 | 58.1     | 53.9     | -4.2     |
| harmless         | neutral  | 150 | 34.5     | 33.3     | -1.2     |
| **Explicit avg** |          |     | **57.1** | **48.4** | **-8.7** |
| **Implicit avg** |          |     | **53.0** | **46.6** | **-6.4** |


BGE-M3 outperforms HateBERT on every category. The largest gap is `profanity` (−20.9 pp), followed by `harassment` (−8.6 pp). Notably, HateBERT underperforms even on `hate` — the category most closely aligned with its training corpus.

The absolute P@10 scores range from 34.5% (harmless, BGE-M3) to 63.9% (sexual, BGE-M3), indicating meaningful signal above random (which would yield ~16.7% for six balanced classes) but substantial room for improvement — particularly for `harmless` content, where both models retrieve large proportions of violation items.

**Explicit vs. implicit.** Contrary to our hypothesis, the gap between BGE-M3 and HateBERT is larger on explicit violations (−8.7 pp) than implicit ones (−6.4 pp). This suggests that HateBERT's training on explicit harmful content actively hurts its representational quality for explicit policy categories, not just implicit ones.

### 4.2 Rule Induction

Qualitative analysis of the induced master rules reveals consistent differences in character. BGE-M3 rules emphasise intent and harm pattern: for harassment, the BGE-M3 rule specifies *"solicits, generates, or facilitates targeted harm directed at a specific individual... regardless of framing as hypothetical, humorous, or educational... distinguished from profanity by its focus on interpersonal attack."* HateBERT rules tend to anchor more heavily on observable surface features and behavioural acts: the HateBERT harassment rule foregrounds *"demeaning, mocking, or cruel treatment... soliciting insults, taunting language, or bullying tactics."*

For profanity, the divergence is most pronounced. BGE-M3's rule centres on the absence of a targeted victim as the key distinguishing criterion. HateBERT's rule centres on the presence of explicit vulgar vocabulary.

### 4.3 Downstream Classification

**Table 2: Downstream classification macro F1 by condition (%)**


| Category     | Zero-shot                 | BGE-M3 rules              | HateBERT rules            |
| ------------ | ------------------------- | ------------------------- | ------------------------- |
| harassment   | P=74.4 R=44.1 F1=55.4     | P=81.3 R=60.0 F1=69.0     | P=78.0 R=75.9 **F1=76.9** |
| hate         | P=87.3 R=61.4 F1=72.1     | P=83.6 R=70.3 **F1=76.4** | P=91.0 R=62.8 F1=74.3     |
| profanity    | P=77.3 R=66.2 **F1=71.3** | P=56.5 R=62.3 F1=59.3     | P=67.5 R=67.5 F1=67.5     |
| **Macro F1** | **66.3**                  | **68.2**                  | **72.9**                  |


Both rule conditions improve over zero-shot (macro F1 +1.9 pp for BGE-M3, +6.6 pp for HateBERT). Contrary to the retrieval results, **HateBERT rules produce higher macro F1 (72.9%) than BGE-M3 rules (68.2%)**.

The most striking divergence is profanity: BGE-M3 rules reduce F1 by 12.0 pp below zero-shot, while HateBERT rules reduce it by only 3.8 pp. For harassment, HateBERT rules outperform BGE-M3 rules by 7.9 pp. BGE-M3 rules lead only on hate (+2.1 pp over HateBERT).

---

## 5. Discussion

### 5.1 Why Does the General-Purpose Model Win?

We propose three explanations:

**Objective mismatch.** HateBERT's pre-training objective (masked language modelling on harmful content) optimises for representing the distribution of tokens in harmful text, not for structuring the embedding space by policy category. The model learns "what harmful text looks like" but not "how harassment differs from profanity in policy-relevant ways." BGE-M3, trained with contrastive objectives on diverse retrieval tasks, learns inter-item similarity structure more directly relevant to k-NN retrieval.

**Training data bias.** HateBERT's corpus — banned Reddit communities — is a narrow, platform-specific slice of harmful content. Its representations may generalise poorly to the Aegis distribution, which is drawn from more diverse sources and curated to cover AI-specific safety categories. BGE-M3's broad training corpus provides better coverage.

**Scale effects.** BGE-M3's substantially larger model capacity (568M parameters vs. HateBERT's 110M) likely contributes to richer representations regardless of domain specificity. Scale effects in pre-trained language models are well-documented [CITE] and may dominate domain-specific fine-tuning at this task.

### 5.2 The Retrieval–Classification Inversion

The most significant finding is the non-monotonic relationship between retrieval quality and downstream classification performance. BGE-M3 retrieves more policy-consistent analogues at every category, yet HateBERT's pipeline produces higher macro F1.

We attribute this to a distinction between **rule precision** and **rule usability**. BGE-M3's retrieved analogues are more homogeneous within policy categories, so Claude Sonnet induces rules that accurately capture the intent-level distinctions between categories. However, these intent-based rules require the downstream classifier to exercise fine-grained semantic judgement — a demand that may exceed what a small, fast model like Haiku can reliably perform at inference time.

HateBERT's retrieved analogues are noisier but share strong surface-level features (specific vocabulary, action types). The rules induced from them are more lexically grounded and operationally concrete. Haiku can apply these rules more consistently, yielding higher classification accuracy despite the rules being less semantically precise.

This points to a trade-off that is absent from retrieval-only evaluations: **the complexity of the induced rule must be matched to the capacity of the downstream model**. A more capable downstream model (e.g., Claude Opus) might realise the full benefit of BGE-M3's more precise rules.

### 5.3 The Policy-Semantics Gap Revisited

Our results reveal the policy-semantics gap as a multi-layer phenomenon. At retrieval, it describes the divergence between semantic similarity and policy similarity — BGE-M3 closes this gap more than HateBERT. At the rule level, it describes the divergence between rule accuracy and rule usability — BGE-M3 rules are more accurate but less usable. At the classification level, the gap manifests as the difference between the rule-as-written and the rule-as-applied by the downstream model.

Optimising at one layer does not guarantee optimisation at the next. This suggests that end-to-end evaluation — measuring macro F1 across the full pipeline rather than P@k in isolation — is necessary for selecting the right embedding model for a retrieval-augmented moderation system.

### 5.4 Limitations

Several limitations constrain the generalisability of these findings:

- **Single dataset.** Aegis is an AI-safety focused dataset; findings may not transfer to other moderation domains (e.g., CSAM detection, financial fraud).
- **CLS token only.** For HateBERT, we use CLS token embeddings without pooling alternatives (mean pooling, etc.). Different pooling strategies may yield different results.
- **No fine-tuning.** We evaluate both models off-the-shelf. Fine-tuning HateBERT on a retrieval objective (e.g., contrastive learning with policy category pairs) could close the retrieval gap.
- **Small rule induction sample.** Master rules are aggregated from only 5 queries per category. The induced rules — and by extension the classification inversion finding — may not be stable across different random samples. Robustness checks with 30 queries per category are in progress.
- **Three categories for Phases 6–7.** Rule induction and classification evaluation cover only harassment, hate, and profanity. The remaining categories (sexual, confessions, harmless) may exhibit different patterns.
- **Single downstream model.** We use Claude Haiku 4.5 as the classifier. A more capable model might better leverage BGE-M3's semantically precise rules, potentially reversing the classification inversion. We are re-running classification with Claude Sonnet 4.6 to test this directly.
- **English only.** Both models and the Aegis dataset are English-centric.

---

## 6. Conclusion

We evaluated a three-stage retrieval-augmented moderation pipeline — retrieval, rule induction, and classification — comparing BGE-M3 (general-purpose) and HateBERT (moderation-aware) across the Aegis AI Content Safety Dataset.

At the retrieval stage, BGE-M3 outperforms HateBERT on P@10 in every violation category by an average of 8.7 pp on explicit violations and 6.4 pp on implicit violations, challenging the assumption that domain-specific pre-training improves retrieval quality for content moderation.

At the downstream classification stage, this advantage inverts: rules induced from HateBERT retrievals yield higher macro F1 (72.9% vs 68.2%) when injected into Claude Haiku. We attribute this to the distinction between rule precision and rule usability — BGE-M3's more semantically precise rules exceed the operational capacity of a small downstream model, while HateBERT's vocabulary-grounded rules are more consistently applicable.

The central lesson is that the policy-semantics gap operates at multiple levels of the pipeline, and optimising retrieval in isolation is insufficient. End-to-end evaluation — measuring classification performance across the full pipeline — is necessary for selecting the right embedding model for retrieval-augmented moderation.

Future work should investigate: (1) whether a more capable downstream classifier (e.g., Claude Opus) realises the full benefit of BGE-M3's precise rules, potentially reversing the classification inversion; (2) whether fine-tuning BGE-M3 on policy-paired data further improves retrieval without sacrificing rule usability; and (3) whether the pattern holds for larger moderation-aware models such as LlamaGuard embeddings.

---

## References

- Caselli, T., Basile, V., Mitrović, J., & Granitzer, M. (2021). HateBERT: Retraining BERT for Abusive Language Detection in English. *Proceedings of the 5th Workshop on Online Abuse and Harms.*
- Chen, J., et al. (2024). BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation. *arXiv:2402.03216.*
- Ghosh, S., et al. (2024). Aegis: Online Adaptive AI Content Safety Moderation with Ensemble of LLM Experts. *arXiv:2404.05993.*
- Thakur, N., Reimers, N., Rücklé, A., Srivastava, A., & Gurevych, I. (2021). BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models. *NeurIPS 2021 Datasets and Benchmarks Track.*
- Chen, J., Shen, E., Bavalatti, T., et al. (2024b). Class-RAG: Content Moderation with Retrieval Augmented Generation. *arXiv:2410.14881.* (Meta GenAI)
- Lu, H., Mou, Y., & Wu, B. (2026). CHAIRO: Contextual Hierarchical Analogical Induction and Reasoning Optimization for LLMs. *arXiv:2604.10502.*
- Shi, J., Liang, H., Shen, X., et al. (2025). Embedding-based Retrieval in Multi-Modal Content Moderation. *ACM Digital Library.* (TikTok)
- Yew, W. C., Fan, X., Sarkar, K., et al. (2026). Dynamic Content Moderation in Livestreams: Combining Supervised Classification with MLLM-Boosted Similarity Matching. *KDD '26, arXiv:2512.03553.* (TikTok)


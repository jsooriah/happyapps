---
type: post
title: Building an agentic RAG tool to support my hobby research into the history of the French Revolution in the Indian Ocean
description: Academic research generates an enormous volume of PDF documents—papers, theses, archival materials, and historical analyses. Everytime I have a chance, I am digging into a huge amount of history related complex topics related to the French revolution period in the Indian Ocean. This history and its impact spans over decades across multiple locations like the Mascarene Islands, India, and of course, France and the UK as well. Given the huge amount of information that my brain needs to process a get a good understanding of all the intricacies going on at that time, and given the limited time I have as well to dig into these huge amount of documentary materials, I have decided to build a RAG pipeline powered by graph databases to help me out. Of course, traditional RAG approaches hit fundamental limitations. Modern LLMs have context windows ranging from 128K to 200K tokens, but a single comprehensive research paper can consume 20,000+ tokens. A research corpus of 50 papers quickly exceeds 1 million tokens—far beyond what any model can process in a single query. Simply "uploading PDFs" to a chat interface doesn't work at scale.
This experiment addresses that challenge head-on: building a Retrieval-Augmented Generation (RAG) system that transforms raw research PDFs into an intelligent, queryable knowledge base augmented with relationship understanding through graph technology.
publication: 2025-01-12 11:27:12
tags:
  - aiengineering
authors:
  - joel-sooriah
featured: false
redirects:
    - from: building-an-agentic-rag-tool-to-support-my-hobby-research-into-the-history-of-the-french-revolution-in-the-indian-ocean
---

Building an agentic RAG tool to support my hobby research into the history of the French Revolution in the Indian Ocean
-----------------------------------------------------------------------------------------------------------------------

**The Challenge: Research Documents and Context Windows**

Academic research generates an enormous volume of PDF documents—papers, theses, archival materials, and historical analyses. Everytime I have a chance, I am digging into a huge amount of history related complex topics related to the French revolution period in the Indian Ocean. This history and its impact spans over decades across multiple locations like the Mascarene Islands, India, and of course, France and the UK as well. 

Given the huge amount of information that my brain needs to process a get a good understanding of all the intricacies going on at that time, and given the limited time I have as well to dig into these huge amount of documentary materials, I have decided to build a RAG pipeline powered by graph databases to help me out. 

Of course, traditional RAG approaches hit fundamental limitations. Modern LLMs have context windows ranging from 128K to 200K tokens, but a single comprehensive research paper can consume 20,000+ tokens. A research corpus of 50 papers quickly exceeds 1 million tokens—far beyond what any model can process in a single query. Simply "uploading PDFs" to a chat interface doesn't work at scale.

This experiment addresses that challenge head-on: building a Retrieval-Augmented Generation (RAG) system that transforms raw research PDFs into an intelligent, queryable knowledge base augmented with relationship understanding through graph technology.

**Why Naive RAG Falls Short**

Naive RAG implementations follow a straightforward pattern: split documents into chunks, embed them, store in a vector database, and retrieve relevant chunks for each query. This works for simple use cases but breaks down with academic research:

**Problem 1: Naive Chunking Destroys Context**

Fixed-size chunking (e.g., "split every 500 tokens") cuts through sentences, paragraphs, and sections indiscriminately. An argument that spans multiple paragraphs becomes fragmented across chunks, losing the logical flow that makes it comprehensible.

**Problem 2: Semantic Similarity Misses Relationships**

Vector similarity finds passages that "sound like" the query, but research questions often require understanding relationships. "How did Napoleon's policies affect Mauritius?" requires connecting information about Napoleon (one context) with Mauritius (another context) through their relationship—something pure vector similarity cannot capture.

**Problem 3: No Entity Awareness**

Naive RAG treats text as anonymous content. It has no understanding that "Bonaparte," "Napoleon," and "the Emperor" refer to the same person, or that mentions of "Port Louis" across different documents refer to the capital of Mauritius.

**Problem 4: Citation and Provenance Loss**

Researchers need to trace answers back to specific sources with page numbers. Naive implementations lose this metadata during chunking.

The Experiment: Agentic RAG with Graph Enhancement
--------------------------------------------------

This system implements a multi-stage pipeline that addresses each limitation through purpose-built components:


Stage 1: Intelligent PDF Ingestion
----------------------------------

**PDF Parsing with PyMuPDF**

The ingestion pipeline begins with PyMuPDF (fitz), chosen for its ability to extract text while preserving structural information:

Page-level extraction: Each page is processed separately, maintaining page number metadata for citations
Layout preservation: The parser respects reading order, handling multi-column layouts common in academic papers
Metadata extraction: Title, author, creation date, and other PDF metadata are captured for filtering

**Semantic Chunking: Respecting Document Structure**

The chunking strategy is the critical differentiator from naive implementations. The \`SemanticChunker\` operates on several principles:

**Token-Based Sizing**

Rather than character counts, chunks are sized using tiktoken (OpenAI's tokenizer). This ensures chunks fit precisely within embedding and LLM context limits:

**Hierarchical Split Points**

The chunker finds split points in priority order:

1.Section headings (detected via regex patterns for "Chapter", "Introduction", etc.)
2.Paragraph breaks (double newlines)
3.Sentence endings (period + space patterns)
4.Word boundaries (last resort)

This ensures chunks never cut mid-sentence when paragraph or section boundaries are available.

**Overlap for Context Continuity**

A 10-15% overlap between consecutive chunks (configurable, default 100 tokens) ensures that context flows across boundaries. If a concept is introduced at the end of one chunk, the overlap carries it into the next:



Stage 2: Embedding Generation
-----------------------------

Chunks are converted to 1536-dimensional vectors using OpenAI's \`text-embedding-3-small\` model. This model offers an optimal balance:

Accuracy: Competitive with larger embedding models on retrieval benchmarks
Speed: Fast inference enables batch processing of large corpora
Cost: Economical for research-scale datasets


Stage 3: Vector Storage with Qdrant
-----------------------------------

**Why Qdrant**

Several vector databases exist (Pinecone, Weaviate, Milvus, ChromaDB), but Qdrant was selected for specific technical advantages:

**1. Local-First Operation**

Qdrant runs as a local Docker container or embedded process. For research applications where data sensitivity matters, having full control over where vectors are stored is crucial. No data leaves the researcher's machine.

**2. Rich Filtering Capabilities**

Qdrant supports complex filters on payload (metadata) during search. This enables queries like "find similar content, but only from papers published after 2010" or "search within this specific source document":

**3. HNSW Indexing with Tunable Parameters**

Qdrant uses HNSW (Hierarchical Navigable Small World) graphs for approximate nearest neighbor search. The parameters are configurable:


**4. Hybrid Search Support**

The system implements hybrid retrieval combining vector similarity with keyword matching.

Stage 4: Entity Extraction and Knowledge Graph
----------------------------------------------

This is where the system naive RAG. The \`EntityExtractor\` uses GPT-4o to identify named entities and relationships from each chunk:

**Entity Types for Historical Research**

The extraction is domain-aware:

\| Type | Examples |
\|------|----------|
\| PERSON | Napoleon Bonaparte, Toussaint Louverture |
\| LOCATION | Mauritius, Port Louis, Pondicherry |
\| DATE | 1789, 18th century, Revolutionary period |
\| EVENT | Storming of the Bastille, Treaty of Paris |
\| ORGANIZATION | East India Company, National Assembly |
\| SHIP | Naval vessels in colonial trade |
\| DOCUMENT | Declaration of the Rights of Man |

**Relationship Extraction**

Beyond entities, the system identifies how they connect:
\- PARTICIPATED\_IN: Person → Event
\- LOCATED\_IN: Entity → Location
\- GOVERNED: Person → Territory
\- CAUSED: Event → Event
\- CONTEMPORARY\_OF: Person → Person


**Entity Resolution**

The extractor maintains a cache for deduplication, recognizing that "Bonaparte," "Napoleon," and "the Emperor" refer to the same entity;

**Graph Storage with NetworkX**

Entities and relationships form a knowledge graph stored in NetworkX, exportable to GraphML for visualization in tools like Gephi or Neo4j:

Stage 5: Intelligent Retrieval
------------------------------

The retrieval stage combines multiple strategies:

**Hybrid Retrieval**

1\. \*\*Vector Search\*\*: Find semantically similar chunks
2\. \*\*Keyword Boost\*\*: Re-rank based on query term presence
3\. \*\*Graph Expansion\*\*: If the query mentions "Napoleon," also retrieve chunks about entities connected to Napoleon in the knowledge graph

**Retrieval Modes**

The system supports different retrieval strategies:

Vector: Pure semantic similarity
Keyword: Traditional keyword matching
Hybrid: Combined vector + keyword (default)
Graph: Graph-enhanced retrieval using entity relationships


**Context Assembly**

Retrieved chunks are assembled into a context window respecting token limits.

Stage 6: Answer Generation
--------------------------

The final stage uses GPT-4o to generate answers from the retrieved context. The prompt engineering ensures:
- Grounded responses: Answers cite specific sources
- Historical accuracy: The model is instructed to prioritize factual accuracy
- Source attribution: Each claim traces to specific documents and pages


**When I upload a PDF, here is what is supposed to happen:**
1\. Parse: PyMuPDF extracts text from each page
2\. Chunk: SemanticChunker creates \~800 token chunks at paragraph boundaries
3\. Embed: OpenAI generates 1536-dim vectors for each chunk
4\. Store: Qdrant indexes vectors with full metadata
5\. Extract: GPT-4o identifies entities (Napoleon, Mauritius, 1810) and relationships
6\. Graph: NetworkX builds the knowledge graph

**When I ask a question like "How did British rule affect Mauritius after 1810?":**
1\. Embed Query: Convert question to vector
2\. Retrieve: Qdrant finds similar chunks; graph expands to related entities
3\. Assemble: Top chunks form context within token limits
4\. Generate: GPT-4o produces answer with source citations
5\. Display: Streamlit shows answer, sources, and expandable context



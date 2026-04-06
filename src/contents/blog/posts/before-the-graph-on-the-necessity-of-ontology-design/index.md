---
type: post
title: Before the Graph - On the Necessity of Ontology Design
description: I had been deep into GRAPHOS (Graph-based Research Assistant for Historical and Ontological Sources) for months — as a hobby — an AI-powered research platform to make the history of Mauritius and the Mascarene Islands accessible to everyone — I assumed the hard part would be the ingestion pipeline. Parse the PDFs. Extract the entities. Build the graph. Let the LLM answer questions.
publication: 2026-04-06 14:43:42
tags:
  - graphrag
  - graphos
  - aiengineering
authors:
  - joel-sooriah
featured: false
redirects:
    - from: before-the-graph-on-the-necessity-of-ontology-design
---

There is a particular kind of mistake you can only make once you already know quite a lot.

I had been deep into GraphRAG for months — not as a hobby, but as a professional obsession. My day job building content moderation platforms had taught me to think in graphs: entities, relationships, traversal, context. When I started sketching what would become my most personal project — an AI-powered research platform to make the history of Mauritius and the Mascarene Islands accessible to everyone — I assumed the hard part would be the ingestion pipeline. Parse the PDFs. Extract the entities. Build the graph. Let the LLM answer questions.

I was wrong about where the hard part was.

## The Seduction of the Pipeline

GraphRAG is, on the surface, a satisfying technical problem. You have documents. You extract entities and relationships. You store them in a graph. You traverse that graph to answer questions that flat vector search cannot. The pipeline has clear stages, clear tools, clear metrics for success.

This clarity is a trap.

It invites you to think of the graph as a container — something you fill with facts extracted from documents — rather than as an argument. A claim about what kinds of things exist in a domain, what those things can do to each other, and what distinctions are worth preserving at the infrastructure level.

The pipeline asks: how do I get data into the graph?

The prior question, which the pipeline cannot ask on your behalf, is: what should the graph be capable of saying?

That prior question is what ontology design answers. And for a project about Mascarene Islands history — five centuries of colonialism, slavery, migration, and cultural formation — getting that question wrong does not produce a technically flawed system. It produces a historically dishonest one.

## What an Ontology Actually Is

An ontology is not a database schema, though it informs one. It is not a taxonomy, though it contains one. It is the formal answer to a question that most technical builders skip because it feels philosophical: what kinds of things exist in this domain, and what kinds of relationships are possible between them?

The surface layer of this question is technical. What entity types do I need? What relationship types connect them? What constraints govern those relationships? These prevent the graph from encoding nonsense — logical contradictions that would corrupt traversal and degrade answers.

But below that surface layer is something harder and more important: the ontology is a set of decisions about what deserves to be a first-class citizen in your knowledge structure. What gets its own node. What gets reduced to a property. What relationships are typed precisely enough to be queried. What distinctions are considered worth preserving.

Those decisions are never neutral. They reflect a theory of what matters in the history you are trying to represent. And in a history as contested as that of the Mascarene Islands, the theory embedded in your ontology is itself a historiographical position.

## The Problem of Flat Accounts

History as it is usually written is a flat account. Narrative prose connects events through causation and chronology, but it does not formalise the types of those connections. A governor authorises a mission. An officer executes it. A place is named after the executor. These are three different kinds of relationship — authorisation, execution, commemoration — but in a narrative they appear as one continuous sentence.

When you extract entities and relationships from that narrative without a prior ontology, you inherit its flatness. The extraction picks up the actor most prominently associated with the event and connects them to the outcome. The authorisation chain disappears. The distinction between deciding and doing, between executing and being remembered, collapses into a single edge.

The result is a graph that is factually accurate at the sentence level and historically misleading at the structural level. It does not contain false information. It contains insufficient relationship types to represent what actually happened.

This is the failure mode that under-typed graphs share with flat accounts: they remember the visible actor and lose the decision-making chain. In naval history, this erases a governor's final act. In the history of slavery, it erases the institutional logic that determined whether people were rescued or abandoned.

An ontology that defines `[AUTHORIZED]`, `[EXECUTED]`, and `[NAMESAKE_OF]` as distinct relationship types — rather than collapsing them into a single `[INVOLVED_IN]` — is not adding technical complexity. It is refusing to repeat the archive's own simplifications at the infrastructure level.

## The Problem of Temporal Flatness

Relationship typing is one dimension of the problem. Temporal modelling is another, and in some ways more insidious, because it is harder to notice when it is absent.

A flat entity node represents a thing as it is — a snapshot. A `PERSON` node with properties for name, role, and institution captures how someone appears at a given moment in the record. For many historical actors, this is sufficient. Naval officers have careers that change slowly and are documented systematically.

But history also contains people whose fundamental status changes — sometimes legally, sometimes catastrophically, sometimes through the slow accumulation of survival. A person who is legally classified as property in one document, as a survivor in another, as a freed person in a third, and as a renamed individual in a fourth cannot be represented by a flat node without erasure. To flatten that trajectory into a single `legal_status` attribute is not a technical decision. It is a decision about whose story the graph is designed to hold.

The ontology must model `LEGAL_STATUS` as temporal — something that changes, that has a before and after, that can be contested and revised. This requires not just a different data structure but a different conceptual commitment: the recognition that for some people in this history, the most important fact about them is not what they were, but the arc of what they became.

A system that cannot represent that arc does not just fail technically. It reproduces, in its infrastructure, the same categorical rigidity that colonial administration used to manage enslaved people — classifying them once, at the point of acquisition, and never updating the record.

## The Problem of Absence

Perhaps the most counter-intuitive insight of ontology design is that what the graph does not contain is as significant as what it does.

Every ontology implicitly defines not just what exists but what is worth tracking. An entity type that does not appear in the schema is an entity type that will never surface in an answer, never generate a follow-up question, never become visible as a gap in the record.

This matters acutely for a history built substantially on colonial archives. Those archives were meticulous about some things — ship manifests, harbour depths, administrative salaries, engineering plans — and silent about others. The silence is not neutral. It is the archive expressing, systematically, what the colonial administration considered worth recording.

If the ontology is derived solely from what the archive contains, it inherits those silences as structural features. The things the archive did not track — the names of enslaved people, the oral knowledge of indentured labourers, the domestic arrangements of plantation workers — will be absent from the graph not because the history did not happen, but because the ontology did not make space for it.

An ontology designed with historiographical intention makes those absences visible rather than invisible. It includes entity types and relationship types for which the current corpus has little evidence — not because the data exists, but because its absence is itself a historical fact worth representing. A node with no edges is a different kind of knowledge claim than a node that was never defined. The first says: this person existed, and we cannot connect them to anything else in the record. The second says: this kind of person was not considered worth tracking.

Those are not the same statement. The ontology is the only structure that can hold the difference between them.

## The Governance Implication

An ontology that takes these questions seriously cannot be designed once and fixed. It must evolve — with the corpus, with the research questions, and most importantly with the growing understanding of what the history actually contains and who it concerns.

This evolution is not a sign of poor initial design. It is a sign that the platform is doing what a research tool should do: generating new questions that reveal the limits of its current structure.

But evolution requires governance. Ontology changes are not equivalent to data updates. When a new relationship type is added, it changes what the graph is capable of saying — not just about new documents, but potentially about documents already ingested. When an entity type is split into subtypes, it changes the categories through which users understand the history. When a property is made temporal, it changes which questions can be asked.

These are decisions that should be documented, reasoned about, and traceable. Not because ontology design is bureaucratic, but because the changelog of an ontology is itself a historical document — evidence of how the platform's understanding of Mascarene history developed over time. Future researchers will want to know not just what the graph contains, but when it became capable of containing it, and why.

That traceability is not overhead. It is integrity.

## What the Ontology Is For

I started this project thinking the hard problem was ingestion. Get the documents. Parse them well. Extract entities reliably. Build the graph.

The hard problem is prior to all of that. It is the question you have to answer before you write a single line of extraction code: what is a thing, in this history, and what can one thing do to another?

For the Mascarene Islands, that question is never purely technical. The history involves people who were legally classified as property, institutions that generated meticulous records of harbour depths and almost no records of human suffering, and a colonial epistemology that systematically decided what was worth naming and what was not.

An ontology designed without confronting those facts will not just be technically incomplete. It will be complicit in the same logic that shaped the archive — privileging the well-documented over the poorly documented, the named over the unnamed, the institutional over the personal, the executor over the authoriser, the cartographer over the survivor.

The graph cannot correct the archive. But it can refuse to reproduce its hierarchies as neutral infrastructure.

That refusal begins with the ontology. Before the data. Before the pipeline. Before the first entity is extracted or the first relationship is typed.

The map before the map has to know what it is mapping — and for whom. And it has to have made, deliberately and documentably, the decisions about what deserves to exist in the world it is about to construct.

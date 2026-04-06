---
type: post
title: Before the Graph On the Necessity of Ontology Design
description: I have been dwelling into GraphRAG for some time now, vibe coding in my spare time. I started vibe coding GRAPHOS — a Graph-based Research Assistant for Historical and Ontological Sources (I recently changed the project name to reflect the importance of ontologies in this piece of work) — I assumed the hard problem would be the ingestion pipeline. Parse the documents. Extract the entities. Build the graph. Let the system answer questions.
I was wrong about where the hard problem was.
publication: 2026-04-06 08:00:00
tags:
  - graphrag
authors:
  - joel-sooriah
featured: false
redirects:
    - from: before-the-graph-on-the-necessity-of-ontology-design
---

I have been dwelling into GraphRAG for some time now, vibe coding in my spare time. I started vibe coding GRAPHOS — a Graph-based Research Assistant for Historical and Ontological Sources (I recently changed the project name to reflect the importance of ontologies in this piece of work) — I assumed the hard problem would be the ingestion pipeline. Parse the documents. Extract the entities. Build the graph. Let the system answer questions.

I was wrong about where the hard problem was.

## The Idea

History lives in fragments: in archives, in academic papers, in documents scattered across institutions that most citizens will never visit. The idea behind GRAPHOS was straightforward in principle: ingest the research, build the graph, and let citizens, students, and scholars ask questions in plain language — receiving answers drawn from the actual historical record, with sources, with nuance, with the kind of reasoning that connects distant events across time.

GraphRAG was the right technology for a history research assistant of this kind. Historical knowledge is inherently relational. Events connect to people, people connect to places, places connect to institutions, institutions connect to documents. A graph captures what flat vector search cannot: the structure of history, not just its semantic surface.

What I had not fully reckoned with was this: before you can build the graph, you have to decide what kinds of things exist in your world — and what kinds of things can happen between them.

## What Ontology Actually Means

An ontology is not a database schema, though it informs one. It is not a taxonomy, though it contains one. It is the formal answer to a question that most technical builders skip because it feels philosophical:

> What kinds of things exist in this domain, and what kinds of relationships are possible between them?

For a history research assistant like GRAPHOS, this question has layers.

The surface layer is technical. What entity types do you need? What relationship types connect them? What constraints govern those relationships? These prevent the graph from encoding nonsense — relationships between entities that have no meaningful connection, or actions attributed to the wrong category of actor.

But there is a deeper layer, and it is not technical at all.

A flat entity model works well for certain categories of historical actor. It works less well the moment you try to represent actors whose status, identity, or role changes over time — or who appear differently across different documents depending on who wrote them and why. The same person can hold multiple legal statuses, multiple names, and multiple relationships to power across a single archive. A schema that cannot hold this does not just have a technical limitation. It has a historiographical one.

The decision about how to model change over time — whether status is a fixed property or a temporal trajectory, whether identity is singular or multiple — is not a database decision. It is a decision about whose story the history research assistant is designed to tell.

## The Three Layers of Ontology Design

Working through these questions, I came to understand ontology design in GRAPHOS as operating simultaneously at three levels.

**The structural level** is where most builders start and stop. Entity types, relationship types, cardinality constraints. This is necessary but insufficient. A structurally correct ontology can still be historiographically careless.

**The relational level** is where the real work happens. The question here is not what things exist, but what kinds of connections between things are meaningful and distinct. This is where relationship typing becomes critical.

Consider the difference between the person who authorises an action, the person who executes it, and the person who gets commemorated for it. In a flat account, these collapse into one. In a properly typed graph, they are three distinct relationships — and the difference between them can be the difference between a historical actor being visible in the record or disappearing from it entirely.

This is not an abstract problem. Archives systematically record some relationships and not others. A graph that inherits those omissions at the schema level does not just reflect the archive's blind spots. It encodes them as infrastructure.

**The epistemological level** is the most demanding. Not all knowledge in a historical corpus is the same kind of knowledge. A primary source, a secondary interpretation, a transcription of oral testimony, and an archaeological inference are not equivalent. A graph that treats them identically is not technically wrong. It is epistemologically careless — and for a history research assistant serving researchers, that carelessness will surface in every answer the system generates.

## Why the Ontology Must Evolve

A static ontology is a sign that your corpus isn't growing — or that your understanding of it isn't deepening.

Three forces drive ontology evolution in a project like GRAPHOS, and all three are inevitable.

**The first is new document types.** An ontology designed around one category of source will be incomplete the moment you ingest a different kind of document. New sources surface entity types and relationship types that simply did not exist in your earlier corpus. Their absence was not an oversight. Their addition is not a correction. It is the ontology growing in response to what the material demands.

**The second is new research questions.** The questions a history research assistant cannot answer are as informative as the questions it can. When a researcher asks something the graph cannot traverse, it is often not because the data is absent — it is because the relationship type that would make the traversal possible was never defined. Every unanswerable question is a signal that the ontology needs to grow.

**The third is deepening historiographical understanding.** As you work more closely with a corpus, you come to understand its structure differently. Categories that seemed adequate reveal themselves as too coarse. Distinctions that seemed unnecessary turn out to matter enormously. This kind of evolution is not driven by new data or new questions — it is driven by growing understanding of what the history actually contains and how it is organised.

Each of these forces produces a different kind of ontology change. Some changes are purely additive — new entity types, new relationship types — and carry no risk to existing structure. Others require refinement: splitting a category that was too broad, or specialising a relationship type that was doing too much work. Occasionally, restructuring is necessary — a fundamental rethinking of how a domain is organised. These are rare, expensive, and worth doing when the understanding demands it.

## The Governance Question

An evolving ontology raises a question I had not anticipated when I first conceived GRAPHOS as a technical project: who decides?

An ontology change is not just a schema migration. It is a statement about what the history research assistant considers worth representing. Historians from different traditions will disagree about what deserves to be a first-class entity type. Those disagreements are not resolvable by technical argument. They are disagreements about what the platform is for.

This means ontology governance cannot be left implicit. It needs a lightweight but deliberate process: proposed changes documented with rationale, assessed for impact on existing structure, and recorded in a changelog that travels with the ontology itself.

The changelog is not just governance infrastructure. It is a historical document in its own right — a record of how GRAPHOS's understanding of its subject matter developed over time. Future researchers using the history research assistant will want to know not just what the ontology contains, but why it contains it, and when particular distinctions were first considered important enough to encode.

That provenance matters. An ontology without a changelog is an argument without a history.

## The Map Before the Map

I began this project thinking the hard problem was ingestion. Get the documents. Parse them well. Extract entities reliably. Build the graph.

The hard problem is prior to all of that. It is the question you have to answer before you write a single line of extraction code:

> What is a thing, in this history — and what can one thing do to another?

For any history as layered and contested as the ones GRAPHOS is designed to serve, that question is never purely technical. The corpus contains actors who were classified differently by different institutions at different times. It contains events whose significance depends entirely on which relationships you choose to make visible. It contains absences — things the archive chose not to record — that are themselves historical evidence if you build a schema capable of representing them.

An ontology that inherits the archive's categories without examining them does not produce a neutral graph. It reproduces, at the infrastructure level, the same decisions about what counts and who matters that shaped the archive in the first place.

The map before the map has to know what it is mapping — and why.
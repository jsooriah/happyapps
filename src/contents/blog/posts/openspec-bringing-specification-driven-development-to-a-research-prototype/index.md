---
type: post
title: OpenSpec Bringing Specification-Driven Development to a Research Prototype
description: Research prototypes have a particular failure mode: they work, and then they grow. What starts as a script to test an idea becomes a pipeline. The pipeline gains a frontend. The frontend gets tabs. New retrieval modes are added. A knowledge graph appears. An agent memory layer. Six months later, the codebase is genuinely complex — but the only documentation is the code itself, scattered comments, and whoever wrote it remembers *most* of what it does.
publication: 2026-04-18 13:46:53
tags:
  - This is exactly where the RAG assistant for historical research in the Indian Ocean found itself. Eight distinct subsystems — ingestion
  - chunking
  - embedding
  - retrieval
  - generation
  - knowledge graph
  - agent memory
  - evaluation — each with non-obvious constraints
  - silent failure modes
  - and subtle interactions. No single file explained how they fit together or *why* certain decisions were made.
authors:
  - joel-sooriah
featured: false
redirects:
    - from: openspec-bringing-specification-driven-development-to-a-research-prototype
---


---
type: post
title: OpenSpec Bringing Specification-Driven Development to a Research Prototype
description: Research prototypes have a particular failure mode - they work, and then they grow. What starts as a script to test an idea becomes a pipeline. The pipeline gains a frontend. The frontend gets tabs. New retrieval modes are added. A knowledge graph appears. An agent memory layer. Six months later, the codebase is genuinely complex — but the only documentation is the code itself, scattered comments, and whoever wrote it remembers most of what it does.This is exactly where the RAG assistant for historical research in the Indian Ocean found itself. Eight distinct subsystems — ingestion, chunking, embedding, retrieval, generation, knowledge graph, agent memory, evaluation — each with non-obvious constraints, silent failure modes and subtle interactions. No single file explained how they fit together or *why* certain decisions were made.
publication: 2026-04-18 13:46:53
tags:
  - openspec
authors:
  - joel-sooriah
featured: false
redirects:
    - from: openspec-bringing-specification-driven-development-to-a-research-prototype
---

# OpenSpec: Bringing Specification-Driven Development to a Research Prototype

## The Problem with Prototype Codebases

Research prototypes have a particular failure mode: they work, and then they grow. What starts as a script to test an idea becomes a pipeline. The pipeline gains a frontend. The frontend gets tabs. New retrieval modes are added. A knowledge graph appears. An agent memory layer. Six months later, the codebase is genuinely complex — but the only documentation is the code itself, scattered comments, and whoever wrote it remembers *most* of what it does.

This is exactly where the RAG assistant for historical research in the Indian Ocean found itself. Eight distinct subsystems — ingestion, chunking, embedding, retrieval, generation, knowledge graph, agent memory, evaluation — each with non-obvious constraints, silent failure modes, and subtle interactions. No single file explained how they fit together or *why* certain decisions were made.

OpenSpec was introduced to fix that.

---

## What OpenSpec Actually Is

OpenSpec is not a documentation framework. That distinction matters.

Documentation describes what code does after the fact. It drifts. It becomes outdated the moment someone refactors a function without updating the README. It is written for readers who want to understand the past.

Specifications describe what the system *should* do — and they are written before or alongside implementation, not after. They are the source of truth that code is validated against, not the other way around.

OpenSpec formalises this with a lightweight structure:

```
openspec/
├── specs/          ← source of truth (one domain per folder)
└── changes/        ← proposed modifications (one folder per change)
    └── archive/    ← completed changes
```

Each spec uses a consistent language: `### Requirement:` headings, `#### Scenario:` sub-sections with GIVEN/WHEN/THEN structure, and SHALL/MUST/SHOULD to signal obligation strength. Changes follow a proposal → delta spec → tasks → implement → archive lifecycle.

This is not bureaucracy. It is structure that pays for itself.

---

## What Was Found During the Gap Analysis

When the first eight domain specs were written for this project — ingestion, retrieval, generation, knowledge graph, agent memory, frontend, evaluation, configuration — the process was deliberately slow. Every spec section required reading the actual source code to verify the claim being made.

The result was uncomfortable: **26 discrepancies** between what a reasonable person would assume the system does and what it actually does.

Some were documentation gaps — things that worked correctly but were never articulated. Others were genuine bugs:

**Graph score overflow.** The retrieval score formula `len(overlap) * 0.3` was applied without a ceiling. Three or more matching entities would push the score above 1.0, breaking score normalisation downstream. The fix was a one-line `min(..., 1.0)` — but the bug had existed undetected because there was no spec to assert that scores must be bounded.

**Custom prompt injection.** The `generate()` method accepted a `custom_prompt` parameter with no validation. An empty string or a 50,000-character prompt were both accepted silently, with unpredictable LLM behaviour as the result. The spec requirement forced the validation code into existence.

**Embedding dimension mismatch.** Changing `EMBEDDING_DIMENSIONS` without recreating the Qdrant collection produces a silent failure at query time — vectors of the wrong shape are stored and searched incorrectly. There was no startup check. Writing the spec requirement for the configuration domain made the gap obvious, and a `_KNOWN_DIMENSIONS` validation was added to `config.validate()`.

This is the first and most immediate value of specifications: **they surface assumptions**. When you write "the system SHALL validate X", you are forced to check whether it actually does.

---

## Example 1: A Spec That Caught a Real Bug

**The spec requirement (`retrieval/spec.md`):**

```markdown
### Requirement: Graph Score Normalisation
The graph score SHALL be bounded to [0.0, 1.0].

#### Scenario: Multiple entity matches
- GIVEN a retrieved chunk shares 4 or more entity names with query results
- WHEN the graph score is computed
- THEN the score MUST NOT exceed 1.0
```

**What the code actually did before the spec was written:**

```python
# src/rag/retriever.py:360
r.graph_score = len(overlap) * 0.3  # 4 matches → 1.2, which is invalid
```

**The fix the spec forced:**

```python
r.graph_score = min(len(overlap) * 0.3, 1.0)
```

No test had caught this. No one had noticed. Writing "SHALL be bounded" required checking the code — and the check failed.

---

## Example 2: A Constraint Made Legible

**The spec requirement (`agent-memory/spec.md`):**

```markdown
#### Scenario: Browser refresh
- GIVEN a user refreshes the Streamlit page
- WHEN the frontend re-initialises
- THEN a new asyncio event loop is created and stored in `st.session_state`
- AND a new session UUID is generated
- AND the previous session's traces are NOT automatically resumed
```

Without the spec, this looks like a bug. Users who refresh lose their session context. Someone unfamiliar with the codebase might "fix" it by reusing the event loop across refreshes — which would break Neo4j connections because the driver is bound to the loop created at init time.

With the spec, the scenario documents that this is intentional behaviour with a specific technical reason. The constraint is preserved even when someone refactors the init code.

---

## Example 3: A Change Proposal That Defined Scope

**`openspec/changes/application-agents/proposal.md` (excerpt):**

```markdown
**In scope:**
- ResearchAgent class using Claude with five tools
- ToolExecutor wiring tools to existing retriever and graph builder
- RAGPipeline.research() method delegating to ResearchAgent
- "agent" mode in the Streamlit frontend mode selector

**Out of scope:**
- Streaming agent responses to the UI
- Agent-to-agent communication
- Custom tool registration at runtime
```

Streaming was tempting — the agentic loop takes 10–30 seconds and showing intermediate tool calls would improve UX. But adding streaming would have required changes to the `QueryResult` type, the Streamlit rendering code, and potentially the generator. The proposal said explicitly: not now. The implementation stayed focused.

---

## Example 4: A Delta Spec as a Precise Brief

**`openspec/changes/application-agents/specs/generation.md`:**

```markdown
#### Scenario: Iteration limit reached
- GIVEN the agent has made 12 tool-call rounds without reaching end_turn
- WHEN the limit is hit
- THEN a final synthesis prompt is sent to Claude
- AND the partial research is returned as the answer
```

This single scenario drove three implementation decisions in `research_agent.py`:

1. `MAX_ITERATIONS = 12` as a named constant, not a magic number
2. A `_force_synthesis()` method that sends a separate final prompt rather than returning raw partial results
3. The `auto_reason` field in the returned `QueryResult` reporting tool call count and duration

All three exist because the spec made the expected behaviour explicit enough that the implementation had no ambiguity to fill in.

---

## Example 5: The Configuration Spec as a Contract

**`openspec/specs/configuration/spec.md` (Anthropic section):**

```markdown
### Requirement: Anthropic Configuration
| Variable | Default | Description |
|----------|---------|-------------|
| `ANTHROPIC_API_KEY` | — | Required for agent mode. Anthropic API key |
| `ANTHROPIC_MODEL`   | `claude-sonnet-4-6` | Claude model used by ResearchAgent |

#### Scenario: Agent mode without API key
- GIVEN `ANTHROPIC_API_KEY` is not set
- WHEN `ResearchAgent.__init__()` is called
- THEN a `ValueError` is raised with a clear message
```

**The `.env.example` entry that follows directly from it:**

```bash
# Anthropic Configuration (required for agent mode)
ANTHROPIC_API_KEY=your-anthropic-api-key-here
ANTHROPIC_MODEL=claude-sonnet-4-6
```

The spec is the contract. The `.env.example` is the operator-facing expression of that contract. The `ValueError` in `ResearchAgent.__init__()` is the enforcement. All three are consistent because all three were written against the same requirement — not independently guessed.

---

## Example 6: The Tasks File as an Audit Trail

**`openspec/changes/application-agents/tasks.md` at the start of a session:**

```markdown
- [ ] 5.2 Add `ANTHROPIC_API_KEY` to `.env.example`
- [ ] 5.3 Update `openspec/specs/configuration/spec.md` with new env vars
- [ ] 5.4 Archive this change once verified
```

This file survived a context window reset between sessions. When the conversation resumed, the two unchecked boxes were the immediate next action — no reconstruction needed, no "where were we?", no risk of forgetting. The tasks file is a bookmark that works across sessions, contributors, and AI assistants alike.

---

## The Change Lifecycle: Application-Level Agents

The second value of OpenSpec becomes visible when adding new capabilities. The introduction of the `ResearchAgent` — a Claude tool-use agent that iteratively searches documents and traverses the knowledge graph — was a non-trivial change touching five files across three layers of the stack.

Without a structured process, this kind of change arrives as a pull request with a vague title and a body that says "added agent mode". Understanding what was intended, what edge cases were considered, and why specific limits (12 iterations, 4096 max tokens, ephemeral prompt caching) were chosen requires reading the code and reverse-engineering the intent.

With OpenSpec, the change folder tells the whole story:

- `proposal.md` — why this exists, what problem it solves, what is explicitly out of scope
- `specs/generation.md` — a delta spec declaring exactly what new behaviours were ADDED, in GIVEN/WHEN/THEN form
- `tasks.md` — a checklist tracking every implementation step

Anyone reading this folder six months from now will know: the iteration limit exists because the agent must return a `QueryResult` compatible with the existing UI, which means it cannot run indefinitely. The prompt caching is explicit because the system prompt is fixed per deployment and caching it reduces API cost. These are decisions, not accidents.

The `archive/` folder preserves completed changes permanently. The `changes/` folder shows what is in flight. At any moment, the state of the system's evolution is legible.

---

## Value for the Project

For the RAG assistant specifically, OpenSpec provides three things that matter:

**A stable contract between layers.** The retrieval spec defines the exact weight distribution for hybrid mode (60% vector, 25% keyword, 15% graph). The generation spec defines the 6-message conversation history limit. The configuration spec lists every env var with its default. These are now authoritative — not inferred from code.

**A safe surface for experimentation.** This is a research prototype. The retrieval strategy will change. New entity types will be added to the knowledge graph. The agent may gain new tools. Every change that goes through the proposal → delta → tasks lifecycle is automatically scoped: what is in scope, what is not, what existing behaviour is preserved. Experiments stay experiments; they do not silently become load-bearing assumptions.

**Onboarding that works.** The `CLAUDE.md` and sub-agent definitions (spec-writer, pipeline-debugger, graph-agent, eval-analyst) give any new contributor — human or AI — an immediate map of the system. The specs give them the detail. Together they replace the institutional knowledge that lives only in the head of whoever wrote the code.

---

## Value for You as a Developer

There is a more personal dimension to this.

Research projects tend to be solo or small-team efforts with long gaps between active development sessions. You build something in a burst of intensity, understand it completely, step away for two months, and return to a codebase that has become slightly foreign. The mental overhead of reconstruction — what does this parameter do, why is this limit here, what was I about to add — is real and significant.

Specifications are externalised memory. When you return to this project in three months, the retrieval spec will tell you exactly how graph mode scoring works without requiring you to read `retriever.py:350-375` and reconstruct the formula. The change archive will show you what you built, when, and why. The tasks files will show you what was left unfinished.

This also changes how you interact with AI assistants working on the codebase. A sub-agent asked to modify the chunking pipeline can read `openspec/specs/ingestion/spec.md` and immediately know the boundary priority order, the overlap scope, and the hard ceiling. It does not need to infer intent from variable names. The specification is a precise brief, and precise briefs produce precise implementations.

Finally, there is the discipline effect. Writing a spec before implementing a feature forces a clarity of intent that often catches design problems before they are encoded in code. "The system SHALL support X" is easy to write. "GIVEN Y, WHEN Z, THEN the system SHALL..." requires you to think through the actual behaviour — and occasionally to notice that you are not sure what the behaviour should be, which is exactly the right moment to realise that.

---

## What OpenSpec Is Not

It is worth being clear about what has not been added.

OpenSpec is not a testing framework. It does not generate tests from scenarios. The GIVEN/WHEN/THEN language is human-readable behavioural description, not executable code.

It is not a schema validator. The specs do not enforce types or interfaces at runtime.

It is not a heavy process. There is no approval workflow, no versioning ceremony, no tooling that must be run. A change is a folder with three markdown files and a checklist. Archiving is moving a folder. The overhead is intentionally minimal.

What it is, precisely, is a habit: the habit of writing down what you intend before you implement it, and of verifying that the code does what the spec says. For a research prototype that is expected to grow, change, and eventually be handed to others, that habit is worth more than any individual feature.


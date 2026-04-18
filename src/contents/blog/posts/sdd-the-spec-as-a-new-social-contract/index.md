---
type: post
title: SDD - The Spec as a New Social Contract
description: Spec-Driven Development — SDD — is, at its best, a proposed answer to this perennial failure of translation. But it is arriving in 2026 not as a project management reform but as an engineering methodology, carried into organisations on the back of agentic AI tools. And that origin shapes everything about its promise and its limits.
publication: 2026-04-08 17:55:53
tags:
  - This article traces the state of the art as of Q1 2026
  - maps the sociotechnical experiments already underway
  - and makes the case that the spec is quietly becoming the most contested artifact in modern software delivery — not because of what it does for agents
  - but because of what it forces humans to do before the agent runs.
authors:
  - joel-sooriah
featured: true
css:
  - /happyapps/css/editorial.css
redirects:
    - from: sdd-the-spec-as-a-new-social-contract
---

# The Spec as a New Social Contract

**How a methodology born in the IDE is quietly reshaping who holds the pen on software intent — and why the most important experiments in 2025–2026 are happening at the boundary between product, engineering, and the agents that serve them both.**


---

There is a moment, familiar to anyone who has worked on a cross-functional product team, when the same sentence means different things to different people in the same room. The engineer hears a constraint. The designer hears a metaphor. The product manager hears a user story. The compliance officer hears a liability. Everyone nods. Everyone leaves and builds something different.

Spec-Driven Development — SDD — is, at its best, a proposed answer to this perennial failure of translation. But it is arriving in 2026 not as a project management reform but as an engineering methodology, carried into organisations on the back of agentic AI tools. And that origin shapes everything about its promise and its limits.

This article traces the state of the art as of Q1 2026, maps the sociotechnical experiments already underway, and makes the case that the spec is quietly becoming the most contested artifact in modern software delivery — not because of what it does for agents, but because of what it forces humans to do before the agent runs.

---

## I. How We Got Here: The Taxonomy That Stuck

In October 2025, Thoughtworks technologist Birgitta Böckeler published a memo on Martin Fowler's site that gave the field its working vocabulary.[^1] 
She had looked at three tools claiming to implement SDD — AWS Kiro, GitHub Spec Kit, and Tessl — and found not one practice but three, arranged along a spectrum of commitment:

**Spec-First** — A structured spec is written before coding begins and used during that session. The spec may or may not survive the sprint.

**Spec-Anchored** — The spec is maintained after delivery, serving as the living source of truth for ongoing evolution and maintenance.

**Spec-as-Source** — The spec is the only artifact humans edit. Code is generated from it and treated as a build artifact — never edited directly.


This taxonomy hardened quickly. A January 2026 paper on arXiv formally adopted the same three levels and added decision guidance on when each applies.[^2] The academic frame arrived faster than the tooling warranted — a sign of the field's velocity, and perhaps its anxiety.

Böckeler also drew a distinction that most practitioners had been conflating: the difference between a *spec* and a *memory bank*. Memory banks are the always-on context files — rules files, architecture guides, coding standards — relevant across all AI coding sessions in a codebase. Specs are scoped artifacts, live only for the tasks that create or change a specific feature.[^1] This distinction is not merely taxonomic. It defines the labour division: who writes the memory bank (typically a principal engineer or technical lead), who writes the spec (the open question), and who validates both (the human still in the loop).

---

## II. The Tool Landscape as of April 2026

### AWS Kiro: The Production Entrant

AWS Kiro launched in July 2025 as a VS Code fork and became, within months, the dominant reference point in SDD conversations. Its workflow is systematic: natural language prompt in, structured requirements and acceptance criteria in EARS notation out, followed by an architecture recommendation and an implementation plan with tasks sequenced by dependency.[^3]

The reception was instructive. One developer fed Kiro a spec for a simple macOS keyboard shortcut helper and received 5,000 lines of code for what should have been 800.[^4] Another tried a gnarly datetime-parsing problem and reported that the tool "forced me to stop and think more clearly about the problem I was trying to solve" — and then delivered.[^4] The tool, in other words, amplifies the quality of the spec it receives. Give it ambiguity and you get over-engineered guesswork. Give it precision and the leverage is real.

Kiro's most significant structural contribution is *steering files* — persistent, project-level documents covering product overview, tech stack, API standards, testing standards, and security policies — sitting in a `.kiro/steering/` directory alongside the specs.[^5] This is the memory bank made filesystem-real: a structured context layer that any collaborator — human or agent — can read before touching the codebase.

### GitHub Spec Kit: The Constitution Model

GitHub's Spec Kit, launched in September 2024 and iterated through 2025, introduced a workspace-centric model anchored by a "constitution" — a persistent set of project principles, technology constraints, and coding standards. The workflow exposes three explicit commands: `specify`, `check`, and `implement`. The ambition is executable specs — not static documentation but machine-runnable contracts that fail a build when they drift from the code.[^6]

The real-world use of GitHub's GraphQL schema as a living contract between product and engineering illustrates what this looks like when it works. PMs and engineers iterate on schema proposals that double as documentation; code generation produces strongly typed clients and tests so that one edit updates documentation, SDKs, and compatibility checks in lockstep.[^7] The schema is the spec: diff-able, versioned, auditable, and owned by no single role.

### Tessl: The Spec-as-Source Bet

Tessl remains the most philosophically ambitious entrant — and the most behind schedule. It raised funding on a promise of early-2025 launch, delivered a closed beta Framework and a free Spec Registry in September 2025.[^4] The Registry is valuable in its own right: it addresses the problem of AI hallucinating API surfaces by providing verified specifications for over 10,000 libraries. But spec-as-source — the model where humans only edit the spec file and never touch the generated code — remains a horizon, not a shipped product.

### Claude Code: The Terminal-Native Path

Claude Code has emerged as the practical SDD substrate for teams unwilling to adopt a new IDE. The approach relies on `CLAUDE.md` files for persistent memory, subagent orchestration, task tracking, and event hooks — a four-phase workflow (spec → context engineering → subagent execution → validation) that imposes structure on what practitioners had been calling "vibe coding chaos."[^8] The pattern is gaining traction particularly among engineers who find the IDE-based tools too opinionated about folder structure and workflow sequencing.

---

## III. The Context Turn: When the Spec Is One Layer, Not the Whole Stack

The most important conceptual development of early 2026 is not about any single tool. It is the shift from *prompt engineering* to *context engineering* as the operative frame for understanding what these systems actually need to perform reliably.

Andrej Karpathy and Shopify CEO Tobi Lütke named the shift in mid-2025, and it has since clarified practice across the field.[^9] Prompt engineering is the craft of asking a better question. Context engineering is the science of building the library that surrounds the question: the structured information pipeline — memory, retrieved documents, tool outputs, codebase state, conversation history — that the agent has access to when it reasons. Anthropic's own engineering team formalised it: "The engineering problem at hand is optimising the utility of those tokens against the inherent constraints of LLMs in order to consistently achieve a desired outcome."[^10]

> *Prompt engineering gives you better questions. Context engineering gives you better systems. The spec is one curated layer in a context stack — and the most contested one, because it carries the most human intent.*

This reframe matters for SDD directly. A spec is not, in context engineering terms, a standalone artifact. It is one curated layer in a context stack. Thoughtworks articulates the full picture: MCP servers like Context7 supplying real-time documentation; CodeConcise tools extracting knowledge graphs from legacy codebases; integration with JIRA and Confluence to support subsequent code generation.[^11] The spec compresses the planning phase into a structured document; the context stack ensures the agent can execute against the realities of the actual codebase.

What this means in practice was articulated sharply by Rahul Garg, Principal Engineer at Thoughtworks, in his February 2026 essay on *Knowledge Priming*.[^17] Garg observed that AI assistants default to what he calls "the average of the internet" — a blend of millions of repositories and tutorials from training data. Without project context, a request for a `UserService` yields Express.js when the codebase uses Fastify, class-based syntax when the codebase is functional, wrong file paths, outdated APIs. The code is syntactically correct, and completely wrong for the team. His proposed remedy is to treat curated project context as infrastructure: versioned files that prime the model before each session, structured like an onboarding packet for a new hire — architecture overview, tech stack and versions, naming conventions, code examples, anti-patterns to avoid.[^17]

There is a mechanistic reason this works. Garg explains it in terms of the attention mechanism: a focused priming document does not merely add context, it shifts the balance of what the model pays attention to. Curation matters more than volume — a well-structured fifty-line priming document outperforms a brain-dumped five-hundred-line one, because the model's attention is a finite budget and high-signal tokens displace low-signal ones.[^17]

Garg also introduces a distinction that sharpens Böckeler's memory bank concept considerably. There are two layers of context, not one. The *priming document* captures project-level context — tech stack, architecture patterns, naming conventions — relatively stable, shared across all features and sessions. The *feature document* captures feature-level context — specific decisions made during development, what was considered and rejected, what remains open, the current state of progress. Together, they form two layers of the same context strategy: the project context as the stable foundation, the feature context as the record of where things stand.[^18]

The feature document is, in essence, a living Architecture Decision Record — one that evolves in real-time as decisions are made, rather than being written after the fact. This matters because of a documented failure mode in long AI sessions: language models perform significantly worse on information placed in the middle of long contexts, as research confirms.[^18] In Garg's observation, it is not the decisions themselves that fade first, but the *reasoning behind* them. The AI might remember "we are using PostgreSQL" while forgetting *why* — and proceed to propose a schema structure that fights against PostgreSQL's relational strengths while technically complying with the stated choice. Externalising the reasoning into a feature document is the only reliable defence against this drift.

The practical implication for teams: writing a good spec is necessary but insufficient. You need a coherent context architecture — memory banks, feature documents, retrieval hooks, tool integrations — that turns the spec from a planning artefact into an executable system instruction. Most SDD tool documentation skips this. Most teams learn it the hard way.

---

## IV. The Sociotechnical Turn: Who Writes the Spec?

Here is the question that the tooling literature elides and the engineering community is just beginning to confront: in a team with a product manager, a designer, an engineer, a QA analyst, and a compliance officer, who authors the spec?

The developer reactions to Kiro are the most candid data point available. When the tool shipped, the most-shared developer comment was not about code quality — it was about identity: *"This was a great demo for a project manager. I feel like I'm a PM, not an engineer."*[^4] A subsequent post-launch analysis put it more analytically: Kiro requires a different kind of project management — you are not just writing code anymore, you are steering an AI that can get overwhelmed by complexity and occasionally needs to be told explicitly not to take shortcuts.[^4]

AWS has leaned into the identity shift explicitly, framing Kiro as a tool that lets business users describe what they need in plain English and then build, iterate, and refine working applications themselves — eliminating the translation loss that occurs when requirements pass through analysts and developers.[^12] This is not subtle. It is a claim that the spec layer democratises software authorship. Whether that claim survives contact with production-scale complexity is a different question.

The PM-authored literature on SDD is more generous and more specific. One practitioner framing is clarifying: only 10–20% of value is the code we push; the other 80–90% is the structured conversation that decides what to build. Specs make that conversation permanent, testable, and increasingly executable.[^7] The corollary is uncomfortable for both sides of the function boundary: engineers must become fluent in the language of intent, and product managers must become fluent in the language of constraints.

Garg's work on *Encoding Team Standards* adds a dimension that neither side of this debate typically acknowledges: the consistency problem.[^19] In any team, a senior engineer prompting an AI instinctively specifies architectural compliance, naming conventions, error handling, and security checks. A less experienced colleague, faced with the same task, asks the AI to "create a notification service." Same codebase. Same AI. Completely different quality gates — not just in code review, but across every kind of AI interaction: generation, refactoring, security checks. The senior's output is right not because of the tool but because of tacit knowledge built over years of reviews, production incidents, and architectural discussions. That knowledge is the team's most valuable and most fragile asset — it lives in people's heads, transfers slowly through pairing and code review, and walks out the door when someone leaves.

The solution Garg proposes is to treat AI instructions as *executable governance*: versioned, reviewed, and shared artifacts that encode team judgment consistently, regardless of who is prompting. The move is from *tacit to explicit* (surfacing what the senior knows instinctively) and from *documentation to execution* (making it a config file the workflow invokes, not a wiki page that requires someone to remember it).[^19] This has a direct bearing on the spec question: the spec itself is not enough if the team's standards for what makes a spec *good* remain tribal knowledge. Those standards need to be encoded and shared too.

> **The Core Tension:** The spec is simultaneously an engineering artifact (consumed by agents, versioned in git, validated against tests) and a product artifact (expressing user intent, business rules, acceptance criteria). No role owns it cleanly. Every attempt to assign ownership produces a political settlement, not a technical one.

---

## V. BDD's Second Life and the JTBD Connection

The older tradition that SDD draws from most directly is Behaviour-Driven Development. BDD practitioners will recognise the shape of the SDD spec immediately: structured scenarios, domain-oriented language, testable assertions. Thoughtworks makes the technical connection explicit: the spec-by-example approach in BDD is essentially a few-shot prompting technique — the structured examples that guided human developers now guide agents, at a different level of formality and at a different scale of consequence.[^11]

The lessons BDD accumulated carry forward. Specifications should use domain-oriented ubiquitous language rather than implementation-bound terms. They should follow a common scenario style — Given/When/Then — and strive for completeness without exhaustively enumerating every edge case. Clarity and determinism reduce model hallucinations; well-formed constraints help save tokens in context-window-sensitive workflows.[^11]

The Jobs-to-be-Done tradition offers a complementary lens. A well-formed job story — *When I [situation], I want to [motivation], so I can [outcome]* — is structurally isomorphic with a Gherkin scenario's Given/When/Then. Both are trying to do the same epistemic work: locate a behaviour in a context, name its trigger, and specify its expected resolution. The difference is that a job story is grounded in customer research (the Mom Test, contextual inquiry, outcome-driven innovation) while a Gherkin scenario is grounded in engineering precision. SDD, at its best, is where these two grounding traditions meet.

This convergence suggests a concrete role for the spec in cross-functional product delivery: it can serve as the *translation artefact* between JTBD research outputs and agent-legible behaviour contracts. The product manager brings the job story. The engineer brings the acceptance criterion. The spec is where they negotiate until both can live with the result — and the agent can execute it without guessing.

---

## VI. Experiments at the Boundary: What Teams Are Actually Doing

### The Drug Discovery Case

The most revealing real-world SDD experiment from early 2026 comes from an AWS industry team building a drug discovery target identification agent: three solution architects, three weeks, a production-ready multi-agent system. The coordination layer was entirely spec-based — shared Requirements.md, Design.md, and Tasks.md files gave each architect a unified architecture even as they iterated independently on their respective components.[^13]

The methodology lesson is direct: define clear acceptance criteria with stakeholders before writing any code; use steering documents to capture architecture decisions, coding standards, and integration patterns; maintain shared specification documents so that every feature is developed with a unified architecture and consistent design choices.[^13] The output — a working agent, on time, in a domain that traditionally requires months of coordination between scientists and engineers — suggests that the spec-as-coordination-layer hypothesis holds, at least for greenfield projects with disciplined teams.

### The Citizen Developer Wedge

The enterprise strategy argument is starker. Gartner projected that by 2025, 70% of new enterprise applications would use low-code or no-code technologies. IDC estimated that by 2026, more than 90% of organisations would feel the pain of the IT skills crisis, with losses reaching $5.5 trillion from product delays.[^12] SDD tools are being positioned explicitly as a response: the spec layer as a levelling mechanism, letting supply chain managers, compliance officers, and customer success leads build working software without intermediaries.

This is both the most disruptive and the most overstated framing. The evidence — including Kiro's own early case studies — shows that the elimination of intermediaries works for well-bounded, rule-expressible tasks (inventory reconciliation, compliance reporting, customer onboarding workflows) and fails for tasks requiring architectural judgment, security reasoning, or creative constraint-resolution.[^12] The spec layer lowers the floor; it does not remove the ceiling.

### The Enterprise Gap

The InfoQ enterprise analysis, published in February 2026, is the most sober current assessment. SDD shifts AI-augmented delivery from tactical prompting to collaborative intent articulation, but enterprises face real and specific gaps: workflow integration with existing CI/CD pipelines, multi-repository coordination, and — most persistently — cross-functional collaboration. Sustainable adoption requires treating specs as living, shared interfaces and evolving organisational practices around them.[^14]

The critical unresolved question is spec ownership across the feature lifecycle. In greenfield projects with a clear product owner, authorship is natural. In brownfield or platform teams, where the codebase predates the spec culture, ownership is contested. The temptation is to treat reverse-engineered specs as equivalent to intent-first specs. They are not — and the difference surfaces when the agent executes against them.

---

## VII. The Waterfall Objection and Why It Misses the Point

The most common critique of SDD — that it is waterfall with a new name — is worth addressing directly, because it contains a real warning inside a flawed argument.

The warning is real: over-formalised specifications create bureaucratic drag, slow feedback cycles, and penalise the kind of exploratory iteration that produces genuinely good software. A PM who spends three days writing a spec for a feature that takes two days to build has inverted the economics. An engineer who generates 5,000 lines against an imprecise spec and then spends a week pruning it back to 800 has also inverted them.[^4]

But the waterfall diagnosis misses the structural difference. Waterfall suffered from months-long feedback cycles, disconnection between design and implementation, and the impossibility of changing course once the plan was fixed. SDD with agentic tools can have spec-to-working-code cycles measured in minutes. The spec is not a commitment contract; it is a compression artefact — a way of focusing the agent's context so that the implementation phase is faster and the revision cycle is tighter, not longer.[^2]

Thoughtworks puts this well: the problem with traditional waterfall was not the spec; it was the feedback cycle length and the shadow architecture that emerged when implementation diverged from design without the spec ever knowing.[^11] SDD, properly practiced, addresses both: the agent validates against the spec continuously, and the spec lives in the same repository as the code, subject to the same review and versioning discipline.

---

## VIII. Toward a Practice: What Cross-Functional Pairing Actually Looks Like

The most valuable experiments in 2025–2026 are not about tool adoption; they are about the collaboration rituals that emerge around spec authorship. The underlying principle, articulated across Garg's series, is deceptively simple: the techniques that make human collaboration effective — onboarding, structured discussion, shared standards, documented decisions, continuous learning — apply equally to AI collaboration.[^20] Several concrete patterns are crystallising from practitioner accounts:

**The Five-Level Whiteboard.** Garg's *Design-First Collaboration* pattern reconstructs the whiteboarding step that AI coding tools otherwise eliminate entirely.[^21] The problem he identifies is the "Implementation Trap": AI jumps from requirement to implementation, making every technical design decision silently and embedding them invisibly in generated code. The reviewer is then forced to simultaneously evaluate scope, architecture, integration, contracts, and code quality — all at once, all entangled. The solution is five progressive levels of alignment before any code: Capabilities (what does the system need to do?), Components (what are the building blocks?), Interactions (how do they communicate?), Contracts (what are the interfaces?), and Implementation (now write the code). The hard rule: *no code until Level 5 is approved.* Each level becomes a checkpoint where disagreement is cheap to surface and resolve. Crucially, for cross-functional teams, the five levels distribute authorship naturally: PMs own Capabilities, architects own Components and Interactions, engineers own Contracts and Implementation. The spec emerges from the conversation across levels, not from any single role.[^21]

**The Spec Review as the New Sprint Planning.** Teams that have adopted SDD seriously report that the spec review session — where PM, engineer, and QA analyst read the spec together before any code is generated — produces the same alignment benefits that three-amigo conversations did in BDD, but with a higher fidelity artefact as the anchor. The spec forces the questions that sprint planning often defers: What is the failure case? What does "done" mean? What are we explicitly not building?[^6]

**The Constitution as Organisational Memory.** Kiro's steering files and Spec Kit's constitution are emerging as de facto architecture decision records — not just for AI agents but for human onboarding. New engineers and PMs alike can read the steering directory to understand a codebase's values, constraints, and history without reverse-engineering it from commit logs. Garg's seven-section anatomy of a well-structured priming document — architecture overview, tech stack and versions, curated knowledge sources, project structure, naming conventions, code examples, anti-patterns to avoid — gives this practice its most actionable shape to date.[^17] This is knowledge transfer mediated by the spec layer, not by documentation that lives in Confluence and rots.[^5]

**Encoding Standards as Executable Governance.** The most mature teams are taking a step beyond the priming document: encoding the instructions that govern every kind of AI interaction — generation, refactoring, security review, code review — as versioned, shared artifacts in the repository.[^19] The developer does not need to carry the team's full set of standards in their head; they invoke an instruction and the team's judgment is applied consistently. For cross-functional teams, this closes the quality gap between a senior and a junior contributor — not through more pairing, but through shared infrastructure that executes the senior's instincts for everyone.

**Separate Implementation and Testing Agents.** The most mature SDD practitioners are now running two agents against the same spec: one to generate code, one to generate tests. The separation of concerns creates a natural quality checkpoint — the testing agent cannot simply echo the assumptions of the implementation agent, producing independent verification of whether the spec was satisfied.[^15]

**Hybrid Workflows as the Realistic Default.** Despite the vendor framing, the honest practitioner consensus is that most teams will land on hybrid patterns: spec-first for new features with clear requirements, iterative vibe-coding for exploratory spikes, spec-anchored maintenance for anything that needs to survive more than one quarter. The key is not choosing a mode but knowing which mode a given task warrants — and having the team discipline to switch consciously.[^2]

---

## IX. What the Engineering Role Becomes

The deepest implication of SDD — and the one most carefully avoided in vendor marketing — is what it does to the identity of the software engineer.

A McKinsey analysis from early 2026 found that AI-centric organisations were achieving 20–40% reductions in operating costs and 12–14 point EBITDA improvements, driven by automation, faster cycle times, and more efficient allocation of talent.[^16] But the same analysis identified the deeper gain as cognitive leverage: fewer handoffs, less context-switching, reduced rediscovery of system knowledge. Engineers operating at a higher level of abstraction for longer periods of time.

The operative model that is emerging — articulated most clearly by CIO's engineering leadership analysis — is *delegate, review, own*. AI agents handle first-pass execution, scaffolding, implementation, testing, and documentation. Engineers review outputs for correctness, risk, and alignment. Ownership of architecture, trade-offs, and outcomes remains human. This clarity allows autonomy to scale without diluting accountability.[^16]

Charity Majors from Honeycomb captures the stakes: senior engineering has far more to do with the ability to understand, maintain, explain, and manage a large body of software over time than with code generation speed.[^4] SDD does not threaten this; if anything, it makes it the only skill that cannot be delegated. The spec requires someone who understands the system well enough to describe what it should do. The review requires someone who can tell whether the agent did what the spec said. Both require depth. Neither can be prompted away.

What Garg's *Encoding Team Standards* adds here is the mechanism by which this depth transfers.[^19] The senior engineer's instinct about what makes a good spec, what constitutes a security concern, what premature abstraction looks like — these become infrastructure rather than personal capacity. The team becomes collectively more capable not when everyone internalises the senior's knowledge but when that knowledge is encoded in a form that executes for everyone.

---

## X. The Stakes for Product Leaders

For product leaders, the SDD movement is simultaneously an opportunity and a pressure. The opportunity: specs are a native language for product thinking. User stories, acceptance criteria, edge-case enumeration, constraint articulation — these are the daily material of product management. If the spec becomes the primary artefact of software delivery, PMs are not peripheral to the development process; they are upstream of it.

The pressure: that upstreamness carries accountability. A spec that is vague, incomplete, or misaligned with user intent does not produce a misunderstanding in a retrospective. It produces 5,000 lines of code that runs. The cost of ambiguity has changed. A prompt that used to generate a few plausible sentences now generates a working — and possibly wrong — system.

This is why the JTBD tradition matters here. Jobs-to-be-Done is, at its core, a discipline for reducing the ambiguity of intent: getting beneath the feature request to the causal mechanism of demand. A job story is already a spec — it names a situation, a motivation, and an expected outcome. The gap between a job story and a Kiro spec is a gap of formalisation, not of substance. The product manager who has done the JTBD research is already holding the raw material of a good spec. What they need is the facility to formalise it in a way that an agent can consume — and a collaborative partner who can translate the constraints that the codebase places on the intent.

> *The spec is where JTBD research outputs become agent-legible behaviour contracts. The product manager brings the job story. The engineer brings the acceptance criterion. Neither can do the work alone.*

---

## XI. The Feedback Flywheel: How the Spec Culture Sustains Itself

There is a question the article has deferred until now: what keeps the spec from becoming the documentation that lives in Confluence and rots?

The honest answer is that most SDD implementations will follow the same arc as most quality initiatives before them — intensive adoption, gradual drift, eventual abandonment — unless there is a deliberate mechanism for keeping shared artifacts current and alive. Garg's *Feedback Flywheel* is the most concrete answer to this problem currently in the literature.[^22]

The core observation is simple: every AI interaction generates signal. Prompts that worked, context that was missing, patterns that succeeded, failures worth preventing. Most teams discard this signal entirely. The Feedback Flywheel is a practice for harvesting that signal systematically and feeding it back into the artifacts — the priming documents, the encoded standards, the spec templates — that shape the next interaction.

The practice operates at three cadences. After each session: a developer who discovers something worth sharing adds a line to a *learning log* in the repository — a lightweight, low-friction file that is already part of the priming context for subsequent sessions. At the retrospective: an agenda item asks what worked with AI this sprint, what friction was encountered, and what will be updated. The outputs are concrete: a priming document revision, a standards instruction refinement, a new anti-pattern documented. Periodically: a review of whether the shared artifacts remain current and whether they are actually being used.[^22]

The flywheel metaphor is apt. Each rotation of the loop — individual discovery, learning log, retrospective decision, artifact update — leaves the infrastructure a little better prepared for the next rotation. One developer's discovery that a particular constraint improves code review output becomes, through the retrospective, the team's updated review standard. The generation instruction did not need to change; the priming context changed, and the system learned.

This is also where the cross-functional dimension of SDD becomes self-sustaining. A PM who discovers that a particular job story format maps cleanly onto Kiro's EARS notation feeds that into the spec template. An engineer who finds that a certain level of acceptance criterion detail prevents over-engineering adds that to the encoding standards. A QA analyst who observes that separate testing agents consistently surface a class of issue that the implementation agent missed records that in the learning log. The shared infrastructure becomes the accumulation of everyone's experience — not just the senior engineer's.

> **The Flywheel Test:** Could you close the AI session right now and start a new one without losing anything important? If that question creates discomfort — if you feel something essential would be lost — then the context is trapped inside a medium that was never designed to preserve it. The Feedback Flywheel is the practice of making sure the answer is always yes.[^18]

---

## Coda: The Social Contract Claim

The title of this essay makes a claim that deserves to be earned, not assumed. Is the spec a social contract?

A social contract is, in the philosophical tradition, an agreement about the terms of cooperation — what each party brings, what each party owes, what the penalties for defection are. Applied to software teams: the spec, if it is working, is the artefact that encodes the terms of cooperation between product and engineering, between the organisation and its users, and now between humans and the agents that build on their behalf.

What makes the spec contractual is not its format but its function. When a spec is authored jointly, reviewed openly, versioned consistently, and enforced by both tests and agents, it does the work that job titles, story points, and design mockups have always tried and often failed to do: it makes the team's shared understanding legible, durable, and contestable. You can argue with a spec. You can version a spec. You can fail a build against a spec. You cannot do any of those things with a verbal agreement in a sprint planning session.

The patterns emerging from Garg's series — Knowledge Priming, Design-First Collaboration, Context Anchoring, Encoding Team Standards, Feedback Flywheel — are not, at base, techniques for getting better output from AI tools. They are techniques for making the team's collective intelligence durable: externalising what is currently tacit, versioning what is currently verbal, and feeding individual experience back into shared infrastructure. The spec is the most visible artefact in this system, but it is not the whole system.

The experiments of 2025–2026 suggest that the teams getting the most from SDD are not the ones who adopted the tools fastest. They are the ones who took the spec authorship ritual seriously enough to make it a cross-functional practice — who treated the spec review session as a site of genuine negotiation, not rubber-stamping, and who built the flywheel that keeps those standards from drifting. The agent executes the spec. The humans have to write one worth executing — and keep writing better ones.

That is the work. It has always been the work. The tools have just made the cost of getting it wrong faster, louder, and harder to ignore.

---

## Sources & References

[^1]: Böckeler, B. (2025, October 15). *Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl.* Thoughtworks / martinfowler.com. https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html

[^2]: Griffin, L. & Carroll, R. (2026, January). *Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants.* arXiv:2602.00180. https://arxiv.org/html/2602.00180v1

[^3]: Amazon Web Services. (2025). *Kiro: Agentic AI Development from Prototype to Production.* https://kiro.dev

[^4]: InfoQ. (2025, August). *Beyond Vibe Coding: Amazon Introduces Kiro, the Spec-Driven Agentic AI IDE.* https://www.infoq.com/news/2025/08/aws-kiro-spec-driven-agent/ · Hyperdev / Matsuoka. (2025, October). *Is AI A Bubble? I Didn't Think So Until I Heard Of SDD.* https://hyperdev.matsuoka.com/p/is-ai-a-bubble-i-didnt-think-so-until

[^5]: Amazon Web Services. (2026). *Kiro Project Init: Automated Spec-Driven Development Setup.* AWS Startups Prompt Library. https://aws.amazon.com/startups/prompt-library/kiro-project-init

[^6]: GitHub / AI News. (2025). *GitHub Spec Kit: A Guide to Spec-Driven AI Development.* Summarised via IntuitionLabs. https://intuitionlabs.ai/pdfs/github-spec-kit-a-guide-to-spec-driven-ai-development.pdf

[^7]: Wadood, S.M.T. (2025, September). *A Product Manager's Guide to Spec-Driven Development with Case Studies.* Medium. https://medium.com/@sm15nedti/a-product-managers-guide-to-spec-driven-development-with-case-studies-800151d98ff9

[^8]: Panaversity / Agent Factory. (2026, March). *Chapter 16: Spec-Driven Development with Claude Code.* https://agentfactory.panaversity.org/docs/General-Agents-Foundations/spec-driven-development

[^9]: Faros AI. (2025, December). *Context Engineering for Developers: The Complete Guide.* https://www.faros.ai/blog/context-engineering-for-developers

[^10]: Anthropic Engineering. (2025, September 29). *Why Context Engineering Is Critical for AI Agents.* Referenced in: CIO. (2025, October 31). *Context Engineering: Improving AI by Moving Beyond the Prompt.* https://www.cio.com/article/4080592/context-engineering-improving-ai-by-moving-beyond-the-prompt.html

[^11]: Thoughtworks. (2025, December). *Spec-Driven Development: Unpacking One of 2025's Key New AI-Assisted Engineering Practices.* https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices

[^12]: Amazon Web Services. (2025, November). *From Business Logic to Working Code: How Kiro Changes Who Can Build.* AWS Executive in Residence Blog. https://aws.amazon.com/blogs/enterprise-strategy/from-business-logic-to-working-code-how-aws-kiro-changes-who-can-build/

[^13]: Amazon Web Services. (2026, February). *From Spec to Production: A Three-Week Drug Discovery Agent Using Kiro.* AWS for Industries Blog. https://aws.amazon.com/blogs/industries/from-spec-to-production-a-three-week-drug-discovery-agent-using-kiro/

[^14]: intent-driven.dev / InfoQ. (2026, February 19). *Spec-Driven Development – Adoption at Enterprise Scale.* https://www.infoq.com/articles/enterprise-spec-driven-development/

[^15]: dplooy.com. (2025). *Spec-Driven Development with AI: Complete 2025 Guide.* https://www.dplooy.com/blog/spec-driven-development-with-ai-complete-2025-guide

[^16]: CIO / Foundry Expert Contributor Network. (2026, February 20). *How Agentic AI Will Reshape Engineering Workflows in 2026.* https://www.cio.com/article/4134741/how-agentic-ai-will-reshape-engineering-workflows-in-2026.html

[^17]: Garg, R. (2026, February 24). *Knowledge Priming.* Patterns for Reducing Friction in AI-Assisted Development. Thoughtworks / martinfowler.com. https://martinfowler.com/articles/reduce-friction-ai/knowledge-priming.html

[^18]: Garg, R. (2026, March 17). *Context Anchoring.* Patterns for Reducing Friction in AI-Assisted Development. Thoughtworks / martinfowler.com. https://martinfowler.com/articles/reduce-friction-ai/context-anchoring.html

[^19]: Garg, R. (2026, March 31). *Encoding Team Standards.* Patterns for Reducing Friction in AI-Assisted Development. Thoughtworks / martinfowler.com. https://martinfowler.com/articles/reduce-friction-ai/encoding-team-standards.html

[^20]: Garg, R. (2026). *Patterns for Reducing Friction in AI-Assisted Development.* Series introduction. Thoughtworks / martinfowler.com. https://martinfowler.com/articles/reduce-friction-ai/

[^21]: Garg, R. (2026, March 3). *Design-First Collaboration.* Patterns for Reducing Friction in AI-Assisted Development. Thoughtworks / martinfowler.com. https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html

[^22]: Garg, R. (2026, April). *Feedback Flywheel.* Patterns for Reducing Friction in AI-Assisted Development. Thoughtworks / martinfowler.com. https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html

---

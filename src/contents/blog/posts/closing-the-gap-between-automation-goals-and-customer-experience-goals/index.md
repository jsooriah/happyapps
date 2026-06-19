---
type: post
title: Closing the Gap Between Automation Goals and Customer Experience Goals
description: Most organizations building chatbots or voice assistants frame their objectives around two goals - automation and customer experience. These goals are often treated as if they pull in opposite directions. Automation is associated with efficiency, cost reduction, and scale — qualities that read as cold and transactional. Customer experience, by contrast, is associated with warmth, empathy, and individual attention. The implicit assumption in many organizations is that you can optimize for one or the other, but not both at once.
publication: 2026-06-19 07:08:19
tags:
  - aiux
authors:
  - joel-sooriah
featured: true
redirects:
    - from: closing-the-gap-between-automation-goals-and-customer-experience-goals
---

Most organizations building chatbots or voice assistants frame their objectives around two goals: automation and customer experience. These goals are often treated as if they pull in opposite directions. Automation is associated with efficiency, cost reduction, and scale — qualities that read as cold and transactional. Customer experience, by contrast, is associated with warmth, empathy, and individual attention. The implicit assumption in many organizations is that you can optimize for one or the other, but not both at once.

This framing is largely a product of how conversational AI projects are managed rather than a reflection of any inherent trade-off. According to Hans van Dam, co-founder of the Conversation Design Institute (CDI), conversational AI is one of the few technologies capable of unifying these two goals — provided the underlying conversation is designed deliberately, rather than left to emerge as a byproduct of the technology stack.

## A framework for plotting automation against experience

CDI uses a two-axis model — automation on one axis, customer experience on the other — to describe where conversational AI initiatives typically land, based on benchmarking across the industry.

- **High automation, high CX (the target zone).** This is where hyper-automation coexists with a strong customer experience. It is described as difficult to reach and represents the intended outcome of a mature conversational AI program.
- **High automation, low CX ("squandering").** This is where many enterprise programs end up. The chatbot has broad scope — many use cases, many integrations — but the experience underneath it is poorly designed. Customers disengage or drop out of conversations, and the automation investment fails to convert into measurable value.
- **Low automation, high CX (novelty).** Programs in this zone often invest in surface-level polish — custom avatars, voice personas, visual flourishes — without a sound business case behind them. The experience may look impressive in a demo but doesn't move outcomes.
- **Low automation, moderate CX ("discovery").** This is the typical starting point: limited scope, a reasonable experience, and a defensible early-stage trajectory.

Industry benchmarking suggests most organizations start in discovery and then drift toward squandering rather than toward the target zone. The explanation given is structural: once an organization commits to a conversational AI initiative, scaling the underlying technology is comparatively fast. Scaling the design skill set required to support that technology at scale is slower. Budget tends to follow the path of least resistance — toward more integrations, more channels, more automated use cases — while the design discipline needed to keep those interactions usable lags behind. The result is a chatbot with wide functional coverage and a weak experience, which is the squandering outcome.

## Why the problem is structural: two different "brains" in conversation

The underlying difficulty is described as one of two distinct types of intelligence trying to communicate with each other. A conversational AI system is, functionally, an artificial system attempting to converse with a human brain. Each side of that interaction has different requirements.

On the system side, the technical task is understanding: interpreting intent, extracting relevant entities, and maintaining context across a conversation. This is the domain of natural language understanding and, increasingly, large language models.

On the human side, the requirement is different. People bring expectations shaped by how human conversation normally works — they look for acknowledgement, a degree of empathy, and signals that motivate them to continue engaging. This is the domain of natural language generation, and it is harder to get right than it might appear. Teams that are primarily engineering-led tend to invest heavily in the understanding side of the system, since that maps closely to their existing skill set, while underinvesting in the generation side — the part of the system responsible for how the conversation actually feels to the person on the other end. This asymmetry is a recurring source of poor customer experience even in systems that are technically capable.

## Conversational maturity develops in stages

CDI frames the development of a conversational AI system using a developmental analogy: a chatbot's capabilities and the design discipline required to support them grow together, in stages, much as a person develops from infancy to adulthood. Each stage corresponds to a different scope of interaction, and each requires different design patterns.

1. **Functional stage.** The system handles single-turn, transactional exchanges — answering a discrete question, completing a simple task. Design needs here are basic: clear acknowledgement that the system has understood the request.
2. **Transactional, multi-turn stage.** As interactions extend across multiple turns, the design focus shifts toward building trust. This includes consistent tone of voice, clear prompts at each step, and a degree of explainability and accountability in how the system behaves.
3. **Behavioral stage.** At this point, design begins incorporating behavioral psychology — managing user anxiety, sustaining motivation across longer interactions, and applying established behavioral models to the structure of the conversation.
4. **Mature stage.** The system supports visual design elements, custom voice personas, and a more fully developed, polished interaction — what is typically marketed as a "delightful" customer experience.

The central claim is that these stages cannot be skipped. An organization cannot deploy stage-four polish on top of a system that hasn't established stage-two trust fundamentals; the underlying design discipline has to be built sequentially, in step with the system's growing scope.

## The CDI workflow: strategize, design, build

CDI structures the development process into three phases.

**Strategize.** This phase defines what conversations the organization needs to have, with which audiences, and through what persona and tone of voice. It is a planning phase that precedes any writing of dialogue.

**Design.** This phase is broken into four steps:
- *Mentalize* the conversation — understand both the customer's and the system's perspective before writing anything.
- *Verbalize* the conversation — write the actual dialogue.
- *Make it inclusive* — ensure the conversation works across the range of users who will encounter it.
- *Elevate* the experience — apply more advanced techniques once the fundamentals are in place.

**Build.** This phase covers training, integration, and technical implementation of the system.

The sequencing matters: strategy and design happen before the technology is configured to deliver the conversation, not the other way around.

## Mentalizing the conversation: a planning step before writing dialogue

Before any dialogue is written, CDI recommends mapping the conversation from both perspectives using a structured canvas. This step is intended to surface assumptions that would otherwise go unexamined.

From the customer's side, the relevant questions include: Where is this person likely to be when they start the conversation? What is their actual goal? What underlying concern or hesitation might they have? A worked example used in the talk involves someone shopping for sneakers — their stated goal is finding the right pair, but their underlying worry is buying the wrong one and being embarrassed by the choice later.

From the system's side, the relevant questions include: What can the system actually do — recognize specific entities, check inventory, ask clarifying questions? What information does it need from the customer to complete the task?

The two sides typically enter the conversation with different expectations. Good design either meets those expectations or actively manages them when they can't be met. A significant share of chatbot failures are attributed to designers not being explicit about this mismatch before building the interaction.

## A foundational design pattern: acknowledgement, confirmation, prompt

One specific structural pattern is presented as a near-universal requirement for any conversational interface: a system response should acknowledge the input, confirm what was understood, and then issue a clear prompt for the next step.

An example: *"Okay [acknowledgement], you want to buy sneakers [confirmation], do you know which one? [prompt]."*

This sequence originated in voice interface design, where the order in which information is delivered is critical to comprehension, but it applies equally well to text-based chat. The acknowledgement signals that the system registered the input. The confirmation demonstrates that what the system understood is relevant to the user's actual request. The prompt — delivered last, once attention is established — carries the most important piece of information: what the system needs next.

## A specific anti-pattern: questions embedded mid-sentence

One rule is treated as close to absolute: a conversational system should never ask a question in the middle of a sentence, with additional information following afterward.

The reasoning draws on the cooperative principle in conversation: when a person is asked a question, they are conversationally inclined to answer it immediately. If a system asks a question and then continues talking before the person has a chance to respond, the interaction breaks down — the person's attention is misaligned with where the system expects the conversation to go next.

This pattern was observed directly when testing general-purpose LLM output against conversation design standards: models like ChatGPT were shown to violate this rule by default, embedding questions mid-sentence in generated dialogue. The explanation offered is that these models are not specifically trained on examples of well-designed conversational interactions, since well-designed conversational data is comparatively scarce relative to the broader corpus of text the models are trained on.

## Behavioral design: applying the Fogg Behavior Model

As conversational systems mature past the functional stage, design begins to draw on behavioral science — specifically BJ Fogg's behavior model, which holds that a given behavior occurs only when three elements are present at sufficient levels simultaneously:

- **Motivation** — the person's underlying desire to act.
- **Ability** — how easy or difficult the action is to perform.
- **Prompt** — the trigger that cues the action at the right moment.

The model implies a trade-off between motivation and ability: when an action is very easy, low motivation is sufficient to drive it; when motivation is high, people will tolerate more friction or difficulty. If any one of the three elements is absent, the behavior does not occur, regardless of the state of the other two.

This is illustrated with everyday examples — a phone ringing while someone's hands are dirty (prompt and motivation present, ability absent); a phone on silent during an incoming call from someone the person wants to talk to (motivation and ability present, prompt absent); a phone ringing with a caller the person doesn't want to speak to (prompt and ability present, motivation absent).

For conversation designers, the practical implication is that any friction point in a chatbot interaction can be diagnosed against these three categories, and addressed with specific copywriting and design techniques targeted at whichever element is missing.

## Applying behavioral techniques to a single message

The sneaker-shopping example is extended to show how multiple behavioral techniques can be layered into a single chatbot message:

- **Anticipatory enthusiasm** — describing or visualizing a successful outcome before the user has acted, comparable to airlines showing imagery of the destination before a flight is booked.
- **Expectation management** — explicitly stating what is about to happen (e.g., "three simple questions") so the user knows the scope of the interaction in advance.
- **Social proof** — signaling that the process is quick or low-effort for most people, which reduces perceived risk.
- **Personality and tone** — writing the message in a way that reads as human rather than generic or robotic.
- **Choice architecture** — deliberately designing the options or buttons presented to the user. Adding a low-commitment option (such as "maybe later") alongside more positive options increases the likelihood that the user selects a positive option overall, since the framing of available choices shapes behavior.

A single, well-designed message of this kind can contain roughly ten distinct design elements working together, when designed at an enterprise outcome-driven level. This stands in contrast to default outputs from general-purpose LLMs, which were shown to overuse exclamation points and question marks, producing copy that reads as generic marketing language rather than a designed conversational exchange.

## The role of expert oversight when using large language models

LLMs lower the barrier to producing chatbot dialogue quickly — a usable draft can be generated with minimal time investment. However, LLM output consistently requires expert review to meet the standard required for production use, particularly when a chatbot represents an established brand with an existing customer relationship built over years.

This raises a practical question for organizations adopting LLMs for conversational interfaces: speed of generation does not substitute for design rigor. Tightly constraining a general-purpose model's output to conform to specific conversational design patterns is one option, but if the constraints required are extensive, it may be worth questioning whether a general-purpose model is the right tool for that particular interaction in the first place.

## Quality assurance for conversational output

A recurring obstacle to message quality is the number of internal stakeholders involved in approving a single chatbot message — customer experience, marketing (tone of voice), the business (KPI targets), security (risk mitigation), and compliance. Each stakeholder optimizes for a different concern, and the cumulative effect of accommodating all of them often degrades the overall quality of the message.

CDI describes a tool built to address this: it scores a given message against established conversational design patterns and returns specific, actionable feedback — for example, flagging when a message ends on a question when it shouldn't, when acknowledgement is missing, or when language could be simplified. The tool produces a numerical score and can be used either as a standalone review step or integrated into workflows involving LLM-generated content, allowing teams to quantify improvements as messages are revised.

## How the conversation designer's role changes with LLMs

The underlying discipline of conversation design does not change when LLMs are introduced into the workflow — the same design patterns still need to be identified and applied. What changes is who is responsible for the literal writing of dialogue.

In legacy or vendor-based systems, conversation designers typically write dialogue directly into the platform. When an LLM generates the dialogue instead, the design patterns need to be encoded as instructions or constraints for the model to follow. This shifts the conversation designer's function from direct authorship toward quality assurance — reviewing and validating that LLM output meets the same design standards that would previously have been written in by hand.

## Organizational maturity: four dimensions that need to scale together

Beyond the design of individual conversations, CDI frames the broader organizational challenge of scaling a conversational AI program around four dimensions that need to develop in parallel:

- **Mindset** — the team's risk tolerance and attitude toward experimentation. Early-stage programs benefit from an adventurous mindset where it's safe to fail; as the program matures, this typically shifts toward a more conservative approach.
- **Skill set** — the level of design and engineering capability available to the team.
- **Culture** — whether departments with a stake in the conversational experience (compliance, marketing, support, engineering) share a common vocabulary and understanding of what good design looks like.
- **Systems** — the tools and technical infrastructure that support delivery.

A common failure pattern is described: organizations scale systems and technology quickly because that is the fastest lever available. If the skill set required to support that scale doesn't keep pace, the functional team responsible for the day-to-day work loses motivation, results decline, and the broader conversational culture across departments begins to erode. Stakeholders — product owners, managers — start reallocating attention to other initiatives, and the program stalls in the "squandering" quadrant described earlier: high automation scope, but a poorly supported customer experience.

The prescription is to invest in all four dimensions simultaneously rather than treating technology scaling as a substitute for design and organizational maturity.

## A practical checklist

The talk closes with a condensed set of heuristics intended for immediate, practical use when reviewing existing conversational interfaces:

- Pause and mentally run through the conversation before writing it.
- If a line of dialogue "sounds written" rather than spoken, rewrite it.
- Prefer active language over passive language.
- Prefer simple language and direct verbs over complex phrasing.
- Prioritize clarity over completeness of detail.
- Apply the acknowledgement–confirmation–prompt structure as a default pattern.
- Apply a "one breath" test: if a line cannot be spoken comfortably in a single breath, it is too long.

These checks are presented as a starting point for auditing existing chatbot deployments, with the expectation that most organizations, on review, will find gaps between current output and these standards.

---
type: post
title: Why Your Best Growth Opportunity Isn't Asking for Anything
description: Most roadmaps are built on a structurally flawed input - the customers who engage most actively in discovery are rarely the customers who represent the largest growth opportunity nor the one your organization need at a specific point in time. They are also potentially vocal, articulate, and easy to build a business case around. They are, more often than not, a minority of the addressable market — and the energy spent serving their sophistication is energy not spent on the segment that would actually move the revenue needle. This is the minority segment problem. It doesn't show up in your funnel metrics your NPS or your win/loss analysis. It shows up when a competitor enters with a simpler product captures a segment you never knew you were ignoring and grows faster than your roadmap can respond.
publication: 2026-06-05 19:55:34
tags: odi strategy
authors:
  - joel-sooriah
featured: false
redirects:
    - from: why-your-best-growth-opportunity-isnt-asking-for-anything
---

# Segment Smarter: Why Your Best Growth Opportunity Isn't Asking for Anything

Most roadmaps are built on a structurally flawed input: the customers who engage most actively in discovery are rarely the customers who represent the largest growth opportunity. They are vocal, articulate, and easy to build a business case around. They are also, more often than not, a minority of the addressable market — and the energy spent serving their sophistication is energy not spent on the segment that would actually move the revenue needle.

This is the minority segment problem. It doesn't show up in your funnel metrics, your NPS, or your win/loss analysis. It shows up when a competitor enters with a simpler product, captures a segment you never knew you were ignoring, and grows faster than your roadmap can respond.

Outcome-Driven Innovation is the methodology that makes this problem visible before it becomes a competitive threat. What follows is a case study in exactly that — and in what happens when the data forces you to redirect a significant engineering investment toward a market you weren't selling to.

---

## How we got here

We were running a restaurant online booking platform with a clear growth mandate. The strategic question was straightforward: what's the next capability that extends our value to operators and increases platform stickiness? The answer that came back from discovery was table management — a digital floor plan editor allowing operators to assign tables, track covers, and handle walk-ins alongside online reservations.

The business case checked out. Customers were asking for it, the competitive gap was real, and engineering scoped the work at several sprints of meaningful effort. Executive sign-off came quickly. The roadmap was set.

What the business case didn't surface — because standard discovery processes aren't designed to surface it — was the representativeness problem. The operators driving the table management ask were fine dining establishments, multi-room venues, and event spaces: restaurants where floor layout is a genuinely managed asset, where a booking for four at a round table is operationally distinct from a booking for four at a booth. They were engaged, requirements-literate, and easy to build a narrative around.

They were also not the majority of the market. And the segment that was — larger, less vocal, and completely underserved — was waiting for something entirely different.

---

## Applying ODI: starting with the job, not the customer

Outcome-Driven Innovation, as Tony Ulwick has articulated it since the 1990s, inverts the typical product development sequence. Rather than starting with customer segments and asking what they want, it starts with the *job to be done* — the underlying goal a person or business is trying to accomplish — and then identifies the desired outcomes customers use to measure success at that job.

The insight is deceptively simple: customers don't buy products. They hire products to get a job done. And crucially, the same job can be performed by very different products in very different ways.

What makes ODI operationally useful is that it forces you to capture outcomes in the customer's own measurement language — not as feature requests or pain points, but as the specific metrics they use to judge success. In his conversation with Melissa Perri on the *Product Thinking* podcast (Episode 207), Ulwick illustrates this with an everyday example: *"As you're preparing a meal you think about things like, maybe you overcooked the meal — I'd really like to minimize the likelihood of overcooking the meal. Minimize the time it takes to prep the food. Minimize the likelihood of creating the wrong portions."*

These aren't preferences. They're measurable criteria for job success. And they're precisely the kind of statements that, when mapped across a market, reveal where products are failing people — not just failing to delight them.

In our case, the job we were initially designing around was: *manage the occupancy of my dining room across the service period*. That's a real job. Table management systems are a legitimate solution to it. But when we ran an ODI process — mapping outcomes, not features — we discovered something very interesting and somehow ... uncomfortable.

The highest-importance, lowest-satisfaction outcomes in our data weren't about floor plan management at all. They clustered around a different, simpler job:

**Fill my available seats as quickly as possible.**

This sounds like a subset of the first job. It isn't. It's a different job, held by a different segment of operators, with completely different success criteria.

---

## The brasserie segment: a market you don't see on a demographic map

Traditional market segmentation is demographic and firmographic: restaurant size, cuisine type, number of covers, city vs. regional, independent vs. chain. These are useful categories for sales and marketing. They are almost useless for product design.

When we segmented by job and by the outcomes operators used to measure success, a distinct cluster emerged: **brasseries**.

Not brasseries as a cuisine category, but brasseries as an *operating model*. High turnover, continuous service, walk-in culture, a floor that's rarely at planned capacity for more than a few hours a day. For these operators, the question was never "which table should I assign this reservation to?" The question was: "I have three tables free right now — how do I get people into them in the next fifteen minutes?"

Their desired outcomes, ranked by importance and satisfaction:

- *Minimize the time between a table becoming free and a new party being seated*
- *Reduce the effort required to communicate current availability to prospective customers*
- *Eliminate the gap between actual availability and displayed availability across booking channels*

Notice the structure of each statement: a direction (minimize), a metric (time, effort, gap), and a context (between table turnover and seating, across booking channels). This is not accidental. Ulwick describes the precise syntax in the podcast: *"It contains four pieces or elements. One is a direction of improvement — which is always minimize. The second is a metric, either time or likelihood. The third is the object of control. And the last part is a contextual clarifier if it's needed."* He adds that this structure was battle-tested across 45 projects with Microsoft to find the format that yields the best insights and the least survey fatigue.

The brasserie outcomes above follow that syntax exactly. And that precision matters: outcome statements written in this format can be surveyed, ranked by importance and satisfaction, and fed directly into opportunity scoring — which is what made the segment visible in the first place. A vague pain point like "I need something simpler" produces no signal. A well-formed outcome statement produces a data point.

None of these outcomes map to a table management system. They map to something much simpler: **a real-time available seats signal**, surfaced immediately to the customer-facing booking interface.

Show me what's free right now. Let me book it in one tap. Done.

---

## The engineering inversion

This is where ODI produces its most useful — and most uncomfortable — output.

The table management system we were building would have served the fine dining / managed floor segment well. But it would have been irrelevant to the brasserie segment, and worse, it would have made our product feel *heavier* than they needed it to be. A drag-and-drop floor editor is not a feature for an operator who doesn't think in terms of floor plans. It's friction.

The real-time availability signal — the thing that would have genuinely served the brasserie segment — was a fraction of the engineering investment. A seats-available counter, updated in near real-time, displayed prominently in the booking flow. No floor plan model. No table assignment logic. No concurrent session handling.

Ulwick makes this tradeoff precise in the podcast: *"What are the chances of you randomly coming up with a solution that addresses the top 15 unmet needs in the market if you don't know what they are? It's zero. But what are the chances if you know exactly what those 15 unmet needs are in priority order? About 86 percent — because now you're just relying on your team to use their creativity to come up with solutions that address the needs you know exist."*

This is the exact inversion we experienced. The table management system was a creative solution in search of the right problem. The availability signal was a direct answer to a known, measurable, underserved need. One was built from a vocal minority's feature requests. The other came from outcome data. The engineering effort wasn't even comparable — and neither was the market opportunity.

The opportunity cost math was stark:

- **Table management system**: high engineering effort, serves a segment that's real but represents a minority of the addressable market, and is already partially served by legacy POS systems with floor management modules.
- **Immediate availability signal**: low engineering effort, serves a segment that's large (brasseries are a dominant format in many urban markets), largely underserved by existing booking tools, and has high willingness to convert because the job is urgent by definition.

The segment that was asking loudest was not the segment with the most opportunity. This is one of the most consistent findings in ODI work, and it's one that standard agile processes — which amplify the voice of whoever shows up to user research — are structurally bad at catching.

---

## What ODI actually did here

It's worth being precise about the methodology, because "talk to customers about outcomes" sounds generic in a way that undersells what's actually happening.

ODI requires you to:

**1. Define the core functional job** at the right level of abstraction — not too specific (don't anchor on solutions), not too broad (don't lose actionability). "Manage my dining room" is a solution-adjacent framing. "Ensure my dining capacity generates maximum revenue per service period" is the functional job.

**2. Collect desired outcomes as measurement statements** — not features, not pain points, but the criteria by which the operator would judge success or failure at the job. The syntax, as described above, is: direction of improvement + metric + object of control + contextual clarifier. "Minimize the time required to match available seating with nearby booking intent" is an outcome. "I need a better availability display" is a solution request dressed up as an insight.

**3. Measure importance and satisfaction for each outcome** across a representative sample. This is where the work is. It requires reaching beyond your engaged customer base to the operators who *aren't* talking to you — who haven't complained because the product hasn't touched their job yet.

**4. Identify opportunity scores** — the combination of high importance and low satisfaction. These are your underserved outcomes. They point directly at where a product can create disproportionate value.

**5. Segment by outcome, not by demographics.** Group customers by which outcomes they prioritize, not by what industry analysts would put them in. Ulwick describes this step in the podcast through the Bosch circular saw case: *"When we looked at the broad market, it looked like there were no opportunities. But when we segmented the market, we found a third of the population that had 14 unmet needs. They were more finished carpenters, they had to make more angle cuts, blade height adjustments — 14 unmet needs that nobody else had. So that became their target."* The conclusion he draws is blunt: *"If you build for the average, you're targeting nobody, usually ineffectively."*

The parallel with our brasserie segment is direct. In aggregate, the booking platform market looked like it needed table management — that's what the loudest operators were asking for. But when we segmented by unmet outcomes, a third of the market turned out to be a cluster of operators with a completely different job, 14 unmet outcomes of their own, and no solution addressing any of them. They were the finished carpenters of the restaurant world. We just hadn't looked for them yet.

---

## The business outcome

The segment discovery wasn't just a product insight — it was a go-to-market insight.

Brasseries are, in many urban markets, one of the most numerous restaurant formats. They're also systematically underserved by booking tools designed around the fine dining mental model of pre-assigned tables, advance reservations, and managed floor plans. They'd been reluctant adopters of booking platforms not because they didn't value them, but because existing platforms solved the wrong job.

A product built around immediate availability — not around table management — becomes the category leader for a segment that's large, underserved, and has a clear, urgent job to be done. The sales motion is also different: you're not selling productivity software to a floor manager, you're selling "more covers tonight" to an owner. That's a faster sales cycle and a more compelling ROI story.

The business outcome wasn't just "we built the right feature." It was "we found a segment we weren't selling to, built something lightweight that served their job better than anything else on the market, and unlocked a channel we'd been systematically ignoring."

---

## The broader lesson

Every product team has a version of the table management trap. It usually looks like:

- A loud, articulate segment of users asking for sophistication
- An engineering investment that's technically interesting and defensible
- A backlog shaped by the people who show up, not by the full job landscape

ODI doesn't tell you to ignore the sophisticated users. It tells you to measure, rigorously, where importance and satisfaction diverge across the full range of outcomes your market cares about — and then to let that measurement, not advocacy volume, drive prioritization.

The brasserie segment never asked for a real-time availability signal. They didn't have the language for it. What they said was "I need something simple" or "your product isn't really for me." Those are not product requirements. But when you map their desired outcomes, you find a cluster of high-importance, deeply-unmet needs that resolve to exactly one thing: show me what's free right now.

That's the table you never built. And in most markets, it's the one that would have filled fastest.

---

*This article is part of a series on Outcome-Driven Innovation and Jobs-to-be-Done in product development practice. The framework references Tony Ulwick's ODI methodology as developed at Strategyn. All direct quotes are from [Product Thinking, Episode 207 — "Mastering Predictable Product Success with the ODI Strategy"](https://open.spotify.com/episode/75o99vSLHEr6F8yrQoJVDz), hosted by Melissa Perri (January 2025). The examples in this article draw on real product work with details changed for confidentiality.*

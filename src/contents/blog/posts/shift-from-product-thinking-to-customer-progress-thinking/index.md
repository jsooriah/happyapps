---
type: post
title: Shift from product thinking to customer progress thinking
description: Every product manager has sat through a roadmap prioritization meeting that devolves into chaos. Engineering wants to pay down technical debt. Sales wants features that will close their current deals. Customer success wants fixes for the loudest complaints. Leadership wants innovation that moves metrics. Everyone's arguing about what to build. Nobody's asking why any of it matters.
This is the natural endpoint of **product thinking**—a mode of operating where the product itself becomes the center of gravity. Features become the unit of value. Roadmaps become lists of things to ship. Success becomes adoption metrics. Product thinking feels productive because there's always something to build, something to measure, something to optimize. But it's fundamentally disconnected from the reason products exist in the first place. This is what Jobs-to-be-Done forces you to confront, customers don't want your product. They want progress. Your product is just a means to that end.
publication: 2025-03-18 11:27:12
tags:
  - jtbd
authors:
  - joel-sooriah
featured: true
redirects:
    - from: shift-from-product-thinking-to-customer-progress-thinking
---

Every product manager has sat through a roadmap prioritization meeting that devolves into chaos. Engineering wants to pay down technical debt. Sales wants features that will close their current deals. Customer success wants fixes for the loudest complaints. Leadership wants innovation that moves metrics.

Everyone's arguing about what to build. Nobody's asking why any of it matters.

This is the natural endpoint of **product thinking**—a mode of operating where the product itself becomes the center of gravity. Features become the unit of value. Roadmaps become lists of things to ship. Success becomes adoption metrics.

Product thinking feels productive because there's always something to build, something to measure, something to optimize. But it's fundamentally disconnected from the reason products exist in the first place: **to help customers make progress in their lives**.

This is what Jobs-to-be-Done forces you to confront: customers don't want your product. They want progress. Your product is just a means to that end.

## **The Uncomfortable Truth: Customers Don't Care About Your Product**

When I ran trust & safety teams, I never woke up thinking "I wish I had better moderation software." I woke up thinking:

- "I need to prevent something terrible from happening on my platform today"

- "I need to show leadership we're controlling abuse without killing engagement"

- "I need my team to make consistent decisions even though our policies are ambiguous"

The software I used—case management systems, automation tools, analytics dashboards—was completely invisible to me except when it got in the way.

I didn't hire software to "have features." I hired software to make progress against problems that kept me up at night.

This distinction sounds obvious. Of course customers want outcomes, not features. But watch what happens when product teams plan:

**Product thinking asks**: "What features should we build next?"

**Progress thinking asks**: "What progress are customers unable to make, and why?"

**Product thinking asks**: "How do we increase feature adoption?"

**Progress thinking asks**: "What job are customers trying to do when they don't use this feature?"

**Product thinking asks**: "What do customers want?"

**Progress thinking asks**: "What situation creates demand for progress, and what forces shape how customers seek it?"

These aren't just different phrasings. They're fundamentally different ways of understanding what you're building and why.


## **What Is a "Job" and Why Most Teams Get It Wrong**

Clayton Christensen, who popularized Jobs-to-be-Done theory, defined a job as:

"The progress that a person is trying to make in a particular circumstance."

Let me break down why each word matters:

**Progress** = Movement from a current state to a better state. Not activity. Not features. Movement toward a goal.

**Person** = An individual in a specific role, not a persona or segment. Sarah the senior moderator has different jobs than Sarah the team lead, even though she's the same person.

**Trying to make** = Active effort against resistance. There's struggle. There are obstacles. The job exists because progress isn't automatic.

**Particular circumstance** = Context determines the job. The same person can have completely different jobs in different situations.

Most teams completely miss the "particular circumstance" part. They ask customers "what do you need?" as if needs exist in a vacuum. But jobs only exist in context.

Here's what this looks like in practice:

**Wrong**: "Moderators need better tools to handle high volumes."

**Right**: "When moderators are reviewing their 50th case of the day and their judgment is degrading from fatigue, they need to maintain decision quality without slowing down—because missing violations risks platform safety, but going too slow creates backlog that leadership blames them for."

The first statement could justify almost any feature. The second statement exposes the actual job: **maintaining decision quality under cognitive load while managing competing performance pressures**.

The solution isn't "better tools for high volume." The solution might be:

- Intelligent case batching that varies difficulty to manage cognitive load

- Real-time decision confidence scoring that flags when fatigue is affecting judgment

- Automatic break scheduling based on decision quality degradation

- Team-based workflows that distribute high-stakes decisions across fresh reviewers

Completely different product. Same "need" if you ask superficially.


## **The Anatomy of a Job: It's Not What You Think**

Jobs-to-be-Done isn't just a different way to phrase customer needs. It's a completely different model of what creates demand and shapes behavior.

A job has distinct components that most product teams never identify:


### **1. The Struggling Moment**

This is the circumstance that creates demand. Something isn't working. Progress is blocked. The status quo has become intolerable.

**Gherkin translation**:

gherkin

Given \[the specific context that creates struggle]

When \[the trigger that makes the struggle acute]

Then \[the progress becomes urgent]

**Example from content moderation**:

gherkin

Given a moderator reviewing borderline content without clear policy guidance

When their manager questions a recent decision they made

Then they urgently need defensible rationale for judgment calls

The struggling moment isn't "reviewing content" or "needing policies." It's **being questioned and lacking defensibility**. That's what makes progress urgent.


### **2. The Desired Outcome**

This is the progress the customer is trying to make. Not features. Not activities. The change in state they're seeking.

Outcomes have a specific structure in JTBD (we'll dive deeper when we cover Ulwick's framework):

- **Direction**: Minimize, maximize, increase, decrease

- **Unit of measure**: Time, cost, effort, quality, likelihood, risk

- **Object of control**: What specifically is being measured

- **Contextual qualifier**: Under what conditions

**Gherkin translation**:

gherkin

Then \[direction] \[measure] of \[object] in \[context]

**Example**:

gherkin

Then minimize the time to generate defensible rationale for judgment calls

And maximize confidence that the rationale will withstand manager scrutiny


### **3. The Constraints**

These are the real-world limitations that shape how customers can seek progress.

**Gherkin translation**:

gherkin

And \[must/must not] \[constraint]

**Example**:

gherkin

And must not slow down case review throughput

And must not require legal expertise the moderator doesn't have

And must work within existing moderation tools without switching contexts


### **4. The Forces of Progress**

This is where JTBD gets really powerful. Bob Moesta and Chris Spiek (we'll cover Moesta's student Boehme's framework later) identified four forces that shape whether customers make progress:

**Push** = Problems with the current solution that create motivation to change

**Pull** = Attraction to a new solution that promises better progress

**Anxiety** = Fears about whether the new solution will actually work

**Habit** = Inertia of the current way of doing things

**Gherkin translation**:

gherkin

Given \[current solution with problems] (push)

When \[new solution promises better progress] (pull)

Then \[must overcome fear of whether it will work] (anxiety)

And \[must overcome inertia of current habits] (habit)

**Example**:

gherkin

Given moderators currently write manual justifications that take 5+ minutes per case (push)

When an AI system promises to auto-generate defensible rationale in seconds (pull)

Then moderators must overcome fear that AI rationale won't actually protect them under scrutiny (anxiety)

And must overcome the habit of writing their own notes in their own words (habit)

Understanding these forces completely changes product strategy. You don't just build features that pull customers in. You also have to reduce anxiety and address habits. We'll dive much deeper into this when we cover Boehme's Wheel of Progress.


## **Why "Hire" Is the Perfect Metaphor**

Christensen used the metaphor of "hiring" deliberately. When you hire someone for a job, you:

- Have a specific task that needs doing

- Evaluate candidates based on their ability to do that task

- Fire them if they don't perform

- Might hire multiple people for different jobs

Customers do exactly this with products:

**They hire for specific circumstances**: I don't hire a milkshake in general. I hire a milkshake for the morning commute job of keeping me full and alert until lunch. I hire a different solution (coffee? protein bar?) for the afternoon energy job.

**They evaluate based on job performance**: Features don't matter except as indicators of job performance. I don't care if the milkshake is "premium" or "artisanal." I care if it's thick enough to last my commute and convenient enough to drink while driving.

**They fire products that don't perform**: If the milkshake doesn't keep me full, I fire it and hire something else—even if the milkshake is objectively delicious.

**They hire multiple products for different jobs**: I might hire one tool for rapid case review and a different tool for complex investigations, even if both are "moderation platforms."

This completely reframes product strategy:

**Product thinking asks**: "How do we get customers to choose our product?"

**Progress thinking asks**: "What jobs are customers hiring solutions for, and why would they hire us instead of alternatives?"

The second question exposes a critical insight: **you're not competing against other products in your category. You're competing against every alternative way customers might make progress.**


## **The Competition You're Not Seeing**

When we built our content moderation platform, we thought we were competing against other moderation software vendors. We spent time analyzing their features, pricing, positioning.

Then we did actual JTBD research. We discovered our real competition was:

**For the job of "making defensible decisions under ambiguity"**:

- Excel spreadsheets where moderators track their own precedents

- Slack channels where they ask colleagues for advice

- Printed policy guides with highlighting and personal notes

- Their own memory and intuition

- Not making a decision at all (escalating everything)

**For the job of "showing leadership we're controlling abuse"**:

- Manual weekly reports compiled in Google Docs

- Slack updates with cherry-picked examples

- Screenshots of individual successful enforcements

- Verbal updates in 1-on-1s

**For the job of "handling volume without burning out"**:

- Team rituals and mutual support

- Taking mental health days

- Rotating case types

- Quitting and finding a less stressful job

We weren't just competing with Spectrum, Hive, or other moderation platforms. We were competing with **the entire ecosystem of workarounds, non-consumption, and alternative approaches customers had already hired for these jobs**.

Understanding this changed everything:

**Product thinking approach**: "Our platform is better than competitors because we have advanced ML and better analytics."

**Progress thinking approach**: "Moderators currently hire manual spreadsheets and Slack channels for the judgment call job because these solutions feel personal, trusted, and defensible even if inefficient. Our system needs to be more defensible than spreadsheets and more personal than algorithms—or it won't get hired at all."


## **The Three Types of Jobs (And Why You Need All Three)**

Tony Ulwick, who we'll cover in depth in Part 5, breaks jobs into three categories:


### **Functional Jobs**

The practical, objective task to accomplish.

**Example**: Process 100 moderation cases per hour without errors.

**Gherkin**:

gherkin

Given a queue of 100 cases requiring review

When a moderator works through the queue

Then all cases should be reviewed within 1 hour

And decision accuracy should exceed 95%


### **Emotional Jobs**

The way customers want to feel (or not feel).

**Example**: Feel confident in decisions, not anxious about mistakes.

**Gherkin**:

gherkin

Given a moderator makes a judgment call on borderline content

When they submit their decision

Then they should feel confident it will withstand scrutiny

And should not feel anxious about being second-guessed


### **Social Jobs**

How customers want to be perceived by others.

**Example**: Be seen as competent by leadership, protective by users, fair by creators.

**Gherkin**:

gherkin

Given a moderator's decision is reviewed by leadership

When leadership evaluates the moderator's judgment

Then the moderator should be perceived as thoughtful and competent

And should not be perceived as either overly harsh or negligently permissive

Here's what most product teams miss: **emotional and social jobs often matter more than functional jobs**.

Your moderation platform might be functionally superior—faster, more accurate, better ML. But if using it makes moderators feel like they're outsourcing their judgment to an algorithm (emotional job failure) or makes leadership perceive them as over-reliant on automation (social job failure), **it won't get hired**.

This is why "better features" often don't drive adoption. You're solving functional jobs while ignoring emotional and social jobs.


## **How to Think in Jobs: The Mental Model Shift**

Shifting from product thinking to progress thinking requires rewiring your instincts. Here's the mental model:


### **Product Thinking Flow:**

1. Identify customer segment

2. Discover their needs

3. Build features that address needs

4. Measure feature adoption

5. Iterate based on usage


### **Progress Thinking Flow:**

1. Identify struggling moments in specific circumstances

2. Understand what progress customers are trying to make

3. Diagnose what's preventing that progress (forces)

4. Build solutions that enable progress better than alternatives

5. Measure progress made, not features used

The key difference: **Product thinking starts with customers as groups with needs. Progress thinking starts with struggling moments that create demand.**

Let me make this concrete with a real example from my work:

**Product thinking approach to moderation tools**:

Segment: Trust & Safety teams at social platforms Need: Better tools to handle growing content volume Feature: Automated content classification Metric: Percentage of cases auto-classified Iteration: Improve classification accuracy

**Progress thinking approach to the same problem**:

Struggling moment: Moderators drowning in volume during viral events, falling behind on case reviews, facing leadership criticism for backlogs Progress desired: Maintain decision quality and platform safety even when volume spikes 10x Forces:

- Push: Manual review can't scale, backlogs create risk

- Pull: Automation promises to handle volume

- Anxiety: Automation might make errors on culturally nuanced content

- Habit: Moderators trust their judgment more than algorithms

Solution: Not just automation, but:

- AI-assisted triage that routes clear cases to auto-action and ambiguous cases to human review

- Real-time confidence scoring that shows moderators which automated decisions to audit

- Easy override system that lets moderators correct AI without friction

- Learning loop that uses moderator corrections to improve AI over time

Metric: Percentage of viral event volume handled without backlog while maintaining decision accuracy

See the difference? Product thinking led us to build automation and measure accuracy. Progress thinking led us to build a **collaborative system that addresses both the functional job (handle volume) and the emotional jobs (maintain confidence, avoid errors) and the social jobs (be seen as maintaining quality standards)**.


## **The Diagnostic Questions That Shift Your Thinking**

Here are the questions that force you out of product thinking and into progress thinking:

Instead of: **"What features do customers want?"**

Ask: **"What progress are customers unable to make right now?"**

**Gherkin diagnostic**:

gherkin

Given \[customer's current state]

When \[they try to make progress]

Then \[what goes wrong or what's inadequate]

***

Instead of: **"How is our product better than competitors?"**

Ask: **"What jobs are customers hiring solutions for, and what alternatives are they currently using?"**

**Gherkin diagnostic**:

gherkin

Given \[customer needs to make specific progress]

When \[they evaluate options]

Then \[what are they currently hiring, including non-consumption]

And \[why would they switch to us vs. stick with current solution]

***

Instead of: **"Why aren't customers adopting this feature?"**

Ask: **"What job did we think this feature solved, and what jobs are customers actually trying to do?"**

**Gherkin diagnostic**:

gherkin

Given \[the feature we built]

When \[customers encounter the struggling moment it's meant to address]

Then \[are they actually hiring our feature, or something else]

And \[if something else, what jobs does that alternative solve better]

***

Instead of: **"What would make customers choose us?"**

Ask: **"What forces would cause customers to switch from their current solution to ours, and what forces prevent switching?"**

**Gherkin diagnostic**:

gherkin

Given \[customer's current solution with specific problems] (push)

When \[our solution promises better progress] (pull)

Then \[what anxieties prevent them from switching]

And \[what habits make the current solution comfortable despite problems]


## **A Practical Example: Reframing a Common Product Decision**

Let's take a real roadmap debate and see how progress thinking changes it:

**Scenario**: Your engineering team wants to rebuild the tech stack. Sales wants integration with Salesforce. Customer success wants better error messages. Product wants a new analytics dashboard.

**Product thinking approach**: Prioritize based on who argues loudest, which initiative affects more users, or which will move the North Star metric.

**Progress thinking approach**: Map each request to the struggling moments and jobs they're trying to address.

**Engineering's tech stack rebuild**:

gherkin

Given our current stack has tech debt that slows development

When we try to ship new features quickly

Then deployment complexity and fragility create delays

And engineers feel frustrated by maintenance burden instead of building value

**Job**: Maintain development velocity and team morale

**Sales's Salesforce integration**:

gherkin

Given sales reps manage prospects across multiple tools

When they try to track which prospects are using the product

Then they have to manually check the product and update Salesforce

And they lose deals because they can't respond quickly to product usage signals

**Job**: Act on buying signals without manual tool-switching

**Customer success's error messages**:

gherkin

Given customers encounter errors but don't understand what went wrong

When they contact support for help

Then support has to diagnose the problem from vague descriptions

And resolution time creates customer frustration and support ticket volume

**Job**: Resolve problems independently without waiting for support

**Product's analytics dashboard**:

gherkin

Given product needs to understand feature usage patterns

When they try to make data-driven roadmap decisions

Then they have to request custom queries from engineering

And the time lag means decisions are based on stale data

**Job**: Make roadmap decisions with current, accurate usage data

Now the prioritization conversation changes completely:

"Which jobs are most critical to customer progress right now? Which struggling moments are most acute? Which solutions enable the most valuable progress?"

Not: "Which team argues loudest?"

You might discover:

- Customer success's error messages solve the most acute customer pain (frustrated customers churning)

- Sales's Salesforce integration solves a high-value job (converting more deals)

- Product's analytics enable better decisions on all future work (force multiplier)

- Engineering's tech stack, while important, doesn't directly solve customer jobs (deprioritize unless it's blocking the other three)

**Or** you might discover the opposite—that tech debt is actually preventing you from solving any customer jobs effectively.

The point isn't which answer is right. The point is that **progress thinking gives you a framework for making the call based on customer jobs rather than internal politics**.


## **The Hardest Part: Recognizing When You're Not Thinking in Jobs**

The biggest challenge with shifting to progress thinking isn't learning the framework. It's catching yourself when you slip back into product thinking.

Here are the telltale signs you're in product mode instead of progress mode:

**Sign 1: You're talking about features more than outcomes**

Product thinking: "We should add bulk actions to the moderation queue."

Progress thinking: "Moderators need to process similar violations quickly without repetitive work."

**Sign 2: You're comparing features to competitors instead of understanding why customers hire alternatives**

Product thinking: "Competitor X has this feature, so we need it too."

Progress thinking: "What job are customers hiring Competitor X to do, and what alternatives (including non-consumption) are they evaluating?"

**Sign 3: You're measuring usage instead of progress**

Product thinking: "Feature X has 40% adoption."

Progress thinking: "What percentage of customers who have the struggling moment this feature addresses are making the desired progress?"

**Sign 4: You're frustrated that customers "don't understand" your product**

Product thinking: "Customers don't appreciate how powerful our automation is."

Progress thinking: "What job are customers trying to do, and why isn't automation the solution they're hiring for it?"

**Sign 5: You're building for personas instead of circumstances**

Product thinking: "Sarah, the senior moderator, needs advanced filtering."

Progress thinking: "When moderators face high-stakes decisions under time pressure, they need confidence without complexity."


## **Making the Shift Permanent**

Shifting from product thinking to progress thinking isn't a one-time decision. It's a discipline you have to practice until it becomes instinct.

Here's how to build that discipline:


### **1. Rewrite your customer research questions**

**Before every interview, translate product questions into progress questions**:

❌ "What features would you like to see?" ✅ "Tell me about a recent time you struggled to make progress. What were you trying to accomplish? What got in the way?"

❌ "How do you use our product?" ✅ "Walk me through the last time you had \[specific struggling moment]. What did you do? What did you hire to help you make progress?"

❌ "What do you think of this design?" ✅ "The last time you tried to \[specific job], what solution did you use? What made you choose that over alternatives? What would make you switch?"


### **2. Reframe your product requirements in Gherkin**

Every user story should be traceable to a job:

gherkin

Job-level (customer progress):

Given moderators make judgment calls on ambiguous content

When they submit their decision

Then they need defensible rationale that protects them from second-guessing

Solution-level (product requirement):

Given a moderator submits an enforcement action on borderline content

When the action is not directly linked to a policy violation

Then the system should prompt for contextual factors that informed the decision

And auto-generate a defensible rationale based on those factors

Implementation-level (acceptance criteria):

Given a case with no direct policy violation match

When moderator selects action\_type and clicks submit

Then display context\_selection modal

And generate rationale\_text from template

And store in case\_history with timestamp


### **3. Challenge every feature request with "what job does this solve?"**

Make it a team ritual. When anyone proposes a feature, the first question is always: "What struggling moment creates demand for this? What progress are customers trying to make?"

If you can't articulate the job, you don't build the feature.


### **4. Measure progress, not usage**

Track:

- Percentage of customers who have the struggling moment

- Percentage of those customers who successfully make the desired progress

- Time from struggling moment to progress achieved

- Customer effort required to make progress

- Forces that prevent or enable progress

Not just:

- Feature adoption rate

- Daily active users

- Time in product


### **5. Make forces visible in your roadmap discussions**

Every roadmap item should document:

- Push: What's wrong with current solutions?

- Pull: What progress does our solution enable?

- Anxiety: What fears prevent adoption?

- Habit: What inertia keeps customers with current solutions?


## **What Changes When You Think in Progress**

When you truly shift from product thinking to progress thinking, everything changes:

**Your roadmap** stops being a list of features and becomes a sequence of struggling moments you're addressing.

**Your metrics** stop being about usage and become about customer progress achieved.

**Your competitive analysis** stops being about feature comparison and becomes about understanding what alternatives customers hire for different jobs.

**Your positioning** stops being about what you do and becomes about what progress you enable.

**Your sales process** stops being about demo'ing features and becomes about diagnosing struggling moments and showing how you enable progress better than alternatives.

**Your customer conversations** stop being about gathering feature requests and become about understanding the circumstances that create demand.

But here's what doesn't change: **you still need to build great products**. Progress thinking doesn't mean features don't matter. It means features only matter insofar as they enable progress better than alternatives.

The difference is that now you know **which features to build, why they matter, and how to know if they're working**.


## Voices from the Field

The shift from product thinking to customer progress thinking finds strong echoes across recent practitioner conversations—leaders who, often without invoking JTBD by name, describe the same reorientation toward understanding what customers are actually trying to accomplish.

**Jeanne DeWitt Grosser** ([Lenny's Podcast, 2025](https://www.youtube.com/watch?v=RmnWHz8HD74)) — Her observation about enterprise buying behavior is a near-perfect validation of the "struggling moment" concept at the heart of JTBD. "80% of customers buy to avoid pain or reduce risk as opposed to increased upside, which is a good thing for startup founders to understand. We all love to talk about the art of the possible, everything we're going to enable in the future, but that's often really a sale that's going to resonate with another founder. For everybody else, particularly enterprises, you're avoiding the risk of not making your revenue target next quarter." This reinforces the article's core argument: customers don't hire products for features—they hire them to escape a struggling moment. If your roadmap is built around aspirational capabilities rather than the specific anxieties keeping buyers awake, you're building for a customer that doesn't exist.

<a class="yt-card" href="https://www.youtube.com/watch?v=RmnWHz8HD74" target="_blank" rel="noopener"><img src="https://img.youtube.com/vi/RmnWHz8HD74/hqdefault.jpg" alt="What world-class GTM looks like in 2026 — Jeanne DeWitt Grosser"><span>What world-class GTM looks like in 2026 — Jeanne DeWitt Grosser</span></a>

**Stewart Butterfield** ([Lenny's Podcast, 2025](https://www.youtube.com/watch?v=kLe-zy5r0Mk)) — The Slack founder offers a masterclass in distinguishing real value creation from feature shipping. "At more than one company all hands, I made everyone in the company repeat this as a chant: In the long run, the measure of our success will be the amount of value that we create for customers… there's no substitute for actually having created it." Butterfield also challenges the friction-removal instinct that dominates product thinking: "It became an assumption that it should always be trying to remove friction when the challenge is really comprehension." This is a powerful complement to the article's point about misframing jobs—teams optimize for surface-level ease when the actual job might be about helping users understand and make confident decisions.

<a class="yt-card" href="https://www.youtube.com/watch?v=kLe-zy5r0Mk" target="_blank" rel="noopener"><img src="https://img.youtube.com/vi/kLe-zy5r0Mk/hqdefault.jpg" alt="Mental models for building products people love — Stewart Butterfield"><span>Mental models for building products people love — Stewart Butterfield</span></a>

**Lazar Jovanovic** ([Lenny's Podcast, 2026](https://www.youtube.com/watch?v=0XNkUdzxiZI)) — The professional vibe coder's Aladdin-and-the-Genie analogy maps surprisingly well onto the gap between product thinking and progress thinking. "You rub the lamp, a genie comes out… The first wish is, 'I want to be taller.' Genie makes me 13 feet tall because I was not specific. AI just don't understand what do you mean when you say, 'You know what I mean?'" The same is true of product teams: when you ask customers "what do you need?" without specifying the circumstance, you get the equivalent of "I want to be taller"—a superficial request that leads to a monstrous solution. Jovanovic's broader point that "if you don't know what you're doing, you're just going to produce garbage faster" applies equally to AI-accelerated feature factories that skip the hard work of understanding the job.

<a class="yt-card" href="https://www.youtube.com/watch?v=0XNkUdzxiZI" target="_blank" rel="noopener"><img src="https://img.youtube.com/vi/0XNkUdzxiZI/hqdefault.jpg" alt="The rise of the professional vibe coder — Lazar Jovanovic"><span>The rise of the professional vibe coder — Lazar Jovanovic</span></a>

**Matt MacInnis** ([Lenny's Podcast, 2025](https://www.youtube.com/watch?v=O_W76LR77Vw)) — Rippling's CPO offers an organizational corollary to the article's warning about product thinking run amok. "If you overstaff, you get politics, you get people working on things that are further down the priority list than necessary. That is poison. It's wasteful. It slows you down. It creates cruft." This is what happens when teams orient around features rather than jobs—without a clear progress-based filter, more people simply means more things being built, not more progress being enabled. Deliberate understaffing forces the kind of ruthless prioritization that progress thinking demands.

<a class="yt-card" href="https://www.youtube.com/watch?v=O_W76LR77Vw" target="_blank" rel="noopener"><img src="https://img.youtube.com/vi/O_W76LR77Vw/hqdefault.jpg" alt="10 contrarian leadership truths — Matt MacInnis"><span>10 contrarian leadership truths — Matt MacInnis</span></a>

**Howie Liu** ([Lenny's Podcast, 2025](https://www.youtube.com/watch?v=GT0jtVjRy2E)) — The Airtable CEO's provocative thought experiment cuts to the heart of why product thinking becomes a trap, especially for established companies. "If you were literally founding a new company from scratch with the same mission, how would you execute on that mission using a fully AI native approach? If you can't, then you should find a buyer." The key word is *mission*—not product, not feature set, not roadmap. Liu is essentially asking: what progress are you trying to help customers make, and is your current product actually the best way to enable it? It's a founder-level version of the article's central question, and a reminder that progress thinking isn't just a prioritization tool—it can be an existential one.

<a class="yt-card" href="https://www.youtube.com/watch?v=GT0jtVjRy2E" target="_blank" rel="noopener"><img src="https://img.youtube.com/vi/GT0jtVjRy2E/hqdefault.jpg" alt="How we restructured Airtable's entire org for AI — Howie Liu"><span>How we restructured Airtable's entire org for AI — Howie Liu</span></a>

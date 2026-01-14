---
type: post
title: Why Your Product Team Speaks a Different Language Than Your customers
description: Every product team has experienced this moment. You ship a feature you're certain customers need. The engineering was solid. The design was clean. The rollout was smooth. And then... crickets. Not because customers don't have the problem you're solving. They do. But because the way you understood their problem and the way they actually experience it exist in two completely different universes.
publication: 2023-06-07 14:57:12
tags:
  - ProductManagement
authors:
  - joel-sooriah
featured: false
redirects:
    - from: root-cause-analysis-in-product-management-learning-the-hard-way
---


# **Why Your Product Team Speaks a Different Language Than Your customers**

Every product team has experienced this moment: You ship a feature you're certain customers need. The engineering was solid. The design was clean. The rollout was smooth. And then... crickets.

Not because customers don't have the problem you're solving. They do. But because the way you understood their problem and the way they actually experience it exist in two completely different universes.


## **The Translation Problem Nobody Talks About**

Here's what typically happens in product development:

A customer tells you: "I need a faster way to handle escalated cases."

Your product team hears: "Build a priority queue with filtering."

Engineering builds exactly that. You ship it. The customer uses it once, maybe twice, then abandons it.

Why? Because what the customer actually meant was: "When my manager asks me why we missed a critical policy violation, I need to show we caught it early and explain what happened—fast enough that I don't look incompetent."

The feature you built solved a workflow problem. The job they were trying to do involved reputation management, organizational trust, and career preservation. Same words, entirely different jobs.


## **The Four Languages Problem**

In my decade of building content moderation systems and working across trust & safety teams, I've watched this translation failure happen across four distinct groups, each speaking their own language:

**Customers speak in outcomes and emotions**: "I need to feel confident we won't miss anything serious."

**Product speaks in features and capabilities**: "We need automated escalation with configurable thresholds."

**Engineering speaks in logic and constraints**: "We need to implement a priority scoring algorithm with rule-based triggers."

**Leadership speaks in metrics and business impact**: "We need to reduce response time on high-severity cases by 40%."

All four groups think they're aligned because they're talking about the same general problem space. But they're solving for completely different things.


## **Why This Matters More Than You Think**

This isn't just about building the wrong feature occasionally. The translation gap creates systemic dysfunction:

**Discovery becomes telephone**: Each handoff from customer → product → engineering → leadership introduces interpretation drift. By the time a customer insight becomes a sprint ticket, it's been translated three times and lost most of its causal truth.

**Disagreements feel personal**: When product and engineering clash over requirements, it's often because product is advocating for the emotional job while engineering is solving for the functional constraint. Neither is wrong—they're just speaking different languages about the same customer need.

**Retrospectives miss the point**: "Why didn't customers adopt this?" becomes a debate about marketing reach or UI polish, when the real answer is: "We built what they asked for, not what would create the progress they needed."

**Priorities become political**: Without a shared language for understanding customer progress, roadmap debates devolve into whoever argues loudest or has the most organizational capital.


## **A Real Example From My Work**

When building our content moderation platform, we interviewed trust & safety teams about their biggest pain points. Over and over, we heard: "We need better tools to track repeat offenders."

Here's how different teams translated that:

**Engineering heard**: "Build a user history database with violation tracking."

**Product heard**: "Create a dashboard showing user violation patterns over time."

**Leadership heard**: "Improve our repeat offender detection rate to reduce platform abuse."

We built all three. Shipped a comprehensive repeat offender tracking system. Beautiful UI, solid technical foundation, clear metrics.

Adoption was terrible.

Why? Because when we finally dug deeper into the actual struggling moment, we discovered what moderators really needed: "When I'm reviewing a case that feels wrong but doesn't obviously violate policy, I need to quickly see if this user has exhibited similar borderline behavior before—so I can make a confident judgment call without second-guessing myself or risking a mistake."

The job wasn't tracking repeat offenders. The job was **reducing the anxiety of making judgment calls in ambiguous situations**. The solution wasn't a dashboard—it was surfacing relevant behavioral patterns at the exact moment of decision-making, embedded in the moderation workflow.

Same customer request. Completely different job. Entirely different solution.


## **The Deeper Problem: We're Not Aligned on What "Understanding" Means**

Most teams think they understand their customers because they:

- Run regular user interviews

- Track usage analytics

- Maintain feedback channels

- Build empathy through shadowing

But understanding what customers do and understanding what progress they're trying to make are fundamentally different things.

**Feature requests are symptoms, not diagnoses**. When a customer says "I need X," they're not handing you a specification—they're describing the first solution that came to mind while experiencing a struggling moment you haven't actually uncovered yet.

**Usage data tells you what happened, not why it mattered**. Knowing that moderators spend 60% of their time looking up policies doesn't tell you whether they're trying to make accurate decisions, cover themselves legally, train new team members, or avoid arguments with colleagues.

**Personas describe people, not progress**. "Sarah is a senior moderator with 3 years experience" doesn't tell you what Sarah is trying to accomplish when she's reviewing her 47th case of the day and her manager just escalated a priority issue.


## **What We Actually Need**

We need a shared language that:

1. **Describes customer reality in causal terms**: Not just what customers do, but what forces create the struggling moment, what progress they're trying to make, and what constraints shape their choices.

2. **Translates cleanly across disciplines**: Product, engineering, design, marketing, sales, and customer success should be able to use the same language without losing meaning in translation.

3. **Stays close to execution**: The gap between customer insight and technical specification should be small enough that we don't lose the causal truth in the handoff.

4. **Makes misalignment visible**: When teams disagree, the language should make it clear whether they're disagreeing about the problem or the solution.

This isn't a theoretical nice-to-have. In content moderation, mistranslation of customer needs directly impacts platform safety. In B2B SaaS, it's the difference between products that get adopted and products that get tolerated. In any product category, it's the difference between innovation that creates genuine progress and features that accumulate like technical debt.


## **The Path Forward**

The rest of this series introduces a solution: **Jobs-to-be-Done methodology as the research framework, and Gherkin syntax as the shared language for translating JTBD insights into executable alignment**.

JTBD gives us the mental models to understand customer progress in causal terms. Gherkin gives us the syntax to communicate those insights across every function without degradation.

Together, they create something I haven't seen elsewhere: a direct path from customer struggling moments to technical specifications that preserves the why behind the what.

In Part 2, we'll introduce Gherkin syntax not as a testing tool, but as the Rosetta Stone your cross-functional team has been missing. Then we'll spend the rest of the series showing you exactly how to use JTBD frameworks to generate the insights that feed it.

Because your product team doesn't need to speak a different language than your customers. You just need the right translation layer.

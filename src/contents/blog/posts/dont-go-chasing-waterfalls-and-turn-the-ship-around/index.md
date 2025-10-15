---
type: post
title: Don't go chasing waterfalls and turn the ship around
description: Historically, many organisations operated with a waterfall-like model where product managers or business analysts would create detailed specifications that engineers would implement. Engineering teams would receive “clearer guidance upfront” with regular check-ins to ensure alignment. This approach treats engineers primarily as implementers who translate requirements into code.
publication: 2023-06-07 14:57:12
tags:
  - swift
authors:
  - joel-sooriah
featured: true
redirects:
    - from: dont-go-chasing-waterfalls-and-turn-the-ship-around
---

Historically, many organisations operated with a waterfall-like model where product managers or business analysts would create detailed specifications that engineers would implement. Engineering teams would receive “clearer guidance upfront” with regular check-ins to ensure alignment. This approach treats engineers primarily as implementers who translate requirements into code.

The Shift Toward Participatory Engineering
------------------------------------------

The modern tech industry increasingly favors empowering engineers to participate in solution design. Leading tech companies have “built intentional cultures that keep top engineers engaged, empowered, and sticking around through clear missions, internal mobility, open-source cred, trust in leadership, and clear technical missions.” [Code, culture, and competitive edge: Who’s winning the engineering talent war in tech?](https://www.signalfire.com/blog/whos-winning-the-engineering-talent-war)

Key aspects of this empowerment approach include:

**Ownership and Decision-Making**: Engineers are encouraged to “make decisions, propose projects, and help set strategy” rather than just implement predetermined solutions. [Engineering Culture at Successful Companies: 9 Common Traits — CTO Fraction](https://ctofraction.com/blog/engineering-culture-at-successful-software-companies/) Companies like Figma exemplify this by giving engineers strategic input.

**Project Leadership**: Some companies designate engineers as project leads who are “empowered to take ownership of the project, starting with initial product requirements and working them through to build and deliver.” [Engineering Culture of Ownership | Built In](https://builtin.com/articles/how-13-tech-companies-build-culture-ownership-their-engineering-teams) This goes beyond technical implementation to include considering schedule, priorities, and resource decisions.

**Collaborative Problem-Solving**: Strong engineering cultures promote “open communication, regular feedback, continuous learning, autonomy, ownership, adaptability, and collaborative environments.” [The Importance of Building a Strong Engineering Culture](https://www.revelo.com/blog/building-strong-engineering-culture)

Industry Benefits and Rationale
-------------------------------

The shift toward participatory approaches reflects several industry realizations:

*   Engineers closest to the technical constraints often have the best insights into feasible solutions
*   Strong engineering cultures “encourage experimentation, risk-taking, and learning from successes and failures” [How to Build a Strong Engineering Culture](https://devdynamics.ai/blog/engineering-culture/) which leads to better outcomes
*   Collaborative cultures enable engineers to work “seamlessly, sharing knowledge, ideas, and resources to solve complex problems” [Engineering Cultures: Unleashing the Potential of Your Tech Team](https://www.metridev.com/metrics/engineering-cultures-unleashing-the-potential-of-your-tech-team/)
*   Empowered engineers tend to be more engaged, innovative, and likely to stay with companies

The consensus among successful tech companies is that while clear communication and alignment remain important, the most effective approach involves engineers as partners in solution design rather than just implementers of predetermined specifications. This participatory model leverages technical expertise more effectively and creates stronger engineering cultures that attract top talent.

The Waterfall Trap Is Back
--------------------------

Fast forward to today, AI tools are luring product teams back into waterfall patterns. [As Alex Hipp points out](https://www.alexhipp.com/blog/the-waterfall-workflow-trap-is-back), “vibe coding has reintroduced the very problems that drove software engineering away from waterfall development two decades ago” [The waterfall trap is back](https://www.alexhipp.com/blog/the-waterfall-workflow-trap-is-back) — teams describe what they want in plain English, AI generates working code in minutes, but the underlying workflow remains dangerously linear.

The parallels are striking: where waterfall had massive spec documents, AI development has giant prompts that teams treat as gospel. Where waterfall meant months of coding before feedback, AI generates everything at once, creating the illusion of progress while actually reducing adaptability. Teams get velocity without true agility — they can ship demos quickly but struggle when users want something different.

The real trap isn’t the speed — it’s the false sense of iteration. Teams think they’re being agile because they can generate new features rapidly, but when feedback demands fundamental changes to architecture or user flows, they hit a wall. The AI-generated foundation can become as rigid as any waterfall artifact.

Most dangerously, AI creates “speed without comprehension.” Teams lose the shared understanding that makes true iteration possible. They become afraid to modify what they don’t fully understand, defaulting to regeneration over refinement.

The solution isn’t avoiding AI — it’s treating it as an accelerant, not autopilot. Successful teams use AI for exploration while maintaining tight feedback loops, light documentation, and collective ownership. They prioritize learning velocity over shipping velocity, ensuring they understand why features work, not just that they do.

Turn the Ship Around
--------------------

“Turn the Ship Around!” by David Marquet offers powerful leadership principles that directly address the core dysfunction of waterfall approaches and provide a blueprint for adaptive product and engineering management.

Inherent Uncertainty in Product Development
-------------------------------------------

Traditional waterfall assumes you can specify requirements upfront and execute linearly. But **user needs evolve, technical discoveries emerge, and market conditions shift**. Instead of fighting this reality:

*   **Product Management**: Build hypothesis-driven roadmaps rather than feature factories. Accept that your initial product requirements are educated guesses that will change as you learn.
*   **Engineering Management**: Design systems for changeability rather than trying to architect the “perfect” solution upfront. Embrace iterative technical design.

Empowerment Over Command-and-Control
------------------------------------

Waterfall centralizes decision-making in planning phases, creating bottlenecks and slow response times. The Leader-Leader model distributes intelligence:

*   **Empower Product Decisions**: Let engineers who understand technical constraints influence feature prioritization. Let customer-facing team members shape product direction based on user feedback.
*   **Empower Technical Decisions**: Give senior engineers authority to refactor code, choose implementation approaches, and make architecture trade-offs within agreed boundaries.

Managing Variability Through Clear Intent
-----------------------------------------

Clarity of Intent Replaces Detailed Specifications
--------------------------------------------------

Instead of 200-page requirements documents, provide clear **outcome-focused intent**:

*   **Product Intent**: “We intend to reduce user onboarding time by 50% while maintaining conversion quality” rather than “Build these 15 specific onboarding screens”
*   **Technical Intent**: “We intend to improve system reliability to 99.9% uptime” rather than prescribing specific technical solutions

Competence Development for Adaptive Teams
-----------------------------------------

Waterfall assumes you can plan away the need for judgment. Instead, invest in capabilities that handle uncertainty:

*   **Cross-functional Competence**: Engineers understanding user problems, PMs grasping technical debt, designers appreciating business constraints
*   **Technical Judgment**: The ability to make good trade-offs between speed, quality, and maintainability under pressure
*   **Product Sense**: Pattern recognition for what works and doesn’t work for users

Psychological Safety Enables Rapid Learning
-------------------------------------------

Waterfall punishes “changes” as scope creep or planning failures. Create environments where:

*   **Pivoting is Celebrated**: When data shows you’re building the wrong thing, changing course is rewarded, not penalized
*   **Technical Experiments are Safe**: Engineers can try new approaches, refactor code, or challenge architectural assumptions without career risk
*   **Honest Feedback Flows**: Bad news travels fast and without punishment, enabling quick course corrections

“I Intend To” Breaks Waterfall Permission Cycles
------------------------------------------------

Traditional approaches create approval bottlenecks. The intent-based language accelerates decision-making:

**Product Examples**:

*   “I intend to remove this feature if usage doesn’t improve after the UX changes” (vs. requiring product committee approval)
*   “I intend to prioritize this customer segment based on support ticket analysis” (vs. waiting for quarterly planning)

**Engineering Examples**:

*   “I intend to implement this performance optimization during the next sprint” (vs. formal architecture review processes)
*   “I intend to roll back this deployment if error rates exceed our threshold” (vs. incident escalation procedures)

Benefits That Transform Product and Engineering Velocity
--------------------------------------------------------

Increased Innovation Through Bounded Experimentation
----------------------------------------------------

*   **Product Teams** can test radical ideas quickly rather than debating them in planning meetings
*   **Engineering Teams** can explore new technologies and approaches within guardrails rather than waiting for “innovation sprints”

Resilience Through Distributed Decision-Making
----------------------------------------------

When problems emerge (and they always do), teams can respond immediately rather than escalating through layers. A critical user experience issue gets fixed by the frontend engineer who discovered it, not scheduled for the next planning cycle.

Unleashing Technical and Product Potential
------------------------------------------

Waterfall treats people as resources executing predetermined plans. Intent-based leadership treats them as intelligent actors who can solve problems creatively within clear boundaries.

Practical Implementation Framework
----------------------------------

**Replace Waterfall Artifacts**:

*   Detailed project plans → Outcome-focused objectives with decision frameworks
*   Change control boards → Clear boundaries and “I intend to” authority
*   Phase gates → Continuous delivery with automated quality gates

**Build New Capabilities**:

*   User research skills across the team, not just dedicated researchers
*   Technical literacy for product managers and designers
*   Business context for engineers and technical teams

**Create New Rhythms**:

*   Weekly learning reviews instead of quarterly planning cycles
*   Daily deployment capability instead of release trains
*   Continuous user feedback instead of post-launch user acceptance testing

The key insight is that variability isn’t a bug in product development — it’s a feature. The organizations that can sense, adapt, and respond to variability faster than their competitors will consistently build better products. Marquet’s principles provide the leadership framework to make this shift from predictive to adaptive product and engineering management.
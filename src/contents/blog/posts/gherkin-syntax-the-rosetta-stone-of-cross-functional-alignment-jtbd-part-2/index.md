---
type: post
title: Gherkin Syntax - The Rosetta Stone of Cross-Functional Alignment
description: In 1799, French soldiers discovered a stone tablet in Egypt that changed our understanding of ancient civilizations. The Rosetta Stone contained the same decree written in three different scripts—hieroglyphics, Demotic, and ancient Greek. Because scholars could read Greek, they could finally decode hieroglyphics.Your product team needs a Rosetta Stone.Not to decode ancient languages, but to translate between the four dialects we identified in Part 1 - customer outcomes, product capabilities, engineering logic, and business metrics. You need a syntax that all four groups can read, write, and understand without losing meaning in translation.That syntax already exists. You've probably seen it in your engineering team's test suites. It's called Gherkin.
publication: 2026-01-15 14:57:12
tags:
  - productmanagement team alignment
authors:
  - joel-sooriah
featured: true
redirects:
    - from: gherkin-syntax-the-rosetta-stone-of-cross-functional-alignment-jtbd-part-2
---


Gherkin Syntax: The Rosetta Stone of Cross-Functional Alignment
-----------------------------------------------------------------------

In 1799, French soldiers discovered a stone tablet in Egypt that changed our understanding of ancient civilizations. The Rosetta Stone contained the same decree written in three different scripts—hieroglyphics, Demotic, and ancient Greek. Because scholars could read Greek, they could finally decode hieroglyphics.

Your product team needs a Rosetta Stone.

Not to decode ancient languages, but to translate between the four dialects we identified in Part 1: customer outcomes, product capabilities, engineering logic, and business metrics. You need a syntax that all four groups can read, write, and understand without losing meaning in translation.

That syntax already exists. You've probably seen it in your engineering team's test suites. It's called Gherkin.


What Is Gherkin? (And Why You Think It's Just for Testing)
----------------------------------------------------------

Gherkin is a structured syntax originally created for Behavior-Driven Development (BDD). Engineers use it to write acceptance criteria that look like this:

```gherkin
Given a user is logged into their account
When they click the "Export Data" button
Then they should receive a CSV file with their data
And the file should download within 3 seconds
```

Most product teams see Gherkin as an engineering artifact—something QA writes, developers reference, and product managers occasionally glance at. It lives in the technical realm, adjacent to code.

This is a catastrophic underutilization of what Gherkin actually offers.


Why Gherkin Is Actually a Universal Translation Protocol
--------------------------------------------------------

Gherkin isn't just a testing syntax. It's a **structured way to describe cause and effect**.

Look at the structure:

- **Given** = The context or situation
- **When** = The action or event
- **Then** = The expected outcome
- **And/But** = Additional context, actions, or outcomes

This structure forces you to think causally:
- What conditions must be true?
- What triggers the change?
- What result must occur?

Now compare that to what you learned in Part 1 about customer jobs. Customers don't want features. They want progress. They have a situation, they take action, they expect a result.

**Gherkin is literally the syntax of progress.**


The Power of Shared Syntax
------------------------------

Here's what happens when every function in your organization uses the same structured syntax:

**Customer Success discovers a struggling moment**:

```gherkin
Given a restaurant manager preparing for evening service
When they need to know which servers are scheduled and which stations they're covering
Then they feel anxious about uneven station distribution
And they spend 15+ minutes manually checking the schedule and floor plan
```

**Product translates that into a requirement**:

```gherkin
Given a restaurant manager opens the schedule for tonight's service
When they view the shift assignments
Then the system should display server assignments with their floor stations
And highlight any stations that are over/under-staffed
```

**Engineering translates that into acceptance criteria**:

```gherkin
Given a shift with id="shift\_123" for today's date
When GET /shifts/shift\_123/assignments is called
Then the API should return server assignments with station mappings
And include staffing\_balance indicators per station
And response time should be under 200ms
```

**Leadership translates that into success metrics**:

```gherkin
Given restaurant managers are preparing for service
When they use the station assignment view
Then pre-service prep time should decrease by 40%
And station balance issues should be identified 90% faster
```

Notice what just happened. The same syntax moved from customer insight to product spec to technical implementation to business metric. Each translation added specificity appropriate to that function, but the causal structure remained intact.

**The Given-When-Then structure preserved the why through every handoff.**


Why This Works When Other Approaches Don't
------------------------------------------

Most cross-functional alignment tools fail because they ask different functions to adopt an entirely new language. Product teams try to get engineers to care about personas. Engineering tries to get product to understand technical constraints. Everyone talks past each other.

Gherkin works because it doesn't ask anyone to abandon their native language. Instead, it provides a **structural grammar** that works for everyone:

**For customers**: Gherkin statements describe their experience in causal terms they recognize. "Given I'm trying to X, when Y happens, then I need Z" maps directly to how they think about their struggles.

**For product managers**: Gherkin forces clarity about context, triggers, and outcomes—the same things product needs to spec requirements effectively.

**For engineers**: Gherkin is already their language for acceptance criteria. No new syntax to learn.

**For designers**: Given-When-Then maps to user flows and interaction states they're already thinking about.

**For QA**: This is literally how they write test cases.

**For marketing**: These statements become the foundation for messaging that describes customer progress, not just features.

**For sales**: Discovery questions can be structured as Given-When-Then explorations of customer context.

Everyone's speaking the same structural language, just emphasizing different parts based on their function.


The Three Levels of Gherkin Translation
---------------------------------------

Gherkin works as a translation layer because it operates at three distinct levels of abstraction—and you can move between them without losing the causal thread.


**Level 1: Job-Level Gherkin (Customer Progress)**

This describes the customer's struggling moment and desired progress in their language:

```gherkin
Given I'm managing a busy Friday night service with 150 reservations
When a server calls in sick 2 hours before service
Then I need to reassign their tables and stations immediately
And avoid overwhelming the remaining servers with unfair distribution
And communicate the changes to the team before service starts
This is pure JTBD territory. No features mentioned. Just context, trigger, and desired outcome.
```


**Level 2: Solution-Level Gherkin (Product Requirements)**

This describes how your product creates that progress:

```gherkin
Given a server's shift is canceled less than 3 hours before service
When the manager opens the schedule
Then the system should suggest reassignment options
And display impact on remaining servers' table counts
And generate a notification draft for the team
And allow one-click reassignment approval
```

Notice: Same structure, now solution-aware. We've moved from customer job to product capability, but the Given-When-Then structure keeps us anchored to the original struggling moment.

**Level 3: Implementation-Level Gherkin (Technical Specs)**

This describes exactly how the system behaves:

```gherkin
Given shift\_id="shift\_456" status changed to "canceled"
When time\_until\_start < 180 minutes
Then POST /shifts/reassign-suggestions with affected\_tables
And calculate server\_load\_balance for remaining staff
And generate notification\_template with changes
And display approval\_interface with one-click confirm
And send real-time updates via WebSocket to manager\_dashboard
Same structure. Same causal logic. Now executable by engineering.
```

**Why This Matters More Than You Realize**

Most product development processes have a **semantic gap** between customer research and technical implementation. Customer insights exist in one format (interview notes, recordings, synthesis documents). Requirements exist in another (user stories, specs). Technical implementation exists in yet another (code, tests, documentation).

Every translation between these formats loses fidelity. Details get dropped. Context gets lost. The "why" behind decisions becomes archaeology.

Gherkin eliminates the semantic gap by providing **one syntax that works at every level of abstraction**.

When a customer insight is documented in Given-When-Then format:

- Product can refine it into requirements without restructuring
- Engineering can translate it into acceptance criteria without re-interpretation
- QA can turn it into test cases without inferring intent
- Everyone can trace back to the original customer job without excavating meeting notes


**A Real Example: The Path from Insight to Code**

Let me show you how this worked when we built context-aware features for restaurant management software.

**Customer interview insight** (Job-Level Gherkin):

```gherkin
Given I'm in the middle of Friday dinner service
When a VIP guest arrives but their reservation isn't showing in the system
Then I need to find their reservation details immediately
And seat them without making them feel like there's a problem
And I need this resolved in under 60 seconds or risk losing the customer
```

**Product requirement** (Solution-Level Gherkin):

```gherkin
Given a host searches for a reservation that doesn't appear in tonight's list
When they enter the guest's name in the search bar
Then the system should search across all dates and flag if found on wrong date
And display the reservation with clear "wrong date" indicator
And offer one-click option to move reservation to tonight
And suggest available tables based on party size
```

**Engineering acceptance criteria** (Implementation-Level Gherkin):

```gherkin
Given reservation with guest\_name="Smith" exists for date != today
When POST /reservations/search with query="Smith" and date=today returns empty
Then GET /reservations/search with query="Smith" and date=any
And if found, return with date\_mismatch: true flag
And include available\_tables\_tonight based on party\_size
And enable PUT /reservations/{id}/move with new\_date and table\_id
```

**QA test case** (Implementation-Level Gherkin):

```gherkin
Given reservation id="res\_789" for "Smith" party of 4 exists for tomorrow
When host searches "Smith" for tonight's date
Then search should return reservation with date\_mismatch: true
And should display available 4-top tables for tonight
And clicking move should update reservation to tonight
And should confirm with success message
Four different functions. Same syntax. Zero semantic loss.
```

The Secret: Gherkin Exposes Your Assumptions
--------------------------------------------

Here's the most powerful aspect of using Gherkin across your entire product development process: **It makes your assumptions visible and testable.**

When you force yourself to write "Given X, When Y, Then Z," you can't hide behind vague language. You can't say "improve the user experience" or "make it more intuitive." You have to specify:

- What context are we assuming?
- What action triggers change?
- What outcome must occur?

This precision surfaces misalignment immediately.

**Product writes**:

```gherkin
Given a manager wants to see labor costs
When they open the reports dashboard
Then they should see labor cost percentages instantly
```

**Engineering reads this and says**: "Wait, what does 'instantly' mean? What time period? What if they have 50 locations?"

That's not a conflict. That's **Gherkin exposing an underspecified requirement before it becomes a bug or a scope argument mid-sprint**.

**Marketing writes**:

```gherkin
Given a prospect concerned about employee turnover
When they ask about scheduling features
Then we should explain our auto-scheduling capabilities
```

**Product reads this and says**: "What specific auto-scheduling features? What aspect of turnover does it address? What outcome does the prospect need?"

Again, not a conflict. Just an assumption becoming visible early enough to address it.


How Gherkin Prevents The Telephone Game
---------------------------------------

Remember the telephone game from childhood? One person whispers a message, it passes through five people, and by the end it's completely different?

That's how most product insights travel through organizations:

1. Customer says: "I need to adjust schedules faster when employees call in sick"
2. Customer success translates: "Customers want better schedule management"
3. Product translates: "Build a drag-and-drop schedule editor"
4. Engineering translates: "Implement a grid-based UI with drag handlers"
5. QA tests: "Verify shifts can be moved via drag and drop"

The original customer job (rapidly handling last-minute callouts without disrupting service) is completely gone by step 5.

With Gherkin, the original insight stays intact:

```gherkin
Given an employee calls in sick 2 hours before their shift
When the manager needs to cover their tables and responsibilities
Then the manager needs reassignment suggestions within 30 seconds
And needs to notify affected staff immediately
And needs confidence the new assignments won't overwhelm anyone
```

Product can see this isn't about drag-and-drop—it's about **rapid reassignment with impact analysis and communication**. The solution becomes completely different: not a fancy editor, but an intelligent reassignment wizard with one-click approval and automated team notifications.

Engineering can implement this without re-interpreting because the job is already specified in causal terms.

QA can test whether the actual outcome (rapid, confident reassignment) matches the customer's job, not just whether the technical implementation works.


The Structure Enables Collaboration, Not Just Communication
-----------------------------------------------------------

Most alignment tools are about **communication**—getting information from one function to another. Gherkin enables **collaboration**—multiple functions working on the same problem in compatible ways.

When everyone uses Given-When-Then:

**Product and design can collaborate on user flows**:

- Product specifies the context and outcome
- Design specifies the interaction that bridges them
- Both are working in the same syntax

**Engineering and QA can collaborate on acceptance criteria**:

- Engineering writes what the system should do
- QA writes how to verify it happened
- Same structure, complementary perspectives

**Product and marketing can collaborate on messaging**:

- Product describes the progress customers make
- Marketing describes how to communicate that progress
- Both anchored to the same customer job

**Sales and customer success can collaborate on discovery**:

- Sales asks Given-When-Then questions to understand context
- CS uses Given-When-Then statements to explain solutions
- Both are diagnosing the same job in compatible terms


Setting Up Your Organization to Use Gherkin
-------------------------------------------

Here's how to introduce Gherkin as a cross-functional syntax:


**Start with one team, one workflow**

Pick a single product team and a single customer job they're working on. Have them document:

- The customer job in Job-Level Gherkin
- Their product requirements in Solution-Level Gherkin
- Their acceptance criteria in Implementation-Level Gherkin


**Run a translation exercise**

Take an existing feature request and translate it together as a team:

1. Someone from customer-facing writes the job-level statement
2. Product translates to solution-level
3. Engineering translates to implementation-level
4. The group compares: Did we lose anything? Did we add assumptions?


**Create templates for each function**

**For customer research**:

```gherkin
Given \[context and constraints]
When \[trigger or struggling moment]
Then \[desired progress]
And \[forces that enable or prevent progress]
```

**For product requirements**:

```gherkin
Given \[user state or system context]
When \[user action or system event]
Then \[system behavior or user outcome]
And \[additional requirements or constraints]
```

**For engineering specs**:

```gherkin
Given \[preconditions and system state]
When \[action or event occurs]
Then \[expected system response]
And \[side effects or additional outcomes]
```

Establish translation moments
-----------------------------

Build Gherkin translation into your existing ceremonies:

- **Backlog refinement**: Require Given-When-Then format for stories
- **Sprint planning**: Review acceptance criteria in Gherkin syntax
- **Customer interviews**: Document jobs in Given-When-Then structure
- **Retrospectives**: Analyze misalignment using Gherkin statements


What Gherkin Doesn't Solve (And Why You Need JTBD)
--------------------------------------------------

Gherkin is a syntax, not a methodology. It gives you structure, but it doesn't tell you:

- How to discover the right customer jobs
- How to distinguish functional, emotional, and social progress
- How to identify the forces that enable or prevent progress
- How to prioritize which jobs to solve for
- How to know when you're building around ideas instead of jobs

That's where Jobs-to-be-Done methodology comes in.

**Gherkin is your translation layer. JTBD is your research framework.**

In the rest of this series, we'll dive deep into JTBD frameworks—specifically the three most powerful ones: Ulwick's Outcome-Driven Innovation, Kalbach's JTBD Canvas 2.0, and Boehme's Wheel of Progress. You'll learn how to use each framework to generate insights about customer jobs.

And here's the key: **Everything you learn from JTBD research can be documented in Gherkin syntax.**

When you interview customers using Ulwick's outcome statements, you can translate them into Given-When-Then format. When you map customer journeys using Kalbach's canvas, each step becomes a Gherkin scenario. When you analyze switching behavior using Boehme's Wheel, the forces become Given-When-Then conditions.

JTBD provides the mental models to understand customer progress. Gherkin provides the syntax to communicate that understanding across your entire organization without degradation.

Together, they solve the translation problem we identified in Part 1.


Next: From Product Thinking to Customer Progress Thinking
---------------------------------------------------------

Now that you understand the syntax that will tie everything together, we're ready to dive into JTBD methodology itself.

Part 3 will challenge the way you think about innovation entirely. We'll explore why "product thinking" leads teams astray, how to shift to "customer progress thinking," and what it actually means to understand the jobs customers are hiring your product to do.

Because before you can translate customer jobs into requirements, you need to understand what a job actually is—and why most teams completely misunderstand the concept.



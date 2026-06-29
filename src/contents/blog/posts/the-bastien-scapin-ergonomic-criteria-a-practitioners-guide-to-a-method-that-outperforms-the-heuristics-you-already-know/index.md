---
type: post
title: The Bastien & Scapin Ergonomic Criteria - A Practitioner's Guide to a Method That Outperforms the Heuristics You Already Know
description: If you've run a heuristic evaluation, you've probably used Jakob Nielsen's 10 usability heuristics. They're fast, well-known, and good enough for a first pass. They're also not the only option — and in at least one direct comparison, not the better one.
publication: 2026-06-29 15:22:08
tags:
  - 
authors:
  - joel-sooriah
featured: false
redirects:
    - from: the-bastien-scapin-ergonomic-criteria-a-practitioners-guide-to-a-method-that-outperforms-the-heuristics-you-already-know
---

# The Bastien & Scapin Ergonomic Criteria: A Practitioner's Guide to a Method That Outperforms the Heuristics You Already Know

If you've run a heuristic evaluation, you've probably used Jakob Nielsen's 10 usability heuristics. They're fast, well-known, and good enough for a first pass. They're also not the only option — and in at least one direct comparison, not the better one.

Bastien and Scapin's ergonomic criteria are a less-cited but more rigorously derived framework, built specifically for the kind of close, systematic inspection that catches problems a quick Nielsen pass misses. This article covers where the criteria came from, what they actually contain, how they stack up against Nielsen's heuristics in practice, and how to actually run an evaluation with the method.

## Where the criteria came from

Christian Bastien and Dominique Scapin, both researchers in ergonomic psychology and cognitive ergonomics, published the criteria in May 1993 as an INRIA technical report (RT-0156), under the title "Ergonomic Criteria for the Evaluation of Human-Computer Interfaces." A refined version followed in 1997 in *Behaviour & Information Technology*.

The method wasn't built top-down from theory. Bastien and Scapin gathered roughly 900 existing ergonomic recommendations from the human-computer interaction literature and sorted them — empirically, through an iterative classification process — into a structure that could hold all of them without losing the distinctions that made each recommendation useful. That sorting process is what produced the final structure: **8 main criteria, broken into 18 elementary sub-criteria.**

This origin matters for how you should think about the method. Nielsen's heuristics were authored as a compact, memorable set of ten. Bastien and Scapin's were derived from a much larger body of accumulated, validated guidance and only afterward compressed into a usable taxonomy. The criteria are more granular as a direct consequence — and that granularity is what gives evaluators more precise language for what's actually wrong with an interface.

## The 8 criteria and their 18 sub-criteria

1. **Guidance (Guidage)** — the means available to advise, orient, inform, and guide the user through their interactions with the system. Splits into:
   - *Prompting* — are users told what's expected of them at each step?
   - *Grouping/Distinction of Items* — are related items visually grouped, and unrelated items visually distinguished?
   - *Immediate Feedback* — does the system respond to user actions in a way that confirms what just happened?
   - *Legibility* — are labels, text, and visual elements actually readable?

2. **Workload (Charge de travail)** — minimizing the perceptual and cognitive load on the user, and maximizing dialogue efficiency. Splits into:
   - *Brevity* — are interactions as short as they can be without losing clarity?
   - *Minimal Actions* — is the number of steps to complete a task as low as it can reasonably be?

3. **Explicit Control (Contrôle explicite)** — the system should only do what the user explicitly asks it to, and the user should be able to control the pace and sequence of their own actions. Splits into:
   - *Explicit User Action* — does the system only take consequential action in direct response to something the user asked for, rather than as a side effect?
   - *User Control* — can the user control the dialogue (interrupt, go back, change their mind) rather than being railroaded through a fixed sequence?

4. **Adaptability (Adaptabilité)** — the system's capacity to behave differently for different contexts and different users. Splits into:
   - *Flexibility* — are there multiple ways to accomplish the same task, suited to different user preferences?
   - *User Experience Consideration* — does the system account for users at different experience levels (a novice and a power user shouldn't be forced through identical interaction paths)?

5. **Error Management (Gestion des erreurs)** — preventing errors where possible, and handling them well where not. Splits into:
   - *Error Protection* — does the system prevent or flag likely mistakes before they cause damage?
   - *Quality of Error Messages* — when something goes wrong, is the message specific and actionable, or generic and unhelpful?
   - *Error Correction* — can the user actually recover from the error without starting over?

6. **Consistency (Homogénéité/Cohérence)** — similar elements and actions should look and behave the same way throughout the system, so that what a user learns in one place transfers to another.

7. **Significance of Codes (Signifiance des codes et dénominations)** — labels, codes, and abbreviations should have an understandable, ideally self-evident, relationship to what they represent — not an arbitrary one the user has to memorize.

8. **Compatibility (Compatibilité)** — the degree to which the system matches the characteristics, expectations, and prior experience of its actual users (their task knowledge, their habits from other tools, their mental models).

Two things stand out next to Nielsen's list. First, several criteria that Nielsen folds into one heuristic are split apart here — *Error Prevention* and *Help Users Recognize, Diagnose, and Recover from Errors* are one Nielsen heuristic, but three distinct Bastien & Scapin sub-criteria (Error Protection, Quality of Error Messages, Error Correction). Second, *Compatibility* has no clean Nielsen equivalent — it's closest to "match the real world," but it's explicitly about the user's actual prior experience with other systems, not just real-world conventions in the abstract.

## Does the extra granularity actually find more problems?

This is the part that's easy to assert and hard to prove, so it's worth being precise about the one study that's actually tested it directly.

Luzzardi et al. (2004), in a comparative case study evaluating information visualization techniques, had separate groups of evaluators run heuristic evaluations using Nielsen's heuristics and Bastien & Scapin's criteria on the same interfaces. The Bastien & Scapin group found more problems overall (46 vs. 39) and, more importantly, found a higher proportion of severe problems (22 vs. 14). The criteria's extra granularity didn't just produce more line items — it produced more of the line items that actually mattered.

That's a single study, not a meta-analysis, and direct head-to-head comparisons between the two frameworks remain rare in the literature. It's evidence, not proof. But it's evidence in a specific, falsifiable direction, which is more than can be said for most "heuristic A vs. heuristic B" claims that circulate in UX folklore.

## How to actually run an evaluation with this method

1. **Don't try to apply all 18 at once on first pass.** Walk the interface task by task (not screen by screen), and at each step ask which criterion, if any, is being violated.
2. **Use the sub-criteria to settle disagreements, not just to generate findings.** When two evaluators disagree about whether something is a problem, the granularity often resolves it — "is this a Guidance issue or an Error Management issue?" is a more answerable question than "is this generally bad UX?"
3. **Expect inter-rater variation, and plan for it.** Even trained evaluators don't converge perfectly on which criterion best explains a given problem — that's a known limitation of the method, not a sign you're doing it wrong. Pair evaluations or a short calibration pass help more than trying to write an ever-more-precise definition.
4. **Log the criterion name with each finding, not just a severity score.** This is what makes the method more actionable for engineering teams than a generic "usability issue" ticket — it tells the team which category of fix is needed.

For product teams specifically — where the cost of a missed error-handling or guidance failure isn't just an annoyed user but a support escalation or a churn risk — the extra rigor is rarely wasted effort.

---

*Sources: Bastien, J.M.C. & Scapin, D.L. (1993), "Ergonomic criteria for the evaluation of human-computer interfaces," INRIA Technical Report RT-0156; Scapin, D.L. & Bastien, J.M.C. (1997), "Ergonomic criteria for evaluating the ergonomic quality of interactive systems," Behaviour & Information Technology, 16(4–5); Luzzardi et al. (2004), comparative case study cited via Chen, "UX heuristics: a closer look at Bastien and Scapin."*
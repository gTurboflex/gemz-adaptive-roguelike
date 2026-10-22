# User discussions and relevance evidence

**Evidence status: no discussions have been recorded.** The university asks for 3–5 substantive discussions with user representatives or an actual client agreement. A public game description is useful background but does not replace that evidence. This document is a ready-to-use protocol and an empty evidence register.

Recruit 3–5 adults with relevant PC action/roguelike experience, including at least one less experienced player if available. Explain the diploma purpose, voluntary participation and intended use of anonymized notes. Agree the university's consent/recording requirements before recording audio or video. Store contacts and consent records outside the repository; refer to participants as U01–U05.

## Discussion guide

1. Which action or roguelike games have you played recently, and what do you enjoy about their difficulty?
2. Describe a specific occasion when enemies became repetitive or a difficulty change felt unfair.
3. What signals would help you recognize that enemies are responding to your tactics?
4. In the mining scenario, when would you choose extraction instead of descending?
5. Which adaptations would make you try another strategy, and which would make a build feel invalid?
6. Walk through the mockup: select difficulty, mine, preview the next encounter and extract. Explain what you expect at each step.
7. Would you want an adaptation notice or an option to disable adaptation? Why?
8. Which three features matter most for a small prototype? What could be removed?

Avoid asking whether the proposed ML system is “innovative” or whether the player “likes our great idea”. Ask for concrete prior examples, expectations and observable misunderstandings.

## Project-specific follow-up prompts — prepared 22 October 2026

These prompts refine the proposed GEMZ requirements. They are preparation, not participant findings or evidence of a personal walkthrough by Zhangir.

- FR02, mining and extraction: after explaining that the player may extract or descend, ask what they expect to keep, what they expect to risk, and what information they need before deciding. Ask for an example from a game they have played.
- FR07/FR09, bounded adaptation: ask the participant to describe an acceptable and an unacceptable enemy response to repeated ranged or close attacks. Ask when they expect the response to take effect, without first suggesting the planned boundary rule or 25% cap.
- FR13, explanation: after the participant has actually seen a preview, ask them to explain in their own words what will change and when. Record misunderstandings separately from interpretations by the interviewer.
- FR10, experimental conditions: ask what differences the participant expects between fixed enemies, rules and a profile-informed response. Explain that the current HTML uses simulated inputs and does not run a trained classifier.
- FR01, preparation: ask which starting difficulty they would choose and why, and whether the labels provide enough information. Ask about accessibility or control needs before proposing a solution.

For each discussion, link an observation to the relevant requirement ID. A confirmed expectation and a requested change are different outcomes. Running a checklist with an assistant is not one of the required 3–5 user discussions.

## Evidence register (unfilled)

| ID | Date | Relevant experience | Consent record location | Notes and observation | Requirement change |
|---|---|---|---|---|---|
| U01 | Pending | Pending | Private, pending | No evidence collected | Pending |
| U02 | Pending | Pending | Private, pending | No evidence collected | Pending |
| U03 | Pending | Pending | Private, pending | No evidence collected | Pending |
| U04, optional | Pending | Pending | Private, pending | No evidence collected | Pending |
| U05, optional | Pending | Pending | Private, pending | No evidence collected | Pending |

After each discussion, record an anonymized observation or an accurately attributed short quotation, distinguish observation from interpretation, and link a concrete requirement or design change. Retain disagreement instead of inventing consensus. Proposed hypotheses are that players want visible limits, meaningful extraction choices and counterplay; none is currently verified.

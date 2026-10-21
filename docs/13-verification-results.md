# Current prototype verification results

Checks performed on 21 October 2026 against the initial materials branch:

| Check | Observed result | Scope limitation |
|---|---|---|
| Python unit tests | 10 passed | Reference model contracts only; no Unity integration or learned classifier |
| Deterministic synthetic demo | Output transitions from ranged to close remembered style after manually supplied probabilities change | Synthetic inputs and manual shift flag; not human evidence or detector validation |
| Materials integrity check | Required diagram artifacts, local Markdown links and 11 prepared task records pass | Does not establish research quality, review approval or live YouTrack assignment |
| Browser scenario walkthrough | Hard start → enter → mine → preview → descend → mine → extract; summary shows 24 Gemz from two chambers | Simulated interactions; no playable combat or gameplay telemetry |
| Visual inspection | Three PNG diagrams and desktop scenario layout inspected | Diagram consistency still requires team and supervisor review |

The tests cover bounded EAS/difficulty under extreme inputs, no in-combat budget change, capped elapsed-time steps, static control, memory turnover, accelerated turnover under a manual shift flag, low-confidence decay, stale/invalid inference tactics, explicit fallback reset, invalid numeric input and starting-difficulty separation. No classifier accuracy, inference performance, real user preference or Unity frame-rate result is claimed.

Re-run the commands in the README after changing the controller. Preserve measured Unity and study results in separate reports when those systems exist.

# Current prototype verification results

Checks performed on 21 October 2026 against the initial materials branch:

| Check | Observed result | Scope limitation |
|---|---|---|
| Python unit tests | 10 passed | Reference model contracts only; no Unity integration or learned classifier |
| Deterministic synthetic demo | Output transitions from ranged to close remembered style after manually supplied probabilities change | Synthetic inputs and manual shift flag; not human evidence or detector validation |
| Materials integrity check | Required diagram artifacts, local Markdown links and 11 linked task records pass | Does not establish research quality or review approval |
| Live YouTrack setup | Dedicated GEMZ project and 11 saved tasks verified; all have an owner assignment, priority and actual due-date field, and remain To do | Historical setup observation; individual assignments were verified on 22 October, all states still To do |
| Browser scenario walkthrough | Hard start → enter → mine → preview → descend → mine → extract; summary shows 24 Gemz from two chambers | Simulated interactions; no playable combat or gameplay telemetry |
| Visual inspection | Three PNG diagrams and desktop scenario layout inspected | Diagram consistency still requires team and supervisor review |

The tests cover bounded EAS/difficulty under extreme inputs, no in-combat budget change, capped elapsed-time steps, static control, memory turnover, accelerated turnover under a manual shift flag, low-confidence decay, stale/invalid inference tactics, explicit fallback reset, invalid numeric input and starting-difficulty separation. No classifier accuracy, inference performance, real user preference or Unity frame-rate result is claimed.

Re-run the commands in the README after changing the controller. Preserve measured Unity and study results in separate reports when those systems exist.

The checks above are historical observations of the original package. The UX mock-up and pending walkthrough checklist were imported by Zhangir in PR #3. No browser scenario is reported as executed by this import. The split does not create new human evidence.

## PR 2 review revision, 22 October 2026

Review by ynagi-1: https://github.com/gTurboflex/gemz-adaptive-roguelike/pull/2#pullrequestreview-5617968862

The review reproduced elevated EAS after a stale result and renewed budget growth immediately after an explicit failure. Three added regression tests failed against the previous implementation; the ten original tests passed. The controller now latches static fallback until explicit fresh, validated recovery. All 13 tests pass after the fix, as does the materials integrity check. New coverage checks stale/invalid results at elevated EAS on Easy and Hard, repeated budget and profile updates while fallback is latched, explicit failure followed by fresh recovery at the 10-second boundary, rejected stale/malformed recovery, and safe-boundary budget growth after recovery. This is reference-controller verification only; ynagi-1 subsequently approved this fix and PR #2 was merged. Unity integration remains pending.

## PR 3 import review, 22 October 2026

Review scope: README, interview protocol, imported HTML and walkthrough checklist. The new prompts align with FR01/FR02/FR07/FR09/FR10/FR13. Source inspection confirms the documented scenario handlers; it is not browser execution. Editorial corrections repair the walkthrough title encoding and replace stale pre-import statements. All eight browser scenarios remain Not run, the interview table is unfilled, and YouTrack states are unchanged. Thirteen controller tests and the materials check pass on the reviewed branch.

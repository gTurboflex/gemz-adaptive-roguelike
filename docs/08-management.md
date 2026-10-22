# Project management and risks

The immediate milestone is the materials checkpoint on **24 October 2026**. Dates below use the user's Asia/Qyzylorda calendar; no time of day was specified by the university. Later dates are proposed internal checkpoints and must be aligned with the official diploma calendar.

## Responsibility proposal

| Area | Proposed lead | Reviewer |
|---|---|---|
| Gameplay, UX, cave route, enemy state machines | Sailaubek Zhangir, SE-2429 | Yessentemirov Yergun |
| Telemetry, profiles, controller, ML evaluation | Yessentemirov Yergun, SE-2418 | Sailaubek Zhangir |
| Literature, requirements, experiments and thesis | Both students | Aigerim Bakiyeva |

The split was agreed on 22 October 2026. gTurboflex belongs to Yessentemirov Yergun; ynagi-1 belongs to Sailaubek Zhangir. Their YouTrack accounts are admin and Zhangir respectively. Supervisor: Aigerim Bakiyeva. Initial analysis and code are preparation. Separate imports identify who inspected/uploaded files and do not prove independent authorship. Individual findings and revisions are still needed.

## Milestones

| Target | Outcome | Dependency |
|---|---|---|
| 21 Oct | Initial repository and reviewable materials package | Requirements document and project concept |
| 22 Oct | Three to five real user discussions and revised assumptions | Participant availability; approved recording approach |
| 23 Oct | Team review, supervisor comments and corrections | Aigerim Bakiyeva’s availability; account access |
| 24 Oct | Reviewed checkpoint snapshot and submission summary | Dedicated YouTrack, accepted materials and access for committee |
| 6 Nov, proposed | Unity vertical slice and deterministic controller replay | Editor version and minimal assets |
| 20 Nov, proposed | Labeled pilot dataset and model comparison | Consent/approval, playable slice and feature validation |
| 4 Dec, proposed | Integrated model, failures and performance tested | Export parity and declared machine |
| 18 Dec, proposed | Pilot experiment and initial analysis | Recruitment and protocol approval |

## Risk register

| Risk | Likelihood / impact | Mitigation | Trigger / owner |
|---|---|---|---|
| Art and procedural scope exceeds capacity | High / high | One planet, modular rooms, flat-color assets; no voxel destruction | Vertical slice slips / gameplay lead |
| Too little labeled data | High / high | Pilot collection, Mixed class, simple baseline, explicit uncertainty | Classes missing in development folds / ML lead |
| Adaptation feels punitive | Medium / high | Boundary changes, caps, warning and control conditions | Negative fairness feedback / both |
| Feature leakage inflates results | Medium / high | Group by participant; separate test set and train-only preprocessing | Shared participant IDs across splits / ML lead |
| Inference or logging causes stalls | Medium / high | Bounded queue, snapshots, fallback and profiler measurements | p95 overhead >1 ms / ML lead |
| Supervisor review unavailable before deadline | Medium / high | Request review early; retain actual comments and unresolved decisions | No review by 23 Oct / both |
| Assignments diverge from evidence | Medium / medium | Keep individual task ownership and record actual results separately | Missing results or review / both students |
| Untraceable individual contributions | Present / high | Individual accounts and substantive reviewed changes; no fabricated history | Missing student-specific evidence / both |

## Workflow

The dedicated project has eleven tasks, all To do, with priorities and deadlines. Yergun/admin owns GEMZ-1,3,4,5,7,8,9,11; Zhangir owns GEMZ-2,6,10. Zhangir reviews GEMZ-4,5,8; GEMZ-7 and GEMZ-11 involve both students. Keep one accountable assignee per task. Include actual IDs in branches, commits and PRs. Another team member reviews before merge.

The owner requested replacing the draft history on 22 October 2026. The old release/tag is withdrawn; earlier PR history may remain accessible on GitHub. New imports do not imply completed interviews, supervisor comments or review approval. Create the next submission tag only after both students' contributions and review are accepted.

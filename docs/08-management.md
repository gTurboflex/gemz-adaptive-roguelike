# Project management and risks

The immediate milestone is the materials checkpoint on **24 October 2026**. Dates below use the user's Asia/Qyzylorda calendar; no time of day was specified by the university. Later dates are proposed internal checkpoints and must be aligned with the official diploma calendar.

## Responsibility proposal

| Area | Proposed lead | Reviewer |
|---|---|---|
| Gameplay, UX, cave route, enemy state machines | Сайлаубек Жангир, SE-2429 | Yessentemirov Yergun |
| Telemetry, profiles, controller, ML evaluation | Yessentemirov Yergun, SE-2418 | Сайлаубек Жангир |
| Literature, requirements, experiments and thesis | Both students | Aigerim Bakiyeva |

The split requires team confirmation. GitHub account **gTurboflex** belongs to **Yessentemirov Yergun, SE-2418**. Supervisor: **Aigerim Bakiyeva**. The second student’s and supervisor’s account details remain pending. Do not attribute assisted initial commits to independent student work. Each student must submit substantive changes through their own account and explain them at the checkpoint.

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
| No personal YouTrack workspace | Present / medium | Prepare task package; register a free instance or use an existing authorized one | Cannot create a project / repository owner |
| Untraceable individual contributions | Present / high | Individual accounts and substantive reviewed changes; no fabricated history | Missing student-specific evidence / both |

## Workflow

Create one real YouTrack task per meaningful deliverable with assignee, priority, deadline and acceptance criteria. Replace local PLAN keys with issued IDs; use the real ID in branch and commit/PR descriptions. Link the PR or commit back to the task. Another team member reviews before merging. The supervisor reviews selected significant decisions at agreed checkpoints.

`main` begins with repository initialization. The initial materials are submitted on a branch for review. An open PR is not approval. Do not mark user interviews or supervisor feedback complete merely because a form exists. Use `pre-defense-1`, `pre-defense-2`, and `final-pre-defense` for the actual reviewed submission snapshots, never as retroactive evidence of reviews.

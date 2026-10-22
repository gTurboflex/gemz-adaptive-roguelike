# Project proposal and scope

## Proposed title

Design and Evaluation of a Player Profiling and Bounded Enemy Adaptation System in a 3D Roguelike Game

Working game title: **GEMZ**. Students: Сайлаубек Жангир, SE-2429; Yessentemirov Yergun, SE-2418. Supervisor: **Aigerim Bakiyeva**. Approval of the topic has not been recorded.

## Problem statement and relevance

Action roguelikes need repeatable challenge without making all encounters predictable. A single fixed difficulty does not describe differences in combat distance, damage preference or movement. Conversely, responding to every successful action with stronger opposition can discourage experimentation. The project will investigate whether a slowly updated player profile can support recognizable enemy responses while preserving bounded difficulty and a playable escape route.

The literature establishes DDA as an existing field; adding machine learning to a game is not itself a new scientific contribution [S1–S3 in the literature review]. The proposed contribution is an implementation and controlled evaluation of the combination of profiling, fading memory, a bounded EAS controller and explicit application boundaries in a mining roguelike. Novelty beyond this combination is not claimed. Player demand and preferred limits must still be checked through 3–5 discussions.

## Aim and research questions

The aim is to design, implement and evaluate a modular adaptation system that recognizes combat styles and adjusts enemy strategies without unacceptable instability or runtime overhead.

- RQ1: Can a lightweight supervised classifier recognize the selected combat archetypes on held-out players better than majority and simple-rule baselines?
- RQ2: How quickly can fading profile memory follow a deliberate tactic change without oscillating on noisy windows?
- RQ3: Compared with static difficulty and rule-based adaptation, how does profile-informed adaptation affect completion, perceived fairness, challenge and frame-time overhead?

Success criteria and their provisional thresholds are specified in the verification plan. A negative or inconclusive result remains a valid research outcome if the experiment and limitations are reported accurately.

## Objectives and expected outputs

1. Review DDA, player modeling and non-stationary data methods, and record supported limitations.
2. Establish user-informed requirements and a minimal gameplay scenario.
3. Implement event collection, feature windows, model inference and an auditable controller interface.
4. Build a short playable 3D expedition with two fixed starting difficulties and switchable experimental adaptation modes.
5. Compare candidate classifiers using participant-separated data and implement the selected model locally.
6. Test memory decay, distribution-change signals, failure recovery and timing limits.
7. Run a counterbalanced pilot and report uncertainty, reproducibility information and threats to validity.

Expected deliverables are a Unity source project and executable build, versioned model and feature definitions, a reproducible evaluation package, architectural documentation, tests and the thesis. These are future deliverables; the current checkpoint package is listed in the README.

## Game setting and loop

In the fictional setting, humanity survives an unexplained loss of solar energy by searching for Gemz crystals to power an artificial sun. The story is science fiction, not an astrophysical claim. A miner leaves the expedition ship, enters a cave, fights or avoids creatures, collects crystals, selects upgrades and either extracts or risks a deeper chamber. Greater depth provides greater potential reward and a higher threat budget. Gemz can power equipment and the colony; only a small subset of these effects is needed for the experiment.

The visual direction is stylized low-poly using flat colors and limited textures. Cel shading is optional after the core loop is stable. This choice reduces planned art scope; a performance or production-time benefit has not yet been measured.

## MVP boundaries

| Included | Acceptance boundary |
|---|---|
| Windows PC single-player | Keyboard and mouse; one miner; no network dependency during a run |
| One planet and cave route | Seeded arrangement of modular rooms with reachable extraction |
| Combat and mining | Two damage types, three enemy archetypes, crystals and one upgrade decision |
| Run structure | Preparation, combat, descent or extraction, summary |
| Adaptation experiment | Static, rule-based and profile-informed modes; Easy and Hard starting difficulty |
| Instrumentation | Local opt-in experiment logs, model/config/build identifiers and seed |

Out of scope: online co-op, autonomous squad companions, an open galaxy, realistic solar physics, extensive cinematic content, fully deformable terrain, live reinforcement-learning training and commercial release. If the schedule slips, retain the experimental arena and controller evaluation before expanding art or procedural content.

## Assumptions requiring agreement

The team must confirm its responsibility split, camera perspective, supervisor review arrangements, study recruitment route, target test hardware and final diploma milestones. Current date targets beyond 24 October are planning proposals. No interviews, ethics approval or supervisor endorsement are implied by this document.

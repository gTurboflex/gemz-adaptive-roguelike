# GEMZ Adaptive Roguelike

**Diploma project:** Design and evaluation of a player profiling and bounded enemy adaptation system in a 3D roguelike game.

GEMZ is a single-player expedition game in which a space miner explores alien caves, collects energy crystals and chooses whether to descend or extract. The game is an experimental environment for comparing static difficulty, rule-based adaptation and adaptation informed by a learned player profile.

## Problem and intended users

Fixed enemy behavior can become predictable, while aggressive difficulty changes can feel unfair. The engineering problem is to detect changes in combat style and respond within explicit timing, strength and performance limits. Intended users are PC action roguelike players; researchers and the supervisor use local experiment logs to assess the system. Improved enjoyment is a hypothesis, not an established project result.

## Team and supervision

| Member | Group | Proposed responsibility |
|---|---|---|
| Сайлаубек Жангир | SE-2429 | Gameplay loop, Unity scenes, enemy state machines and UX |
| Yessentemirov Yergun | SE-2418 | Telemetry, profiling, EAS controller and evaluation tooling |

The responsibility split is a planning proposal for team confirmation. Repository owner **gTurboflex** is **Yessentemirov Yergun, SE-2418**, confirmed by the owner. Supervisor: **Aigerim Bakiyeva**. The second student’s official Latin spelling and individual account, the supervisor’s account, and the new YouTrack account mapping remain to be confirmed. No invitations have been sent.

## Scope and current status

Prepared on **21 October 2026** for the **24 October** materials checkpoint. This repository currently contains analysis and design documents, editable architecture diagrams with readable exports, an interactive UX mockup, and a small executable Python reference model of the proposed controller with automated tests.

**There is no playable Unity build, collected player dataset, trained classifier, user-study result or supervisor approval yet.** The Python model receives manually supplied probability vectors; it does not demonstrate learned enemy intelligence. The mockup is a scenario prototype, not a 3D game.

The MVP targets Windows PC, one planet, a modular cave route, one playable miner, three enemy archetypes, two damage types, extraction and a 10–15 minute experimental run. NPC expedition members are narrative context. Squad AI, multiplayer, a galaxy simulation and fully destructible voxel terrain are outside the MVP.

## Technologies

Planned game stack: Unity 6 / C#, URP and stylized low-poly materials. Exact editor and package versions will be pinned when the Unity project is initialized. ML experiments will use Python and scikit-learn; Decision Tree, Random Forest and k-NN are candidates. The intended runtime loads a versioned compact tree model locally in C#; no Python service or network access is required during play. The current reference model uses only Python standard-library modules.

## Read the materials

1. [Proposal and scope](docs/01-proposal.md)
2. [Literature review and source register](docs/02-literature-review.md)
3. [Existing systems comparison](docs/03-existing-systems.md)
4. [Technology alternatives](docs/04-technology-comparison.md)
5. [Requirements and acceptance criteria](docs/05-requirements.md)
6. [Architecture and adaptation specification](docs/06-architecture.md)
7. [Verification and evaluation](docs/07-verification.md)
8. [Management, milestones and risks](docs/08-management.md)
9. [User discussion protocol](docs/09-user-evidence.md)
10. [Supervisor review record](docs/10-supervisor-feedback.md)
11. [Submission readiness checklist](docs/11-submission.md)
12. [Data dictionary](docs/12-data-dictionary.md)
13. [Architecture decision records](docs/adr/decisions.md)

[YouTrack setup status and task package](management/youtrack-setup.md): the owner has submitted a dedicated workspace registration; email activation and the project URL are pending. The currently signed-in `youtrack.jetbrains.com` account belongs to JetBrains' public tracker; it is not a personal project workspace. Prepared tasks are in [backlog.json](management/backlog.json). Local PLAN identifiers are not issued YouTrack IDs.

## Run and check what exists

Open `prototype/index.html` in a current desktop browser. It works offline and demonstrates preparation, a mining decision, an adaptation preview and extraction. Its manual controls are for demonstration, not measured telemetry.

From the repository root, with Python 3.10 or later:

```text
python -m src.adaptation.demo
python -m unittest discover -s tests -v
python scripts/check_materials.py
```

The first command prints a deterministic synthetic controller demonstration. The second checks safety limits, fallback behavior and profile forgetting. The third checks required artifacts and local Markdown links. No third-party dependencies are required for these commands. Unity execution instructions will be added together with the first runnable Unity scene.

## Structure and development process

```text
src/adaptation/   Executable reference model, not Unity runtime code
prototype/        Offline interactive UX scenario
docs/             Proposal, review, requirements, architecture, evaluation
diagrams/         Editable SVG and PlantUML sources, PNG exports
tests/            Controller contract tests
config/           Non-secret configuration example
management/       Task package and YouTrack setup status
scripts/          Materials integrity check
```

Use individual student accounts, real task branches, pull requests and another team member's review. See [CONTRIBUTING.md](CONTRIBUTING.md). The initial material preparation is assisted work dated today, not evidence of earlier student contributions. Each student must inspect, understand and contribute to the materials, then record substantive revisions under their own account. The submission tag `pre-defense-1` must be created only after the agreed review; do not move a submitted tag.

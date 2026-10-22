# GEMZ Adaptive Roguelike

**Diploma project:** Design and evaluation of a player profiling and bounded enemy adaptation system in a 3D roguelike game.

GEMZ is a single-player expedition game in which a space miner explores alien caves, collects energy crystals and chooses whether to descend or extract. The game is an experimental environment for comparing static difficulty, rule-based adaptation and adaptation informed by a learned player profile.

## Problem and intended users

Fixed enemy behavior can become predictable, while aggressive difficulty changes can feel unfair. The engineering problem is to detect changes in combat style and respond within explicit timing, strength and performance limits. Intended users are PC action roguelike players; researchers and the supervisor use local experiment logs to assess the system. Improved enjoyment is a hypothesis, not an established project result.

## Team and supervision

| Member | Group | Proposed responsibility |
|---|---|---|
| Sailaubek Zhangir | SE-2429 | Gameplay loop, Unity scenes, enemy state machines and UX |
| Yessentemirov Yergun | SE-2418 | Telemetry, profiling, EAS controller and evaluation tooling |

The team agreed the responsibility split on 22 October 2026. Repository owner **gTurboflex** is **Yessentemirov Yergun, SE-2418**, confirmed by the owner. Supervisor: **Aigerim Bakiyeva**. Yergun uses YouTrack `admin`; Zhangir uses YouTrack `Zhangir` and GitHub `ynagi-1`. Both have project access. Supervisor and committee access still requires verification.

## Scope and current status

The original package was prepared on 21 October 2026. On 22 October the owner requested a split of future imports between individual accounts. This branch includes Yergun's reviewed analysis, architecture, reference controller and tests, plus the prepared protocol, HTML mock-up and pending walkthrough checklist imported under GEMZ-2/GEMZ-6 from Zhangir's handoff. Source inspection and controller verification are recorded separately from participant evidence and browser execution. The imports do not establish earlier independent student work. PR #2 records controller review and correction; PR #3 records the protocol and mock-up import review.

The draft history was reorganized on 22 October 2026 at the repository owner's request. The old release and tag are withdrawn. A new checkpoint version must be created after the individual contributions and reviews are accepted.

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
9. [User discussion protocol and unfilled evidence register](docs/09-user-evidence.md)
10. [Supervisor review record](docs/10-supervisor-feedback.md)
11. [Submission readiness checklist](docs/11-submission.md)
12. [Data dictionary](docs/12-data-dictionary.md)
13. [Architecture decision records](docs/adr/decisions.md)

[YouTrack project](https://gemz-diploma.youtrack.cloud/projects/GEMZ) · [Task list](https://gemz-diploma.youtrack.cloud/issues/GEMZ) · [Task board](https://gemz-diploma.youtrack.cloud/agiles/204-1/218-1). Eleven actual tasks, **GEMZ-1 through GEMZ-11**, have priorities, due dates, acceptance criteria and a PR link. On 22 October the assignees were verified as Yergun/admin: GEMZ-1, 3, 4, 5, 7, 8, 9, 11; Zhangir: GEMZ-2, 6, 10. All remain To do. Task assignment is not evidence of completion. See [assignment records](management/backlog.json).

## Run and check what exists

Download or clone this branch, extract the repository ZIP if needed, and open `prototype/index.html` from the repository root in a current desktop browser (for example, use File > Open in Chrome). The HTML is self-contained and needs no build step or server. Follow [the walkthrough checklist](docs/14-prototype-walkthrough.md) and record only actual results. All eight browser scenarios currently remain **Not run**, and the interview register is unfilled. The file is an imported offline scenario mock-up with simulated inputs; it is not Unity gameplay, measured telemetry or a trained classifier.

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
prototype/        Imported offline HTML mock-up; browser walkthrough Not run
docs/             Proposal, review, requirements, architecture, evaluation
diagrams/         Editable SVG and PlantUML sources, PNG exports
tests/            Controller contract tests
config/           Non-secret configuration example
management/       Task package and YouTrack setup status
scripts/          Materials integrity check
```

Use individual student accounts, real task branches, pull requests and another team member's substantive review. See [CONTRIBUTING.md](CONTRIBUTING.md). The initial materials were prepared on 21 October 2026, not evidence of earlier student contributions. Each student must inspect, understand and contribute to the materials, then record substantive revisions under their own account. The submission tag `pre-defense-1` must be created only after the agreed review; do not move a submitted tag.

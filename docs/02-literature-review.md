# Literature review and source register

## Scope and search approach

This initial critical review covers dynamic difficulty adjustment, lightweight player profiling and adaptation to changing data. Public publisher pages, author preprints, institutional records and official technical documentation were checked on **21 October 2026**. Search phrases included “dynamic difficulty adjustment systematic review”, “player modeling dynamic difficulty”, and “concept drift data streams”. Inclusion required a direct connection to adaptation design, evaluation or deployment. This is a targeted initial review, not a systematic review with an exhaustive search protocol.

The register contains **11 scientific sources** and **8 technical/product sources** used across this package. S1–S8 are journal or conference publications; S9 is a doctoral consortium abstract and S10–S11 are author preprints, so those three are supplementary evidence. Six of the eight core publications are from 2023–2025. The two 2021 papers are retained as implementation precedents. Access level is explicit below: an abstract-level assessment must not be represented as a full-paper replication or a complete quality appraisal.

## Structured analysis of scientific publications

| ID and publication | Approach and available evidence | Limitation for GEMZ | Design consequence |
|---|---|---|---|
| S1 Souza et al., 2025 | SLR of DDA implementations; publisher abstract reports 34 selected studies | Heterogeneous games and evaluation protocols; no direct estimate for this game; abstract and publisher sections consulted | Implement interchangeable strategies and compare them in one controlled testbed |
| S2 Mortazavi et al., 2024 | Review of performance, emotion and personality-based DDA; publisher abstract consulted | Search coverage ends in September 2022; reported benefits do not establish benefits for GEMZ | Measure both experience and objective outcomes; add newer primary work |
| S3 Lopes and Lopes, 2023, OL2A 2022 | Review of serious-game DDA including performance and physiological signals; abstract consulted | Rehabilitation objectives differ from recreational combat; physiological hardware is outside scope | Start with gameplay telemetry and avoid transferring clinical claims |
| S4 Ben Or et al., 2021 | Deep-learning DDA with gameplay and UX constraints; author abstract states CoG acceptance | Large-scale commercial context differs from a student dataset; abstract consulted | Put explicit constraints around adaptation rather than optimizing only a success proxy |
| S5 Huber et al., 2021 | Experience-driven generation in VR exergames with RL and an exploratory user study; author abstract and linked publication DOI consulted | VR exercise and level generation differ from enemy policy adaptation | Separate level generation from enemy adaptation and include subjective questionnaires |
| S6 Arora et al., 2024 | Review of concept-drift detection and adaptation in streaming data; publisher abstract consulted | Generic data streams do not identify the cause of a player's behavior change | Treat drift alarms as evidence of changed feature distributions, not proof of learning or intent |
| S7 Suárez-Cetrulo et al., 2023 | Review of recurring concepts and stream adaptation; institutional abstract consulted | Returning combat styles need not require retraining a classifier | Keep a fixed classifier and test fading profile memory first; record recurrent switches |
| S8 Komorniczak and Ksieniewicz, 2024 | Experiments with stream metafeatures on synthetic, semi-synthetic and real streams; abstract and introduction consulted | Metafeature usefulness on those streams is not demonstrated for short gameplay windows | Validate a small feature set and quantify detector false alarms before increasing complexity |
| S9 Biemer, 2023 | MDP director for platformer/roguelike generation; doctoral consortium abstract explicitly reports surrogate-agent evidence | Proposed player studies are future work in that abstract | Label bot evidence separately from evidence collected with humans |
| S10 Fuchs et al., 2024 | Two-agent imitation and reinforcement-learning DDA demo in a fighting-game environment; author preprint abstract consulted | A short demo is insufficient evidence of improved experience in a mining game | Consider as an alternative; do not add two-agent training to the MVP |
| S11 Rahimi et al., 2023 | Continuous RL DDA in a visual working-memory game; author abstract reports a within-subject comparison | Domain and action space differ; preprint status in the consulted record | Compare against rule-based adaptation and counterbalance condition order |

## Synthesis and engineering gap

DDA has multiple implementations rather than one universally superior method. S1–S3 motivate an explicit baseline and measurement of the intended experience. They do not support a claim that all adaptive games are more enjoyable. GEMZ therefore distinguishes two interventions: a threat-budget multiplier and the tactical composition of enemies.

S4–S5 illustrate that adaptation can be constrained and can affect different parts of a game. Changing room structure, spawn pressure, resistances and movement at once would make an experiment difficult to interpret. The first experiment will freeze room generation, cap resistance and apply strategy changes only at encounter boundaries. ML contributes a player-style estimate; the controller retains responsibility for admissible changes.

S6–S8 make a second distinction necessary: a shift in P(X) is not automatically a change in P(Y|X), nor proof that a player intentionally changed strategy. Without live labels, GEMZ can flag feature distribution changes and measure detection delay on scripted switches; it cannot claim that classifier accuracy has deteriorated in a live session. Offline labels and participant-separated evaluation address that separate question.

S7 also motivates testing a return to a previously used style. A fading probability profile can adapt without online retraining. Its update coefficient is not a learning rate for Random Forest or k-NN. This reduces runtime complexity, but may miss unusual hybrid styles. The Mixed class, confidence fallback and error analysis are needed to avoid confident overreaction.

The project-specific research question is whether this bounded combination is useful in the selected testbed under a small-data and frame-time budget. It does not establish a new general-purpose ML algorithm. S9–S11 provide comparison ideas while illustrating why surrogate, demo and different-genre evidence must be distinguished.

## Scientific references

- **S1** Souza, C. H. R.; Nascimento, D. F.; Berretta, L. O.; Carvalho, S. T. (2025). *Solutions for Dynamic Difficulty Adjustment in digital games: A Systematic Literature Review*. Entertainment Computing, 55, 101041. [Publisher and DOI](https://doi.org/10.1016/j.entcom.2025.101041).
- **S2** Mortazavi, F.; Moradi, H.; Vahabie, A.-H. (2024). *Dynamic difficulty adjustment approaches in video games: a systematic literature review*. Multimedia Tools and Applications, 83, 83227–83274. [Publisher](https://link.springer.com/article/10.1007/s11042-024-18768-x).
- **S3** Lopes, J. C.; Lopes, R. P. (2023). *A Review of Dynamic Difficulty Adjustment Methods for Serious Games*. OL2A 2022 proceedings, CCIS 1754, 144–159. Online publication 1 January 2023. [Publisher](https://link.springer.com/chapter/10.1007/978-3-031-23236-7_11).
- **S4** Ben Or, D.; Kolomenkin, M.; Shabat, G. (2021). *DL-DDA — Deep Learning based Dynamic Difficulty Adjustment with UX and Gameplay constraints*. Accepted to IEEE CoG 2021 according to the author record. [Author manuscript](https://arxiv.org/abs/2106.03075).
- **S5** Huber, T.; Mertes, S.; Rangelova, S.; Flutura, S.; André, E. (2021). *Dynamic Difficulty Adjustment in Virtual Reality Exergames through Experience-driven Procedural Content Generation*. IEEE SSCI. [Publication DOI](https://doi.org/10.1109/SSCI50451.2021.9660086); [author manuscript](https://arxiv.org/abs/2108.08762).
- **S6** Arora, S.; Rani, R.; Saxena, N. (2024). *A systematic review on detection and adaptation of concept drift in streaming data using machine learning techniques*. WIREs Data Mining and Knowledge Discovery, 14(4), e1536. [Publisher](https://doi.org/10.1002/widm.1536).
- **S7** Suárez-Cetrulo, A. L.; Quintana, D.; Cervantes, A. (2023). *A survey on machine learning for recurring concept drifting data streams*. Expert Systems with Applications, 213, 118934. [DOI](https://doi.org/10.1016/j.eswa.2022.118934); [institutional record](https://researchportal.uc3m.es/display/act560492).
- **S8** Komorniczak, J.; Ksieniewicz, P. (2024). *On metafeatures’ ability of implicit concept identification*. Machine Learning, 113, 7931–7966. [Publisher](https://link.springer.com/article/10.1007/s10994-024-06612-0).
- **S9** Biemer, C. F. (2023). *Dynamic Difficulty Adjustment via Procedural Level Generation Guided by a Markov Decision Process for Platformers and Roguelikes*. AIIDE, 19(1), 436–439, Doctoral Consortium Abstracts. [Publisher](https://ojs.aaai.org/index.php/AIIDE/article/view/27540).
- **S10** Fuchs, R.; Gieseke, R.; Dockhorn, A. (2024). *Personalized Dynamic Difficulty Adjustment — Imitation Learning Meets Reinforcement Learning*. arXiv preprint 2408.06818. [Author record](https://arxiv.org/abs/2408.06818).
- **S11** Rahimi, M.; Moradi, H.; Vahabie, A.-H.; Kebriaei, H. (2023). *Continuous Reinforcement Learning-based Dynamic Difficulty Adjustment in a Visual Working Memory Game*. arXiv preprint 2308.12726. [Author record](https://arxiv.org/abs/2308.12726).

## Technical and product references

- **T1** Unity. [Unity user manual](https://docs.unity3d.com/Manual/UnityManual.html). Supports the proposed Unity workflow; exact project version remains unpinned.
- **T2** Epic Games. [Blueprints overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine). Supports the C++/Blueprints alternative in the engine comparison.
- **T3** Godot. [Scripting documentation](https://docs.godotengine.org/en/stable/tutorials/scripting/index.html). Supports GDScript, C# and C++ alternatives.
- **T4** scikit-learn. [Trees](https://scikit-learn.org/stable/modules/tree.html), [ensembles](https://scikit-learn.org/stable/modules/ensemble.html), [neighbors](https://scikit-learn.org/stable/modules/neighbors.html). Supports candidate model behavior and implementation tradeoffs; no accuracy ranking is inferred.
- **T5** scikit-learn. [GroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html). Supports grouping evaluation by participant to avoid overlapping identities across folds.
- **T6** Ghost Ship Games / Coffee Stain. [Deep Rock Galactic official store description](https://store.steampowered.com/app/548430/Deep_Rock_Galactic/).
- **T7** Hopoo Games / Gearbox. [Risk of Rain 2 official store description](https://store.steampowered.com/app/632360/Risk_of_Rain_2/).
- **T8** Gunfire Reborn Studio / Duoyi. [Gunfire Reborn official store description](https://store.steampowered.com/app/1217060/Gunfire_Reborn/).

## Review work still required

Retrieve accessible full texts for the core sources through the university library or author repositories; extract datasets, sample sizes, measures and validity threats into this table before the final thesis. Do not copy inaccessible details from secondary summaries. Confirm citation style with the supervisor. The current review meets the numerical source selection target but remains an initial, partly abstract-based assessment.

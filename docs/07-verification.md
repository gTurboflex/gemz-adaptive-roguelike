# Verification and evaluation plan

The aim is to evaluate both engineering correctness and the usefulness of adaptation. Targets below are provisional pass criteria, not measured results. The current executable tests cover a reference controller only; Unity performance, ML accuracy and player experience remain unmeasured.

## Verification matrix

| Test | Method and condition | Expected evidence |
|---|---|---|
| T01 Gameplay scenarios | Easy and Hard: start, pause, mine, fight, descend, extract and fail | Screen recording and scenario checklist for FR01–FR03 |
| T02 Seeded generation | 100 seeds; graph reachability of extraction | Seed list, generator version and failure cases |
| T03 Telemetry | Known event replay, empty window, queue overflow, shutdown | Feature oracle fixture, bounded memory and dropped-event counter |
| T04 Classifier and export | Held-out participant folds; compact export versus Python predictions | Macro-F1, confusion matrix, per-class recall, latency and probability parity |
| T05 Controller contracts | Boundary values, negative/NaN inputs, Easy/Hard, pause and extreme DPS | EAS/difficulty bounds and slew-rate assertions |
| T06 Memory and change | Known switches and recurring styles; no-switch noisy controls | Time to dominant correct style; false alarms per minute |
| T07 Enemy behavior | Apply a queued adaptation during combat and then between waves | No mid-encounter mutation, resistance ≤25%, text warning |
| T08 Reproducibility | Same trace, seed, mode and artifacts; compare decisions | Matching controller decision sequence within 1e-6 |
| T09 Failure recovery | Missing/corrupt model, incompatible schema, old run, stale result and worker timeout | Static fallback with diagnostic; responsive game |
| T10 Data handling | Inspect sample exports and repository diff | Only approved pseudonymous records; no secrets or direct identifiers |
| T11 Usability | Task walkthrough at 720p and 1080p | Player can identify objective, Gemz amount, extraction and adaptation notice |
| T12 Performance | Fixed scene, seed, 1080p, declared machine; three 10-minute runs per mode after warm-up | p50/p95/p99 frame times, main-thread overhead, inference latency and allocation counts |

## Machine learning evaluation

Collect feature windows from consenting players using pseudonymous participant codes. Freeze the label rubric before labeling evaluation traces. Have two raters code at least 20% of windows and report agreement and resolution rules. Keep scripted synthetic traces in a separate dataset; they check mechanics, not human generalization.

Split by participant, never randomly by overlapping window: 20-second windows overlap and otherwise leak near-duplicate observations. Use grouped development cross-validation to choose features/hyperparameters, with preprocessing fitted only on training folds. Reserve a held-out participant test set when sample size allows; report explicitly if only cross-validation is feasible. Candidate models are Decision Tree, Random Forest and k-NN. Baselines are majority class and a frozen simple-rule classifier.

Initial acceptance target: macro-F1 ≥0.70 and improvement of ≥0.05 over majority class on held-out participants, with per-class results. These are engineering targets; small samples may make estimates unstable. Select the smallest model meeting the agreed accuracy and latency budget. Report classification errors and how the controller limits their impact.

For tactic-change traces, define detection delay as time from the scripted switch until the correct new style is dominant for two consecutive updates. Initial target: median ≤30 seconds and no-switch false alarms ≤1 per 5 minutes. Include the 20-second window's inherent delay. Test no-decay and fixed-decay ablations to isolate the variable update rate. The manually flagged reference demo cannot establish detector quality.

## Gameplay experiment

Conditions: A static enemies and EAS=1; B rule-based profiling with bounded EAS; C learned profiling with the same EAS and tactical limits as B. Use the same combat assets and seeded room sets. Starting difficulty is held constant within a participant or analyzed as a predeclared factor, rather than changed together with the condition.

Begin with a feasibility pilot, provisionally **12–18 consenting adult participants**, subject to supervisor and university approval. This is not a power calculation or a confirmed recruitment count. Provide a tutorial, then three short runs; counterbalance A/B/C order across participants and rotate matched seed sets. The separate 3–5 requirement discussions are not a substitute for this evaluation.

Primary experience measure: fairness rating on a predeclared 1–7 scale after each condition, with the same wording. Secondary measures: challenge, perceived predictability, enjoyment, completion, damage taken per active minute, extraction amount and number of voluntary tactic switches. A single custom item is not a validated psychometric instrument; use an approved validated questionnaire if the supervisor requires one and respect its usage terms.

Predeclare the principal paired contrast C versus B to test the learned profile, with C versus A as secondary. Report paired differences and participant-level confidence intervals. For a small ordinal pilot, emphasize distributions, effect sizes and qualitative comments; use an appropriate paired ordinal/nonparametric analysis if inferential testing is justified. Do not treat repeated windows as independent participants or report a significant result from a tiny pilot as general proof. A larger confirmatory sample needs a separate power analysis after variance estimates exist.

## Reproducibility and validity

Archive the build identifier, fixed commit/tag, machine CPU/GPU/RAM/OS, resolution/settings, seed list, condition order, model hash, feature schema, configuration and analysis procedure. Keep identifiable consent forms outside version control and study data access-controlled. Follow the university's approval and retention requirements; agree a retention period before recruitment and document deletion and withdrawal handling.

Threats include learning/fatigue, participant skill differences, imperfect labels, adaptation-induced feedback in telemetry, equipment changes, small sample size, subjective expectations and limited transfer from one map. Counterbalancing, grouped splits, fixed assets, trace replay, a blinded condition label where feasible and explicit limitations reduce these risks. No experiment outcome is currently available.

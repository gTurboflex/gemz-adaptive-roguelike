# Architecture and adaptation specification

The target architecture is an offline Unity game with a replaceable local inference component and separate offline model-training tools. The present Python reference model verifies selected controller contracts; none of the diagrams implies that Unity components already exist.

## Diagrams

- [System context PNG](../diagrams/context.png), [editable SVG](../diagrams/context.svg), [PlantUML source](../diagrams/context.puml)
- [Use case PNG](../diagrams/use-cases.png), [editable SVG](../diagrams/use-cases.svg), [PlantUML source](../diagrams/use-cases.puml)
- [Component draft PNG](../diagrams/components.png), [editable SVG](../diagrams/components.svg), [PlantUML source](../diagrams/components.puml)

SVG files are editable vector sources; PNGs are readable exports of those SVGs. PlantUML is an additional semantic source. If either source is changed, regenerate or update the corresponding views and inspect them for consistency.

## Components and execution boundaries

Gameplay publishes immutable combat and mining events through an Event Bus. A bounded queue feeds a worker that aggregates windows and invokes `IPlayerStyleClassifier`. It returns probabilities plus feature, model and run versions. The main-thread adaptation controller consumes only compatible, recent results. Unity scene objects are read or mutated on the main thread; background work uses snapshots, not Unity object references.

The controller converts the remembered style and EAS into a permitted next-encounter strategy. Enemy State machines execute movement and attacks; Strategy objects select ranged pressure, closing behavior or a limited resistance. Observer/Event Bus reduces direct dependencies, but subscriptions must be removed on scene teardown. Queue capacity, age checks, cancellation and model fallback must be tested rather than assumed to be fast.

Telemetry writer batches local JSONL records. Offline training reads approved study data, fits candidates and exports a versioned compact tree artifact. Exported values must pass Python/C# parity checks before they can enter a build. Raw study data is excluded from the repository.

## Features and model contract

Use a 20-second rolling window emitted every 5 seconds. Initial candidate features are combat-distance mean, close-range damage fraction, elemental damage fraction, dodge frequency, moving-time fraction, cover-time fraction, damage dealt per active combat second and damage taken per active combat second. Normalization and missing-data rules are in the [data dictionary](12-data-dictionary.md).

Provisional labels are Close, Ranged, Evasive and Mixed. Human coding uses replay context and a rubric rather than directly copying the same threshold used by the baseline. Two raters label a subset and resolve disagreements. Insufficient action evidence yields no new prediction; max probability below 0.6 yields no new specialized strategy. The live system receives no personality or intention labels.

## Threat budget and EAS

All coefficients below are initial hypotheses for tuning, not scientifically established constants. Let clamp(x,a,b) limit x to [a,b]. Let d be normalized depth, t=min(active run seconds/900,1), g=min(total mined Gemz/100,1), and p=clamp(DPS/30−1,0,1). Normalize depth by the configured maximum number of chambers. Spending crystals must not reduce g, so use cumulative mined Gemz rather than current inventory.

```text
EAS_target = clamp(1 + 0.35*d + 0.15*t + 0.15*g + 0.15*p, 1, 1.8)
B = 0.85 for Easy, 1.15 for Hard
EAS_next = move_towards(EAS_current, EAS_target, 0.02 * boundary_dt)
Difficulty = clamp(B * EAS_next, 0.75, 2.1)
```

`boundary_dt` is the duration of the current safe update interval, capped at 5 seconds per update; time spent fighting cannot be accumulated and applied as one large change. EAS remains unchanged during an encounter. A future threat-budget allocator will use Difficulty for spawn cost, not multiply health, damage, speed and count simultaneously. Static mode fixes EAS=1 and disables tactical adaptation; rule-based and ML modes share the EAS budget so their difference isolates the profile source. A further ablation can disable EAS while retaining the profile.

## Fading profile memory

For a valid probability vector P over the four styles and existing memory M:

```text
lambda = 0.015 + 0.035*(EAS−1)/0.8 + (0.03 if confirmed shift else 0)
alpha = 1 − exp(−lambda * profile_dt)
M_next = (1−alpha)*M + alpha*P
```

The exponential factor fades old probability mass while preserving a normalized vector. `profile_dt` is the actual update interval, at most 5 seconds. The coefficient is the **profile update rate**, not a gradient learning rate for a forest. Profiles are reset at run start. Per-run state is not silently transferred between study participants.

A planned distribution-change signal compares recent and reference feature histograms with Jensen–Shannon divergence; its threshold must be calibrated on no-switch and known-switch traces, and two consecutive flagged windows are required. The current reference demo accepts a manual `shift` flag; it does not implement this detector. A change signal accelerates memory turnover, not unrestricted enemy mutation.

## Guardrails and failure behavior

Resistance is capped at 25% and at most one specialization is selected for a wave. At low confidence, skip a new specialization and decay toward neutral; do not infer a confident style. An adaptation notice precedes a change. Last-valid inference older than 10 seconds, a worker error or a missing model uses static fallback with a diagnostic record. Current enemies do not instantly gain a counter during an attack.

Avoid a positive feedback loop: DPS contributes at most 0.15 to EAS; depth/time weights remain fixed during a condition. Report changing player equipment separately from changing player style. Record the chosen strategy, source profile, EAS, reason and application boundary for every update so a reviewer can reconstruct a decision.

## Planned interfaces

`CombatEvent → FeatureWindow → ProfilePrediction → ProfileMemory → AdaptationDecision → EnemyStrategy`.

Each message carries schema_version, run_id and monotonic timestamp. Prediction adds model_version and confidence. AdaptationDecision adds mode, EAS, difficulty, resistance_cap and reason. Boundary application rejects results for previous runs. Tests and data contracts are defined in the verification plan and data dictionary.

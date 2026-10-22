# Telemetry and model data dictionary

All fields below describe the planned schema v1. The reference controller does not collect gameplay data. Raw human traces, contacts and consent documents stay outside version control.

## Event envelope

| Field | Type / unit | Rule |
|---|---|---|
| schema_version | integer | Must equal 1 |
| run_id | random string | New per run; no account or machine identifier |
| participant_code | pseudonymous string or null | Experiment-only; linkage stored privately |
| time_s | monotonic seconds | Exclude paused time from active-run counters |
| event_type | enum | damage_dealt, damage_taken, dodge, movement, cover, gemz_mined, encounter_boundary |
| payload | object | Type-specific numeric values; no free-text personal fields |
| seed, build_version, config_version | integer / strings | Log at run start and include in exported manifest |

## Feature window

| Feature | Unit / definition | Missing data and normalization |
|---|---|---|
| mean_distance | metres during valid combat samples | No combat → no classification; clamp by declared sensor range |
| close_damage_fraction | Damage dealt at ≤5 m / all dealt damage | No damage → missing, not automatically zero |
| elemental_damage_fraction | Elemental damage / all dealt damage | Same missing rule; fraction in [0,1] |
| dodge_rate | Valid dodges / active combat seconds | Zero when combat exists but no dodge; upper bound set from mechanic cooldown |
| moving_fraction | Moving time / observed active combat time | Fraction in [0,1]; exclude paused samples |
| cover_fraction | Time with validated cover flag / active combat time | Requires a defined cover sensor; omit if that mechanic is not built |
| dps | Damage dealt / active combat seconds | Zero-damage combat allowed; clip only using training-fold thresholds |
| damage_taken_rate | Damage taken / active combat seconds | Log exposure and armor context to interpret differences |

Window length 20 s, stride 5 s. Require at least 10 s of valid active-combat coverage and 5 combat actions before classifying; tune these thresholds on development data. Fit any standardization or imputation only on training participants. The first deployment must version the exact feature order, units, normalization and missingness mask; silently substituting zero for missing measurements is prohibited.

## Predictions and controller state

`ProfilePrediction`: run_id, window_start_s, window_end_s, schema_version, model_version, probabilities [Close,Ranged,Evasive,Mixed], confidence=max(probabilities). Reject nonfinite/negative probabilities or a vector whose sum differs from 1 by more than 1e-6. Reject schema/run mismatches. A valid but low-confidence result is distinct from model failure.

`ControllerInput`: normalized depth, active seconds, cumulative Gemz mined, DPS, starting difficulty, safe-boundary flag and bounded update interval. Negative or nonfinite values are invalid. `AdaptationDecision`: EAS, difficulty, remembered probabilities, next-wave strategy, resistance cap, fallback flag and reason. Planned model artifacts also record training data version, grouped split procedure and test metrics; no artifact currently exists.

## Retention and reproducibility

Before recruiting, agree consent wording, access list, retention duration, withdrawal handling and the university approval route. Version the schema and analysis scripts in the repository; store consent forms and raw data separately with restricted access. Synthetic fixtures must be labeled synthetic and must never be counted as participant data.

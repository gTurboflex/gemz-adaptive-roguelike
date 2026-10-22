# Technology comparison and decisions

The alternatives below address four key decisions. Qualitative costs are project estimates, not measured benchmarks. Selected technologies are provisional until a small integration spike passes; the user has selected Unity/C# as the intended game stack.

## Game engine

| Alternative | Fit for this project | Cost and limitation | Decision |
|---|---|---|---|
| Unity with C# and URP [T1] | Component-oriented 3D workflow; matches the requested language | Must pin editor and packages; threading cannot mutate scene objects directly | Selected; initialize one test scene before content production |
| Unreal Engine with C++ and Blueprints [T2] | Visual scripting and C++ integration support complex 3D behavior | Additional C++/Blueprint workflow and build complexity for this team are a planning risk | Reserve alternative if the team already has stronger Unreal expertise |
| Godot with C# or GDScript [T3] | Scene/node approach with supported scripting choices | Requires a separate validation of the proposed C# inference integration and export | Feasible alternative; not selected to avoid changing the chosen stack |

Selection does not claim one engine has universally better performance. Visual simplicity and a small asset budget matter more than unmeasured engine comparisons here.

## Player style classification

| Alternative | Strength | Limitation and necessary check | Role |
|---|---|---|---|
| Decision Tree [T4] | Inspectable rules, small export and straightforward C# traversal | High variance and axis-aligned boundaries; tune depth on development folds | First deployable candidate |
| Random Forest [T4] | Can reduce variance relative to a single tree | Larger model; benchmark size and inference time rather than assuming superiority | Main accuracy challenger |
| k-NN [T4] | Simple training procedure and a useful distance-based baseline | Scaling and stored reference data matter; inference work grows with retained samples | Comparison candidate |

Use identical feature definitions and participant-separated splits [T5]. Select by macro-F1, per-class recall, inference latency and export complexity. None of these candidates has the gradient-learning-rate mechanism described in the original concept; EAS will control the rate of profile updating, not the model-training rate.

## Runtime inference integration

| Alternative | Advantage | Cost or failure mode | Decision |
|---|---|---|---|
| Compact versioned tree JSON with C# traversal | Local, inspectable, no live Python dependency | Requires model-export parity tests and schema validation | Proposed MVP path for tree models |
| ONNX runtime integration | Standard model interchange when converter/runtime support matches | Additional package and operator/version compatibility checks | Revisit if measured model complexity justifies it |
| Local Python HTTP service | Rapid model iteration independent of Unity | Process startup, transport, timeouts and packaging introduce avoidable runtime dependencies | Development experiment only; exclude from the shipping MVP |

## Telemetry storage

| Alternative | Advantage | Limitation | Decision |
|---|---|---|---|
| Buffered JSON Lines | Human-readable append-only events; easy scripted replay | Needs schema versions, file rotation and partial-line recovery | Selected for the first local experiment |
| SQLite | Structured queries and transactional storage | Database integration and schema migration cost | Add if multi-session query needs outgrow files |
| Remote database/service | Centralized experiment aggregation | Network, consent, account and deployment requirements | Excluded from the MVP |

Primary technical references T1–T5 are in the [source register](02-literature-review.md). Exact version choices and compatibility results will be recorded in configuration files and [ADRs](adr/decisions.md), not inferred from whichever documentation version is current.

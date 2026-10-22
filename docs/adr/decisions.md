# Initial architecture decision records

## ADR 001 Unity and offline inference

Status: proposed implementation, Unity/C# selected by the project owner. Context: the project needs a small 3D testbed and predictable local execution. Decision: use Unity/C# and initially evaluate a compact tree model loaded locally. Alternatives: Unreal, Godot, ONNX integration and a Python service are compared in the technology document. Consequence: implement and test export parity; do not assume all scikit-learn models can be deployed with the same exporter. Revisit if the Unity spike or accuracy/latency tradeoff fails.

## ADR 002 Separate profile learning from difficulty control

Status: proposed. Context: player style, combat skill and world progression are different variables. Decision: freeze the supervised classifier during a run, update an exponential probability memory, and let bounded EAS control the threat budget and memory turnover. Consequence: online weight training is outside scope; unknown styles and data shifts need confidence fallback and offline error analysis. Revisit after a labeled pilot, not on the basis of the synthetic demo alone.

## ADR 003 Apply changes at encounter boundaries

Status: proposed. Context: sudden counters can invalidate an action after the player commits to it. Decision: queue tactical changes, cap resistance and announce the next encounter's change; do not mutate current enemies in the middle of combat. Consequence: adaptation is delayed, which must be included in response-time measurements. Revisit only after fairness feedback and explicit supervisor agreement.

## ADR 004 Local buffered JSONL for experimental records

Status: proposed. Context: the MVP has no online service and needs auditable trace replay. Decision: use schema-versioned local events with bounded buffering and opt-in study exports. Consequence: log rotation, partial writes and participant privacy still require implementation and tests; raw study records stay outside Git. Revisit if file-based querying becomes the limiting factor.

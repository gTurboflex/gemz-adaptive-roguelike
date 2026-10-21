# Initial requirements and acceptance criteria

Priorities use Must, Should and Could. These are design requirements, not statements of implementation. Tests T01–T12 and ownership roles are defined in the verification and management documents. All numeric thresholds are provisional engineering targets for supervisor and pilot review.

## Functional requirements

| ID | Priority | Requirement | Acceptance criterion | Verification |
|---|---|---|---|---|
| FR01 | Must | Prepare a single-player run | Player can choose Easy or Hard, start, pause and restart; chosen mode is logged | T01 |
| FR02 | Must | Mine and extract Gemz | A crystal increases inventory once; extraction ends the run with the correct retained amount | T01 |
| FR03 | Must | Support combat variation | Two damage types and three enemy archetypes have observable, documented behaviors | T01 |
| FR04 | Must | Provide repeatable cave routes | Same seed and generator version reproduce room layout; an extraction path is reachable in 100 seeded generation checks | T02 |
| FR05 | Must | Collect a bounded telemetry stream | Events create 20-second feature windows every 5 seconds; feature calculations match a labeled replay fixture | T03 |
| FR06 | Must | Infer player style | Output covers Close, Ranged, Evasive and Mixed with probabilities and version; confidence below 0.6 prevents a new specialized tactic | T04 |
| FR07 | Must | Compute bounded EAS | EAS stays in [1.0,1.8], difficulty in [0.75,2.1], and EAS changes by at most 0.02 per second of boundary-update time | T05 |
| FR08 | Must | Fade profile memory | After a scripted style switch, old probability mass decreases and the new dominant style is detected under the documented delay criterion | T06 |
| FR09 | Must | Apply fair enemy changes | Strategy changes occur at encounter boundaries; resistance never exceeds 25%; no damage type becomes fully ineffective | T07 |
| FR10 | Must | Compare experimental modes | Static, rule-based and ML-profile modes use the same seed/configuration and report their mode in each run | T08 |
| FR11 | Must | Recover from unavailable inference | Missing, invalid or incompatible model selects documented static fallback; gameplay remains responsive | T09 |
| FR12 | Must | Export evaluation data | Opt-in logs include pseudonymous participant code, condition, seed and build/model/config versions without names or account details | T10 |
| FR13 | Should | Explain adaptation | A readable HUD notice identifies the next wave's tactical change before it is applied | T11 |
| FR14 | Should | Separate settings from implementation | A validated configuration can change bounds and weights; invalid values fail safely | T05 |
| FR15 | Could | Offer optional cel shading | Style remains readable with the effect disabled; it does not block the experiment | Visual review |

## Nonfunctional requirements

| ID | Priority | Requirement and acceptance criterion | Verification |
|---|---|---|---|
| NFR01 | Must | On a declared Windows test machine at 1080p and a fixed scene load, adaptation adds at most 1 ms to p95 main-thread frame time relative to static mode across three 10-minute runs | T12 |
| NFR02 | Must | At most 10000 queued events; overflow increments a visible diagnostic counter and drops oldest data; worker failure cannot block the Unity main thread | T03/T09 |
| NFR03 | Must | At least 95% of 5-second profile-update cycles finish within 50 ms on the declared machine; the last valid profile may be reused for at most 10 seconds | T12/T09 |
| NFR04 | Must | No passwords, tokens, raw study consent records or direct participant identifiers are stored in version control | T10 and repository review |
| NFR05 | Must | A recorded seed, mode, artifact versions and input trace reproduce controller decisions within floating-point tolerance; exact full-physics determinism is not promised | T08 |
| NFR06 | Should | UI remains readable at 1280×720 and 1920×1080; adaptation notices use text as well as color | T11 |
| NFR07 | Must | Feature/model schema mismatch is rejected; an export parity fixture produces matching Python/C# probabilities within 1e-6 | T04/T09 |

## Priority rationale and traceability

FR05–FR11 and NFR01–NFR05 protect the research validity and runtime safety; decorative content is lower priority. FR01–FR04 provide the smallest loop that makes the experiment interpretable. User interviews may revise these priorities; no requirement is currently labeled user-validated.

UC1 Prepare run → FR01. UC2 Mine and survive → FR02–FR05. UC3 Respond to adaptation → FR06–FR09, FR13. UC4 Extract → FR02. UC5 Configure and evaluate → FR10–FR12, FR14. Components and diagrams use these same names. PLAN04 covers requirements, PLAN05 architecture, PLAN06 prototype, PLAN09 profiling, PLAN10 Unity integration and PLAN11 evaluation in the prepared task package.

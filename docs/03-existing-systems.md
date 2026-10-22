# Existing systems comparison

Three relevant systems are compared against eight common criteria. The purpose is to identify design precedents, not to claim that GEMZ is commercially superior. Evidence is limited to the developers' official store descriptions checked on 21 October 2026. **ND** means not documented in the consulted source, not absent from the game. User tags and review scores are not used as proof of implementation.

| Criterion | Deep Rock Galactic [T6] | Risk of Rain 2 [T7] | Gunfire Reborn [T8] | GEMZ planned scope |
|---|---|---|---|---|
| Single-player option | Listed | Listed | Explicitly described | Required |
| Co-op option | 1–4 players | Listed | Up to four players | Excluded |
| Combat presentation | FPS | Third-person shooter in official feature context | FPS | 3D; perspective to confirm |
| Resource extraction theme | Space mining and mineral collection | Alien-planet survival and loot | Adventure and weapons | Gemz mining and extraction |
| Procedural environments | Explicitly described | Randomized stage/encounter content described | Procedurally generated levels | Seeded modular cave route |
| Destructible terrain | Explicitly described | ND | ND | Excluded; mineable crystal nodes only |
| Character/build variety | Class-based miner roles described | Characters and combinable loot | Hero abilities and weapons | One miner, limited upgrade choice |
| Published per-player ML adaptation and reproducible evaluation | ND | ND | ND | Explicit experimental objective; not implemented yet |

## Design conclusions

Deep Rock Galactic is the closest thematic precedent: mining, caves and alien threats. Reproducing its destructible world and co-op structure would exceed the proposed scope. GEMZ takes the extraction decision as a scenario and uses a smaller environment to isolate adaptation.

Risk of Rain 2 is relevant to replayable combat and build variation. Its official description supports randomized encounters and loot, but this comparison does not infer the internal difficulty formula or a player-specific learning system. GEMZ must document its own formula and evaluate it separately.

Gunfire Reborn demonstrates the combination of FPS combat, roguelite progression and procedural levels. It supports using stylized combat with a limited set of builds as a useful reference, but does not validate GEMZ's profiling hypothesis.

The gap is an **inspectable experimental implementation** with versioned profiles, bounded updates and a reproducible evaluation protocol. The consulted descriptions cannot establish that commercial games lack similar internal techniques. The project is justified as a software-engineering investigation, not by an unsupported market-first claim.

Sources T6–T8 are linked in the [source register](02-literature-review.md). A later comparison should add structured play observations, dates, build versions and evidence for any difficulty-mechanism claim.

# Artifact / Evidence Migration Policy

The artifact inventory exists to make legacy research safer to organize. Inventory and classification happen before any relocation.

## Migration states

- **PRIMARY EVIDENCE — DO NOT MOVE YET** — likely source/challenge/original evidence. Preserve path until a case records provenance and references.
- **DUPLICATE** — byte-identical SHA-256 group. Do not delete automatically; identify the canonical retained copy and references first.
- **GENERATED OUTPUT** — derived analysis output such as bitplanes or extracted binary data. Keep reproducibility notes and link to the generating tool/case before consolidation.
- **NEEDS CASE LINK** — artifact is not attached to a structured case. Establish context/ownership before moving.
- **UNKNOWN PROVENANCE** — repository artifact whose origin and role are not yet clear. Investigate before relocation.
- **SAFE TO ORGANIZE** — artifact is linked to a structured case and can be moved only through a reviewed migration that preserves hashes/references.

## Rules

1. Run `python scripts/artifact_inventory.py scan` before planning moves.
2. Preserve SHA-256 and old path in the migration record.
3. Never auto-delete duplicates.
4. Never move primary evidence based only on filename heuristics.
5. Generated outputs should record the tool/command/input that can reproduce them when known.
6. Every migrated artifact should end up linked to a structured case or documented research collection.
7. After a move, rebuild the inventory and verify hashes did not change.

## Current legacy observations

The existing repository contains large root-level challenge/evidence files plus derived binary outputs and a `bitplanes/` collection. The Git tree already shows some bitplane files sharing identical blob identities across channels, confirming real duplicate groups. These should be reviewed as generated duplicates rather than deleted automatically.

The first cleanup target is therefore metadata and linkage, not file deletion: protect likely primary challenge evidence, attach derived outputs to the relevant case, identify canonical copies for duplicate groups, and only then prepare an explicit move plan.

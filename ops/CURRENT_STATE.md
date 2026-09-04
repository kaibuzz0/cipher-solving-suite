# Current Repository State

Last reconciled: 2026-09-04 07:40 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `a88d32bc6fc56c8f11b34fb300a34f2fa8dea7c4`, the merge of PR #129 (`Build: reconcile Aug 28 afternoon source fingerprints`).
- PR #127 advanced canonical source history through Aug. 28 morning. Its final head `3a73d461933f9064f61da3b83d9d1fcf01e71ca7` passed Core `33848641904`, Intelligence Source Report `33848641950`, and Daily Repository Maintenance `33848641922`; the inspected Python 3.12 matrix ran 79/79 tests passing.
- PR #128 reconciled post-replay coordination and merged as `388e8a6d131e0215d643f8a22a3f4bb394bffdff`. Exact-merge Core `33849314242` and Deploy operations dashboard `33849314241` succeeded.
- PR #129 preserves the Aug. 28 afternoon raw snapshot unchanged and adds a separate provenance reconciliation plus regression coverage. Final head `4e7c1815556100e55f70ff36b68fe49049d8dc84` passed Core `33849585386` on Python 3.11/3.12/3.13 and Daily Repository Maintenance `33849585389`; the inspected Python 3.12 job ran 81/81 tests passing.
- No open repository issue currently blocks the chronological source-replay lane.
- An independent public Pages browser render was unavailable in this runtime. Release-health claims are therefore limited to observed successful deployment workflow evidence.

## Build / integration state

- Canonical source history still extends through Aug. 28 morning at `2026-08-28T07:40:27Z`. PR #129 is reconciliation only and did not advance history or registry freshness.
- The original invalid-hash morning and afternoon raw snapshots remain preserved unchanged.
- `intelligence/feeds/2026-08-28-afternoon-source-health-reconciled.json` is now the sole eligible Aug. 28 afternoon replay surface. It preserves the contributed observation strings and original hashes and records independently recomputed canonical fingerprints:
  - `ctftime-upcoming`: corrected `8ab1541b75153d193963da65855a7c07f99bf9a26bf701b45b1fbc754272a19b`; exact latest canonical predecessor `ab0660900275cf3767cd9b2f49f4bd08c2c0e2f68fa6f074ae1f2f55e66b380f`.
  - `github-search`: corrected `db0ecb913bc55b1de3b637f97325c14ac439c4531e7494144a8db792c457622b`; exact latest canonical predecessor `993f3601dafc2f452f9267c79a861f1e4de5e33e0065e7be100191cdd95dcca9`.
- PR #129 regression coverage requires exact raw observation preservation, original-hash preservation, corrected-hash recomputation, exact predecessor matching, absence of premature canonical afternoon records, and a non-mutating two-observation dry-run replay.
- The first PR #129 Core run failed because the new test incorrectly treated `result["replayed"]` as a list of source-ID strings; the replay engine actually returns record dictionaries. The assertion was corrected to compare each record's `source_id`. No provenance or verification assertion was removed, and the corrected head then passed all required validation.
- The exact next canonical integration is a separate bounded replay of the reconciled Aug. 28 afternoon snapshot. Only the two verified records above may be added at `2026-08-28T19:37:39Z`, and only `ctftime-upcoming` / `github-search` registry timestamps may advance.
- Aug. 29 and all later research remain chronology-blocked until that afternoon replay is independently green and merged.

## Current research / intelligence state

- Independent source recheck supports the material COMPFEST schedule observation: CTFtime records an extension from 24 to 48 hours because of ASIS CTF / BlackHat MEA qualifier collisions, while the official COMPFEST mirror host gives Aug. 29 00:00 UTC through Aug. 31 00:00 UTC. The official host is the stronger event-specific timing source.
- `skyf0l/RsaCracker` remains an evaluation lead, not an imported or mature repository tool. Current public documentation supports RSA key/cipher analysis, targeted and multi-key attacks, partial-prime wildcard recovery, Cargo/Docker use, rug/GMP dependency considerations, and dual Apache-2.0/MIT licensing. Deterministic fixture, overlap, dependency/supply-chain, I/O, and reproducibility review remain required before adoption.
- Later open research lanes remain PR #103 (Aug. 31 morning), PR #106 (Aug. 31 afternoon), PR #109 (Sep. 1 morning), PR #112 (Sep. 1 afternoon), PR #116 (Sep. 2 morning), PR #120 (Sep. 2 afternoon), PR #123 (Sep. 3 morning), and PR #125 (Sep. 3 afternoon). They remain contributed/noncanonical evidence and must be reconciled only at their chronology point.
- Careers in Your Community remains specialized school/team opportunity intelligence, not generic individual work.
- xTech|Search 10 remains non-actionable until authoritative Army/RFI/application evidence resolves conflicting official date/state surfaces.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain preservation debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Canonical tools, toolsets, cases, source health, repository data, and Agent Operations continue to flow through registries/manifests/site-data builders rather than bespoke HTML.

## Security / maintenance state

- Bounded default-branch searches in this run found no indexed `shell=True`, `os.system(`, or `subprocess` matches; this is a targeted check, not a complete security audit.
- Fresh PR #129 validation retained the artifact inventory at 40 items, 10 duplicate groups, 11 orphaned items, 12 generated outputs, 7 items needing case links, 1 protected primary-evidence item, and 0 unknown-provenance items.
- Known root-generated 310 artifacts remain warnings and were left untouched.
- Workflow dependencies remain bounded but not fully immutable: Actions workflows use major tags such as `actions/checkout@v4`, `actions/setup-python@v5`, and `actions/upload-artifact@v4`, while Python test dependencies use bounded version ranges. GitHub Actions currently emits Node runtime deprecation / forced-Node-24 warnings for these actions. Treat immutable action pinning/runtime migration and lockfile strategy as supply-chain hardening debt, not a release blocker for the verified reconciliation.
- No primary research artifact was deleted, moved, or rewritten in this pass.

## Known state / debt

- `data/integration_queue.json` remains semantically correct with Aug. 28 as `needs-integration`, but its detail text predates PR #129 and should be refreshed when the afternoon replay is staged or after it merges; do not rewrite older queue history merely for prose freshness.
- `docs/AGENT_HANDOFF.md` is append-only and materially behind current state. The available connector replaces the complete journal rather than atomically appending; do not risk truncating historical entries. Preserve the exact intended append in the coordination PR until an append-capable mutation is available.
- Later raw research must be reconciled only when chronology reaches it. External 310 provenance, root-artifact relocation, immutable Actions/dependency hardening, and direct public Pages render verification remain separate debt.

## Current operating priorities

1. Create a separate replay branch from current main using `intelligence/feeds/2026-08-28-afternoon-source-health-reconciled.json`; do not modify either raw Aug. 28 snapshot or the reconciliation metadata.
2. Add exactly two `2026-08-28T19:37:39Z` canonical history records using corrected fingerprints `8ab1541b...` and `db0ecb91...` with the exact predecessors above.
3. Advance only `ctftime-upcoming` and `github-search` registry `last_checked_at` values; do not promote RsaCracker into the tool registry as part of source replay.
4. Update the reconciliation regression from pre-replay dry-run expectations to canonical uniqueness/idempotence expectations without weakening provenance checks.
5. Require green source-history, registry, collection report, intelligence, site-data/Agent Operations, Core, Intelligence Source Report, and Daily Maintenance validation before merge.
6. Continue Aug. 29 → Aug. 30 → Aug. 31 → Sep. 1 → Sep. 2 → Sep. 3 strictly in timestamp/source-overlap order.

## Coordination note

This run advanced canonical history through Aug. 28 morning via PR #127, reconciled repository coordination via PR #128, then independently detected that both hashes in the Aug. 28 afternoon raw snapshot were invalid. Rather than silently correcting evidence, PR #129 added a separate provenance-preserving reconciliation and a regression that verifies raw preservation, corrected fingerprints, exact predecessors, and non-destructive replay readiness. No raw evidence, opportunity/case status, security authorization, tool maturity, or bespoke site HTML was changed by PR #129.

## Next handoff

Repo Integrity / Build Integration should replay `intelligence/feeds/2026-08-28-afternoon-source-health-reconciled.json` next. Add only the two verified 19:37:39Z records, advance only their matching source-registry timestamps, preserve RsaCracker as an evaluation lead, update the reconciliation test to require canonical idempotence, and require the full validation stack before Aug. 29 can advance.

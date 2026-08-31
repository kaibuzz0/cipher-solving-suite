# Current Repository State

Last reconciled: 2026-08-31 03:32 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `19de1f0d16daa546fbc67fb737f3dc9d33d46812`, the merge of PR #101 (`Build: reconcile Aug27 source fingerprints without rewriting evidence`).
- PR #101 exact head `55ece8bed635a40354b4245e2a1bb1c7adf0442d` passed Core validation `33332672382` and Daily Repository Maintenance `33332672415` before merge.
- Post-merge Core validation `33354005044` and Deploy operations dashboard `33354005008` both succeeded on exact merge commit `19de1f0d...`.
- No open pull requests or open issues were found at this reconciliation point.
- Source-health observations through Aug. 26 remain canonical. Aug. 27 and later raw research has not been replayed canonically.

## Build / integration state

- PR #101 resolved the Aug. 27 fingerprint-provenance blocker without modifying the original PR #75 raw snapshot. `intelligence/feeds/2026-08-27-source-health.json` remains preserved unchanged.
- `intelligence/feeds/2026-08-27-source-health-reconciled.json` is now canonical contributed evidence. It preserves the exact PR #75 observation strings, records all five original contributed hashes, and supplies only the independently recomputed canonical fingerprints in a separate derived replay surface.
- `tests/test_aug27_source_reconciliation.py` verifies original-vs-derived observation identity, preservation of original hashes, exact corrected hashes, Aug. 26 predecessor links, all-five `changed` classification, direct-script dry-run behavior, and non-mutation of history/registry fixtures.
- Canonical Aug. 27 replay has **not** occurred. `data/source_check_history.json` and `data/intelligence_sources.json` remain intentionally unchanged by PR #101.
- The integration queue and work queue still contain pre-PR101 wording that describes the reconciliation itself as pending. Treat that wording as coordination drift; the next source-history action is a separate bounded canonical replay of the reconciled Aug. 27 snapshot.
- Raw later research is already preserved on `main`: PR #82 (Aug. 28 morning/afternoon), PR #85 and PR #91 (Aug. 29 morning/afternoon), and PR #95 and PR #99 (Aug. 30 morning/afternoon). None may overtake the Aug. 27 canonical replay gate.

## Current research / intelligence state

- Canonical source history is current through Aug. 26 only.
- The Careers in Your Community Challenge remains specialized school/team opportunity intelligence, not generic individual work.
- xTech|Search 10 remains non-actionable until authoritative RFI/application evidence resolves conflicting official date surfaces.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.
- Aug. 28+ research remains contributed evidence until chronology, fingerprint/predecessor validation, and normal source verification are satisfied.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`.
- PR #101 introduced no new tool/toolset registration and no bespoke website HTML.
- Canonical discovery contracts remain unchanged: tools, toolsets, cases, intelligence, evidence, repository data and Agent Operations should flow through canonical registries/manifests/site-data builders.

## Known state / debt

- Reconcile `data/integration_queue.json` and `docs/WORK_QUEUE.md` from the pre-PR101 blocker wording to the post-PR101 replay-ready state without deleting historical provenance.
- Canonically replay the reconciled Aug. 27 snapshot in a separate bounded PR, advancing only the five matching registry timestamps after exact predecessor/hash verification.
- Process Aug. 28, Aug. 29 and Aug. 30 raw research only after Aug. 27 becomes canonical, in timestamp order.
- Daily maintenance continues to report known root-generated artifact debt; migration must preserve hashes, references and provenance.
- External provenance/authenticity for `310_challenge.png` remains unresolved.
- Workflow actions use supported major tags and Python CI uses bounded ranges rather than immutable action SHAs/a full lockfile; treat this as non-blocking supply-chain hardening debt.

## Current operating priorities

1. Update the integration/work queues so PR #101's reconciliation is recorded as merged and Aug. 27 canonical replay is the active integration step.
2. Replay `intelligence/feeds/2026-08-27-source-health-reconciled.json` with the canonical `source-history replay-snapshot` dry-run/write workflow in a separate bounded PR.
3. Require exactly five Aug. 27 history records with the reconciled hashes and verified Aug. 26 predecessor chain; advance only matching source-registry timestamps.
4. Rerun source-history/registry/report/intelligence/site-data/Agent Operations/Core/Maintenance validation before merge.
5. Only afterward process Aug. 28 morning/afternoon, Aug. 29 morning/afternoon, then Aug. 30 morning/afternoon research chronologically.
6. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

PR #101 is now merged and release-healthy. The raw PR #75 file remains primary contributed evidence and was not rewritten. The reconciled Aug. 27 file is explicitly derived evidence, not a retroactive claim that the original hashes were valid. Later research-only merges are preserved but chronology-blocked. No concurrent open PR or issue currently owns the shared coordination files.

## Next handoff

Repo Integrity / Build Integration should first reconcile the machine-readable and human work queues to this post-PR101 truth, then create a separate bounded Aug. 27 canonical replay PR. Do not replay Aug. 28+ research until the Aug. 27 replay is independently verified and merged.

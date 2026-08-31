# Current Repository State

Last reconciled: 2026-08-31 19:18 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `ac6cbdd0b1fc55877059a3c4eeed70bbc5e42081`, the merge of PR #104 (`Ops: preserve green post-PR101 coordination state`).
- PR #104 reused exact tested head `e2c6387e0217849ac91aed56c768277ceb7bcc95`; that head passed Core validation `33368866440` and Daily Repository Maintenance `33368866320` before merge.
- Post-merge Core validation `33371070197` and Deploy operations dashboard `33371070306` both succeeded on exact merge commit `ac6cbdd0...`.
- Scheduled Daily Repository Maintenance `33417471138` and Intelligence Source Report `33420964502` also succeeded on exact current `main`.
- Exactly one open pull request was found: PR #103 (`Research: preserve Aug 31 source health and agent-evidence paper`). It is a one-file raw-research contribution, is reported mergeable, and its exact head `6db8716645ddd44e5f944fbbd31b4d2e3ccaf05a` passed Core validation `33369490812`. Its base predates PR #104, so treat it as contributed/noncanonical evidence and reconcile current `main` before integration.
- No open issues were found.
- Source-health observations through Aug. 26 remain canonical. Aug. 27 and later raw research has not been replayed canonically.

## Build / integration state

- PR #104 merged the post-PR101 coordination reconciliation without changing canonical source history, registry freshness, primary evidence, tools/toolsets, cases, 310 claims, or bespoke website HTML.
- PR #101 previously resolved the Aug. 27 fingerprint-provenance blocker without modifying the original PR #75 raw snapshot. `intelligence/feeds/2026-08-27-source-health.json` remains preserved unchanged.
- `intelligence/feeds/2026-08-27-source-health-reconciled.json` is the eligible derived replay surface. It preserves the exact PR #75 observation strings, records all five original contributed hashes, and supplies independently recomputed canonical fingerprints separately.
- Canonical Aug. 27 replay has **not** occurred. `data/source_check_history.json` and `data/intelligence_sources.json` remain intentionally unchanged beyond Aug. 26.
- `data/integration_queue.json` and `docs/WORK_QUEUE.md` now correctly identify the separate bounded Aug. 27 canonical replay as the active source-history step and preserve Aug. 28-Aug. 30 as chronology-blocked research.
- Open PR #103 adds only `intelligence/feeds/2026-08-31-source-health.json`. It does not advance canonical history, registry timestamps, intelligence, opportunities, cases, coordination files, or website markup. Its research claims remain contributed evidence pending independent verification and chronological integration.

## Current research / intelligence state

- Canonical source history is current through Aug. 26 only.
- The Careers in Your Community Challenge remains specialized school/team opportunity intelligence, not generic individual work.
- xTech|Search 10 remains non-actionable until authoritative RFI/application evidence resolves conflicting official date surfaces.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.
- Raw later research is preserved on `main`: PR #82 (Aug. 28 morning/afternoon), PR #85 and PR #91 (Aug. 29 morning/afternoon), and PR #95 and PR #99 (Aug. 30 morning/afternoon). PR #103 contributes Aug. 31 raw research but is not merged as of this reconciliation.
- Aug. 28+ research remains contributed evidence until chronology, fingerprint/predecessor validation, and normal source verification are satisfied.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`.
- No new tool/toolset registration or bespoke website HTML was introduced by PR #104 or open PR #103.
- Canonical discovery contracts remain unchanged: tools, toolsets, cases, intelligence, evidence, repository data and Agent Operations should flow through canonical registries/manifests/site-data builders.
- Current-main Core validation exercises the existing generated site-data, Agent Operations, tool visibility, source/data validation and compileability contracts; the exact merge commit is green.
- The GitHub connector did not expose the Pages REST state endpoint in this pass. Release-health evidence is therefore the successful exact-commit `Deploy operations dashboard` workflow, not a separate direct Pages API/browser assertion.

## Known state / debt

- Canonically replay the reconciled Aug. 27 snapshot in a separate bounded PR, advancing only the five matching registry timestamps after exact predecessor/hash verification.
- Process Aug. 28, Aug. 29, Aug. 30 and then Aug. 31 raw research only after Aug. 27 becomes canonical, in timestamp/source-overlap order.
- PR #103 is based on pre-PR104 `main`; preserve its one-file research contribution but reconcile/recheck it against current `main` before merge rather than treating its earlier base snapshot as repository truth.
- Daily maintenance continues to report/contain known root-generated artifact debt; migration must preserve hashes, references and provenance.
- External provenance/authenticity for `310_challenge.png` remains unresolved.
- Workflow actions use supported major tags and Python CI uses bounded ranges rather than immutable action SHAs/a full lockfile; treat this as non-blocking supply-chain hardening debt.
- A bounded indexed-code search for `shell=True` returned no matches in this pass; this is not a complete security audit.

## Current operating priorities

1. Replay `intelligence/feeds/2026-08-27-source-health-reconciled.json` with the canonical `source-history replay-snapshot` dry-run/write workflow in a separate bounded PR.
2. Require exactly five Aug. 27 history records with the reconciled hashes and verified Aug. 26 predecessor chain; advance only matching source-registry timestamps.
3. Rerun source-history/registry/report/intelligence/site-data/Agent Operations/Core/Maintenance validation before merge, then require independent integrity verification.
4. Only afterward process Aug. 28 morning/afternoon, Aug. 29 morning/afternoon, Aug. 30 morning/afternoon, then Aug. 31 research chronologically.
5. Reconcile PR #103 onto current `main` before integration and keep its preprint/source claims at contributed-research status until independently verified.
6. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

PR #104 is merged and release-green on current `main`. It corrected the machine-readable/human queues after PR #101 but naturally made its own embedded `current main` statement stale once merged; this integrity pass corrects that post-merge truth without reopening the already-settled source chronology. PR #103 is concurrent but non-overlapping: it owns one Aug. 31 raw research file and does not touch shared coordination state. No compatible research is being discarded and no later source freshness is being manufactured.

## Next handoff

Build Integration should create the separate bounded Aug. 27 canonical replay PR from `intelligence/feeds/2026-08-27-source-health-reconciled.json`. Independently verify exactly five Aug. 26 predecessor/hash pairs, advance only matching source timestamps, and rerun source/history/report/intelligence/site-data/Agent Operations/Core/Maintenance before Repo Integrity reviews it. Do not replay Aug. 28-Aug. 31 research until the preceding chronology is canonical.
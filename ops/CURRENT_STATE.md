# Current Repository State

Last reconciled: 2026-09-01 19:21 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `96c4381ded1847acd891617d96827d89814404ae`, the merge of PR #110 (`Ops: preserve green post-PR107 coordination state`).
- PR #110 merged the exact tested coordination head `693ca88d87c2f59f11cc9d5ce1377656a090cf00`, which had passed Core validation `33482299932` and Daily Repository Maintenance `33482299769` before merge.
- Exact-merge Core validation `33485093125` and Deploy operations dashboard `33485093141` both succeeded on `96c4381d...`. Scheduled Daily Repository Maintenance `33517669710` and Intelligence Source Report `33524047829` also succeeded on that exact main commit.
- Three open research PRs exist: PR #103 (Aug. 31 morning), PR #106 (Aug. 31 afternoon), and PR #109 (Sep. 1). Each is a one-file contributed research lane. PR #103 and #106 predate current main; PR #109 is also based on pre-PR110 main `2b697ea...` and must be reconciled before integration. PR #109 head `c0ff08a271830a6b0b1c71ad3af0c96e396f0495` passed Core validation `33483798783` but GitHub currently does not report it mergeable against current main.
- No open issues were found.
- Source-health observations through Aug. 26 remain canonical. Aug. 27 and later raw/reconciled research has not been replayed canonically.

## Build / integration state

- PR #110 preserved the prior green post-PR107 coordination state and added blocked integration-queue records for PR #103 and PR #106. It did not advance canonical source history, registry freshness, primary evidence, tool maturity, opportunities, authorization state, or website markup.
- `intelligence/feeds/2026-08-27-source-health.json` remains preserved unchanged with its original invalid contributed hashes.
- `intelligence/feeds/2026-08-27-source-health-reconciled.json` remains the only eligible Aug. 27 replay surface. Canonical Aug. 27 replay has not occurred.
- `data/integration_queue.json` records PR #103 and PR #106 as blocked behind Aug. 27-Aug. 30, but it does not yet contain PR #109. Because the available connected file writer replaces the whole large JSON file and this run did not reconstruct that file byte-for-byte, PR #109 is recorded here and in this pass's PR description rather than risking loss of prior queue history.
- PR #109 contributes only `intelligence/feeds/2026-09-01-source-health.json`. Its ETHOnline, arXiv, RSA-tool, and CTF claims remain contributed evidence pending independent verification at the correct chronology point.

## Current research / intelligence state

- Canonical source history is current through Aug. 26 only.
- The Careers in Your Community Challenge remains specialized school/team opportunity intelligence, not generic individual work.
- xTech|Search 10 remains non-actionable until authoritative RFI/application evidence resolves conflicting official date surfaces.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.
- Raw later research preserved on `main` includes Aug. 28 PR #82, Aug. 29 PR #85/#91, and Aug. 30 PR #95/#99.
- Open PR #103 contributes Aug. 31 morning research at `2026-08-31T07:38:39Z`; PR #106 contributes Aug. 31 afternoon research at `2026-08-31T19:41:50Z`; PR #109 contributes Sep. 1 research at `2026-09-01T07:41:07Z`. All remain noncanonical and chronology-blocked behind the Aug. 27 replay and intervening snapshots.
- PR #109's reported ETHOnline prize total, preprint claims, RsaWebTool capability/license state, and NNS CTF prize details must not be promoted from the PR narrative alone.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain preservation debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`.
- No new tool/toolset registration or bespoke website HTML was introduced by PR #110 or the three open research PRs.
- Canonical discovery contracts remain unchanged: tools, toolsets, cases, intelligence, evidence, repository data, and Agent Operations flow through canonical registries/manifests/site-data builders.
- Exact-main Core validation and the successful dashboard deployment are the current release-health basis. Scheduled maintenance/source-report workflows are also green on exact current main.

## Known state / debt

- Canonically replay the reconciled Aug. 27 snapshot in a separate bounded PR, advancing only the five matching registry timestamps after exact predecessor/hash verification.
- Process Aug. 28, Aug. 29, Aug. 30, Aug. 31, and Sep. 1 research only after Aug. 27 becomes canonical, in timestamp/source-overlap order.
- Reconcile stale-base PR #103, PR #106, and PR #109 against current main before integration; preserve each one-file evidence contribution and do not infer freshness merely because its original CI was green.
- Add a machine-readable PR #109 integration-queue record when the queue can be updated without replacing/dropping prior provenance-bearing entries.
- Daily maintenance continues to report known generated/root artifact debt. Relocation remains a hash/reference-preserving task, not deletion cleanup.
- External provenance/authenticity for `310_challenge.png` remains unresolved.
- CI dependencies remain bounded ranges rather than a full lockfile, and workflows use supported major action tags rather than immutable action SHAs; treat this as non-blocking supply-chain hardening debt.
- A bounded indexed-code search for `shell=True` returned no matches in this pass; this is not a complete security audit.
- `docs/AGENT_HANDOFF.md` remains append-only and materially stale. The connected mutation primitive replaces whole-file content rather than atomically appending; this pass does not truncate it. The exact handoff is preserved in the PR description for safe append by a pass that can preserve the complete journal.

## Current operating priorities

1. Replay `intelligence/feeds/2026-08-27-source-health-reconciled.json` with the canonical `source-history replay-snapshot` dry-run/write workflow in a separate bounded PR.
2. Require exactly five Aug. 27 history records with reconciled hashes and verified Aug. 26 predecessors; advance only matching source-registry timestamps.
3. Rerun source-history/registry/report/intelligence/site-data/Agent Operations/Core/Maintenance validation and independently review before merge.
4. Only afterward process Aug. 28 morning/afternoon, Aug. 29 morning/afternoon, Aug. 30 morning/afternoon, PR #103 Aug. 31 morning, PR #106 Aug. 31 afternoon, then PR #109 Sep. 1.
5. Independently verify PR #109's primary-source claims and any external tool license/dependency/reporting behavior before promotion or integration.
6. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

PR #110 is merged and exact-merge Core/Pages workflow health is green. Its embedded current-main statement naturally became stale at merge, and PR #109 opened from the pre-PR110 base shortly before that merge. This branch corrects current repository truth while preserving all three open research lanes as contributed/noncanonical evidence. No source freshness or capability claim is advanced.

## Next handoff

Build Integration should create the separate bounded Aug. 27 canonical replay PR from `intelligence/feeds/2026-08-27-source-health-reconciled.json`. Independently verify exactly five Aug. 26 predecessor/hash pairs, advance only matching source timestamps, and rerun source/history/report/intelligence/site-data/Agent Operations/Core/Maintenance before Repo Integrity reviews it. Do not replay Aug. 28-Sep. 1 research until the preceding chronology is canonical.
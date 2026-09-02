# Current Repository State

Last reconciled: 2026-09-02 08:05 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `18e599d11ae82d433921441644f02a1b6105159c`, the merge of non-draft PR #117 preserving the exact unchanged tested coordination head from former draft PR #115.
- Former PR #115 head `4af122913f0c1b86c4b48b0745d995f3a036e5d4` passed Core `33603852033` and Daily Repository Maintenance `33603852086` with no review threads. The GitHub ready-for-review connector still fails on an unsupported `fullDatabaseId` field; #115 was closed unmerged and the exact head was recreated as #117 without rewriting history.
- PR #114 previously advanced canonical source history through Aug. 27 after independent hash/predecessor/registry/idempotence verification. Its final head `cef3541926fb93245de0fa43b851d2b0918ed2e6` passed Core `33554018254`, Intelligence Source Report `33554018512`, and Daily Maintenance `33554018586` before merge.
- Open later research lanes remain contributed/noncanonical evidence and must follow chronology. PR #116 is Sep. 2 raw research; PRs #103, #106, #109, and #112 are older-base later research lanes.

## Build / integration state

- Canonical source history remains through Aug. 27 at `2026-08-27T19:39:25Z`.
- Aug. 28 morning (`intelligence/feeds/2026-08-28-source-health.json`, `2026-08-28T07:40:27Z`) is the next chronological lane, but its preserved hashes are not replay-safe.
- All five stored Aug. 28 morning SHA-256 values fail the canonical `normalize_fingerprint(observed)` contract (`sha256(observed.strip().lower().encode("utf-8"))`). The original raw snapshot remains unchanged.
- A derived reconciliation is staged on branch `build/reconcile-aug28-morning-fingerprints-20260902` at `intelligence/feeds/2026-08-28-source-health-reconciled.json`. It preserves the exact observation strings, original PR #78 hashes, original head `d5ff98508d08a4d29633735e44fc5d0eec41c6e2`, and the PR #82 merge provenance `b14f45920b9557cb95142b8da64ad90f98f35c8b`.
- Corrected Aug. 28 morning fingerprints are:
  - `challenge-gov`: `1d4ecd2dfb8dedb600589fa4980dfaa1ce96d71a63dd54201821af7fbfc32aed`
  - `ctftime-upcoming`: `ab0660900275cf3767cd9b2f49f4bd08c2c0e2f68fa6f074ae1f2f55e66b380f`
  - `sherlock-bounties`: `e86ebfff5d52fc612e515a6bb6a6b771131938816faceed5e1782d14957860c9`
  - `arxiv-cryptography`: `b8cd96dfef25b74134fe858391b0aa4447f5b779bc46503443aaa8e23a00ef2c`
  - `ethglobal-events`: `8ae70a5efe8985d347d6fa3d8da1ee68767475a612395c3d1c9b150217fe6a24`
- Exact canonical Aug. 27 predecessors are, respectively: `c0e125df5360a452d731c08f76412c7d62381054fca56e6fcb4e2184575d12cf`, `ef2d96986e610ccbfbb877ba67ddc2c5f975182de29629b4401a34a81e0d4add`, `67f240a38ead70926e9776f3e5aa3afb6dc25920b3f7c555f34c7b9dbe262b05`, `d126279a1ebded4a02bb4dca40b381c8cf72484831d9913bf924ae5ebfc2b1c9`, and `9f0a188daf173966ee324470229a9bfbf2e864807b8f46200ea17f6bca9741dc`.
- `tests/test_aug28_source_reconciliation.py` stages deterministic provenance/hash/predecessor verification plus library and documented direct-script `--dry-run` non-mutation checks. Canonical history/registry files are intentionally untouched in this reconciliation pass.
- Aug. 28 afternoon and all later research remain chronology-blocked until this correction is independently verified and then replayed in a separate bounded canonical PR.

## Current research / intelligence state

- Aug. 28 morning includes a high-relevance preprint lead on trace-level provenance for agentic CTF evaluation. It remains research evidence only; no implementation or benchmark claim is adopted as repository capability.
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
- This Aug. 28 correction does not add or change any shared tool/toolset, case, opportunity, primary evidence, or bespoke website HTML.
- Canonical tools, toolsets, cases, source health, repository data, and Agent Operations continue to flow through registries/manifests/site-data builders.

## Known state / debt

- The Aug. 28 morning reconciliation branch needs CI and independent Repo Integrity review before it can be treated as the eligible replay surface.
- `data/integration_queue.json` should eventually record the raw-hash blocker and derived reconciliation without dropping existing provenance-heavy entries; do not reconstruct the queue unsafely through partial replacement.
- `docs/AGENT_HANDOFF.md` remains append-only. Do not truncate its historical journal merely to append through a whole-file writer; preserve the exact intended handoff in the PR when atomic append is unavailable.
- Later raw research must be reconciled only when chronology reaches it. External 310 provenance, root-artifact relocation, and supply-chain/runtime hardening remain separate debt.

## Current operating priorities

1. Run CI on the Aug. 28 morning reconciliation branch and inspect the deterministic direct-script dry-run regression.
2. Repo Integrity independently verifies original-vs-reconciled observation identity, all five bad original hashes, all five corrected hashes, the five Aug. 27 predecessors, and non-mutation.
3. If clean, merge the reconciliation only; then perform the actual canonical Aug. 28 morning replay in a separate bounded PR.
4. Process Aug. 28 afternoon only after the morning replay is canonical, then continue later snapshots in timestamp/source-overlap order.
5. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

The build pass did not rewrite the preserved Aug. 28 raw snapshot or advance source freshness after detecting the fingerprint defect. PR #117 merged coordination truth first, avoiding overlap with the later research PRs. The derived correction follows the same provenance-preserving pattern used successfully for Aug. 27.

## Next handoff

Repo Integrity should independently compare the original Aug. 28 morning snapshot to `2026-08-28-source-health-reconciled.json`, recompute all five hashes, verify the Aug. 27 predecessor chain, inspect `tests/test_aug28_source_reconciliation.py`, and merge the correction only if the exact head is green. The canonical write must remain a separate follow-up PR.

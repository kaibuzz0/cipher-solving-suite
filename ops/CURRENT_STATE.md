# Current Repository State

Last reconciled: 2026-09-03 07:21 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `787f96947ab8da762457d5c4c2607024d07a9cf6`, the merge of PR #121 (`Ops: reconcile state after PR #118 integrity merge`).
- PR #121 reused the exact unchanged coordination head `3530b9ab27fe7c34bb1e7fbc51a0ca89c0daa6fd`; its fresh Core validation `33676581808` succeeded before merge.
- Post-merge Core validation `33727463092` and Deploy operations dashboard `33727463141` both succeeded on exact merge commit `787f96947ab8da762457d5c4c2607024d07a9cf6`.
- The public GitHub Pages Operations Workspace is reachable and exposes repository navigation, opportunities, intelligence, cases, tools, evidence, collection health, source registry, and Agent Operations surfaces.
- No open repository issues were found during this reconciliation pass.

## Build / integration state

- Canonical source history remains through Aug. 27 at `2026-08-27T19:39:25Z`.
- The provenance-safe Aug. 28 morning replay surface is `intelligence/feeds/2026-08-28-source-health-reconciled.json` at `2026-08-28T07:40:27Z`.
- Corrected Aug. 28 morning fingerprints independently match the canonical normalization contract `sha256(observed.strip().lower().encode("utf-8"))`:
  - `challenge-gov`: `1d4ecd2dfb8dedb600589fa4980dfaa1ce96d71a63dd54201821af7fbfc32aed`
  - `ctftime-upcoming`: `ab0660900275cf3767cd9b2f49f4bd08c2c0e2f68fa6f074ae1f2f55e66b380f`
  - `sherlock-bounties`: `e86ebfff5d52fc612e515a6bb6a6b771131938816faceed5e1782d14957860c9`
  - `arxiv-cryptography`: `b8cd96dfef25b74134fe858391b0aa4447f5b779bc46503443aaa8e23a00ef2c`
  - `ethglobal-events`: `8ae70a5efe8985d347d6fa3d8da1ee68767475a612395c3d1c9b150217fe6a24`
- Exact canonical Aug. 27 predecessors are, respectively: `c0e125df5360a452d731c08f76412c7d62381054fca56e6fcb4e2184575d12cf`, `ef2d96986e610ccbfbb877ba67ddc2c5f975182de29629b4401a34a81e0d4add`, `67f240a38ead70926e9776f3e5aa3afb6dc25920b3f7c555f34c7b9dbe262b05`, `d126279a1ebded4a02bb4dca40b381c8cf72484831d9913bf924ae5ebfc2b1c9`, and `9f0a188daf173966ee324470229a9bfbf2e864807b8f46200ea17f6bca9741dc`.
- The original Aug. 28 morning raw snapshot remains preserved unchanged. The next canonical write must be a separate bounded replay PR using the reconciled snapshot; advance only those five source-history records and matching registry timestamps.
- Aug. 28 afternoon and all later research remain chronology-blocked until the morning replay is canonical.

## Current research / intelligence state

- Open later research lanes are PR #103 (Aug. 31 morning), PR #106 (Aug. 31 afternoon), PR #109 (Sep. 1 morning), PR #112 (Sep. 1 afternoon), PR #116 (Sep. 2 morning), and PR #120 (Sep. 2 afternoon). They remain contributed/noncanonical evidence and must be reconciled only at their chronology point.
- PR #120 is based on the pre-PR121 `ab0bfc21...` main and adds only `intelligence/feeds/2026-09-02-afternoon-source-health.json`; its `verialabs/ctf-agent` performance/prize statements remain project-authored research evidence rather than independently reproduced repository capability.
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

- Prior bounded default-branch searches found no indexed `shell=True`, `os.system(`, or `subprocess` matches; this is a targeted check, not a complete security audit.
- Daily Repository Maintenance remains the repository-wide non-destructive check for Python compilation, governance files, version drift, root generated artifacts, suspicious secret-like filenames, and the handoff journal.
- No primary research artifact was deleted, moved, or rewritten in this pass.

## Known state / debt

- `docs/WORK_QUEUE.md` still names the original Aug. 28 morning raw snapshot in its P2 next-step text. The operationally correct replay surface is the reconciled snapshot above; do not replay the invalid contributed hashes from the raw file.
- `data/integration_queue.json` keeps Aug. 28 at `needs-integration`, but its Aug. 28 record predates PR #118 and does not yet annotate the reconciliation path. It also does not yet represent every later open research lane, including PR #120.
- `docs/AGENT_HANDOFF.md` is append-only and remains materially behind current state. The available connector writer performs whole-file replacement, so do not risk truncating historical handoffs merely to append; preserve exact handoff text in the coordination PR description when atomic append is unavailable.
- Later raw research must be reconciled only when chronology reaches it. External 310 provenance, root-artifact relocation, and supply-chain/runtime hardening remain separate debt.

## Current operating priorities

1. Create a separate bounded canonical replay for `intelligence/feeds/2026-08-28-source-health-reconciled.json`.
2. Require exactly five Aug. 28 morning records with the corrected fingerprints and exact Aug. 27 predecessors above; advance only their corresponding registry timestamps and preserve registry-level timestamp non-rewind.
3. Rerun source-history, registry, collection report, intelligence validation, site-data/Agent Operations generation, Core, and Daily Maintenance on the replay head; independently review before merge.
4. Process `2026-08-28-afternoon-source-health.json` only after the morning replay is canonical, then continue Aug. 29 → Aug. 30 → Aug. 31 → Sep. 1 → Sep. 2 in timestamp/source-overlap order.
5. Reconcile stale later research branches against the then-current main at their chronology point and preserve compatible work rather than copying stale coordination state.
6. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

PR #121 safely replaced the closed draft PR #119 using the same tested coordination head and merged only after exact-head validation. Current-main release health is green on the merge commit. No source history, source registry freshness, primary research, tool maturity, case status, security authorization, or bespoke site HTML changed in that merge.

## Next handoff

Repo Integrity / Build Integration should replay `intelligence/feeds/2026-08-28-source-health-reconciled.json` in a separate small PR, verify the five corrected hashes and exact Aug. 27 predecessors again on the replay head, confirm canonical uniqueness/idempotence and registry non-rewind, then require green source/intelligence/site-data/Core/Maintenance validation before merge. Aug. 28 afternoon and later research remain blocked until that succeeds.

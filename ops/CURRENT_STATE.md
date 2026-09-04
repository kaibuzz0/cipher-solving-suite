# Current Repository State

Last reconciled: 2026-09-04 07:28 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `5abbab17ad33c50f28efd5ef5be9fa5d89bfbea2`, the merge of PR #127 (`Build: replay verified Aug 28 morning source health`).
- PR #127 final head `3a73d461933f9064f61da3b83d9d1fcf01e71ca7` passed Core validation `33848641904`, Intelligence Source Report `33848641950`, and Daily Repository Maintenance `33848641922` before merge.
- Core passed on Python 3.11, 3.12, and 3.13. The inspected Python 3.12 job ran 79 tests with 79 passing; compilation, source registry/history/report validation, intelligence validation, artifact inventory, both 310 verification stages, site-data generation, Agent Operations parsing, repository/tool discovery, and maintenance all passed.
- No open repository issue currently blocks the chronological source-replay lane.
- GitHub Pages remains configured for the repository and the default-branch deployment workflow was green before this replay; an independent post-merge public render was not available in this runtime, so no fresh browser-render claim is made.

## Build / integration state

- Canonical source history now extends through Aug. 28 morning at `2026-08-28T07:40:27Z`.
- PR #127 replayed exactly five observations from `intelligence/feeds/2026-08-28-source-health-reconciled.json` using the independently verified corrected fingerprints and exact canonical Aug. 27 predecessors.
- The original invalid-hash raw snapshot `intelligence/feeds/2026-08-28-source-health.json` remains preserved unchanged.
- The five canonical Aug. 28 morning fingerprints are:
  - `challenge-gov`: `1d4ecd2dfb8dedb600589fa4980dfaa1ce96d71a63dd54201821af7fbfc32aed`
  - `ctftime-upcoming`: `ab0660900275cf3767cd9b2f49f4bd08c2c0e2f68fa6f074ae1f2f55e66b380f`
  - `sherlock-bounties`: `e86ebfff5d52fc612e515a6bb6a6b771131938816faceed5e1782d14957860c9`
  - `arxiv-cryptography`: `b8cd96dfef25b74134fe858391b0aa4447f5b779bc46503443aaa8e23a00ef2c`
  - `ethglobal-events`: `8ae70a5efe8985d347d6fa3d8da1ee68767475a612395c3d1c9b150217fe6a24`
- The next chronological integration gate is `intelligence/feeds/2026-08-28-afternoon-source-health.json` at `2026-08-28T19:37:39Z`. Its hashes, predecessor links, source claims, and any tool/research leads must be independently verified against the newly canonical Aug. 28 morning state before replay.
- Aug. 29 and all later research remain chronology-blocked until Aug. 28 afternoon is canonical.

## Current research / intelligence state

- Later open research lanes are PR #103 (Aug. 31 morning), PR #106 (Aug. 31 afternoon), PR #109 (Sep. 1 morning), PR #112 (Sep. 1 afternoon), PR #116 (Sep. 2 morning), PR #120 (Sep. 2 afternoon), PR #123 (Sep. 3 morning), and PR #125 (Sep. 3 afternoon). They remain contributed/noncanonical evidence and must be reconciled only at their chronology point.
- PR #125 is a one-file Sep. 3 afternoon research contribution from stale base `5737c29...`; its loop-safety preprint, ETHOnline, NNS CTF, and xTech observations are not canonical truth until independently verified at the Sep. 3 chronology point.
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

- Fresh bounded default-branch searches in this pass found no indexed `shell=True` or `os.system(` matches; this is a targeted check, not a complete security audit.
- PR #127 maintenance reported 40 artifacts, 10 duplicate groups, 11 orphaned items, 12 generated outputs, 7 items needing case links, 1 protected primary-evidence item, and 0 unknown-provenance items.
- Known root-generated 310 artifacts remain warnings and were left untouched.
- Workflow dependencies remain bounded but not fully immutable: Actions workflows use major tags such as `actions/checkout@v4`, `actions/setup-python@v5`, and `actions/upload-artifact@v4`, while Python test dependencies use bounded version ranges. Node-runtime deprecation warnings are present in Actions logs. Treat immutable action pinning/runtime migration and lockfile strategy as supply-chain hardening debt, not a release blocker for this replay.
- No primary research artifact was deleted, moved, or rewritten in this pass.

## Known state / debt

- `data/integration_queue.json` still needs a provenance-preserving coordination update that marks the Aug. 28 morning replay integrated and represents Sep. 2/Sep. 3 later research lanes without discarding older entries.
- `docs/AGENT_HANDOFF.md` is append-only and materially behind current state; this reconciliation branch must append rather than replace historical handoff content.
- Later raw research must be reconciled only when chronology reaches it. External 310 provenance, root-artifact relocation, immutable Actions/dependency hardening, and direct public Pages render verification remain separate debt.

## Current operating priorities

1. Independently verify `intelligence/feeds/2026-08-28-afternoon-source-health.json` against canonical Aug. 28 morning state.
2. Recompute every protected hash, verify exact latest predecessor per source, validate timestamp order/uniqueness/idempotence, and independently reopen high-impact primary sources before any canonical replay.
3. Replay only evidence-backed Aug. 28 afternoon observations and advance only matching registry timestamps; preserve all raw research unchanged.
4. Rerun source-history, registry, collection report, intelligence validation, site-data/Agent Operations, Core, and Daily Maintenance; independently review before merge.
5. Continue Aug. 29 → Aug. 30 → Aug. 31 → Sep. 1 → Sep. 2 → Sep. 3 strictly in timestamp/source-overlap order, reconciling stale branches against then-current main while preserving compatible evidence.
6. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

PR #127 advanced the Aug. 28 morning replay after independent hash/predecessor verification. Its first Core run correctly failed because three regression tests still asserted the pre-replay state; the tests were updated to preserve provenance and uniqueness while requiring Aug. 27 and Aug. 28 reconciled snapshots to remain canonically present and idempotent after later replay. The corrected exact head then passed all required validation before merge. No raw evidence, opportunity/case status, security authorization, tool maturity, or bespoke site HTML was changed.

## Next handoff

Repo Integrity / Build Integration should process `intelligence/feeds/2026-08-28-afternoon-source-health.json` next. Treat it as contributed evidence, independently recompute its fingerprints and verify its latest canonical predecessors against Aug. 28 morning, reopen any high-impact source claims, and only then stage a bounded replay with full Core/Source Report/Maintenance/site-data validation. Aug. 29 and later research remain blocked until that succeeds.

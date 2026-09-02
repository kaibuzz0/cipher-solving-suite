# Current Repository State

Last reconciled: 2026-09-02 19:26 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `ab0bfc21277f6bf34b71f1fbb632dae3cf23148c`, the merge of PR #118 (`Build: reconcile Aug 28 morning source fingerprints without rewriting evidence`).
- PR #118 exact head `58bd0e4225fa2bbaa464ae11c6e90bc325bfceb6` was independently reviewed before merge. Core validation `33606739008` passed on Python 3.11/3.12/3.13 and Daily Repository Maintenance also passed on that exact head; no review threads were present.
- Post-merge Core validation `33672567059` and Deploy operations dashboard `33672567142` both succeeded on exact merge commit `ab0bfc21277f6bf34b71f1fbb632dae3cf23148c`. The public GitHub Pages Operations Workspace is reachable and exposes repository navigation, opportunities, intelligence, cases, tools, evidence, collection health, source registry, and Agent Operations surfaces.
- The independently recomputed canonical normalization contract is `sha256(observed.strip().lower().encode("utf-8"))`. All five corrected Aug. 28 morning fingerprints in the reconciled snapshot match that contract and all five predecessor links match canonical Aug. 27 source history.
- The preserved raw Aug. 28 morning snapshot remains unchanged. PR #118 added only a derived reconciliation surface, a deterministic regression, and coordination state; it did not advance canonical source history or registry freshness.

## Build / integration state

- Canonical source history remains through Aug. 27 at `2026-08-27T19:39:25Z`.
- The provenance-safe Aug. 28 morning replay surface is now `intelligence/feeds/2026-08-28-source-health-reconciled.json` at `2026-08-28T07:40:27Z`.
- Corrected Aug. 28 morning fingerprints are:
  - `challenge-gov`: `1d4ecd2dfb8dedb600589fa4980dfaa1ce96d71a63dd54201821af7fbfc32aed`
  - `ctftime-upcoming`: `ab0660900275cf3767cd9b2f49f4bd08c2c0e2f68fa6f074ae1f2f55e66b380f`
  - `sherlock-bounties`: `e86ebfff5d52fc612e515a6bb6a6b771131938816faceed5e1782d14957860c9`
  - `arxiv-cryptography`: `b8cd96dfef25b74134fe858391b0aa4447f5b779bc46503443aaa8e23a00ef2c`
  - `ethglobal-events`: `8ae70a5efe8985d347d6fa3d8da1ee68767475a612395c3d1c9b150217fe6a24`
- Exact canonical Aug. 27 predecessors are, respectively: `c0e125df5360a452d731c08f76412c7d62381054fca56e6fcb4e2184575d12cf`, `ef2d96986e610ccbfbb877ba67ddc2c5f975182de29629b4401a34a81e0d4add`, `67f240a38ead70926e9776f3e5aa3afb6dc25920b3f7c555f34c7b9dbe262b05`, `d126279a1ebded4a02bb4dca40b381c8cf72484831d9913bf924ae5ebfc2b1c9`, and `9f0a188daf173966ee324470229a9bfbf2e864807b8f46200ea17f6bca9741dc`.
- `tests/test_aug28_source_reconciliation.py` protects original-vs-reconciled observation identity, corrected hashes, exact canonical predecessors, and documented dry-run/non-mutation behavior.
- The next canonical write must be a separate bounded replay PR using the reconciled snapshot. Advance only the five matching source-history/registry records; do not rewrite the raw snapshot.
- Aug. 28 afternoon and all later research remain chronology-blocked until the morning replay is canonical.

## Current research / intelligence state

- Open later research lanes are PR #103 (Aug. 31 morning), PR #106 (Aug. 31 afternoon), PR #109 (Sep. 1 morning), PR #112 (Sep. 1 afternoon), and PR #116 (Sep. 2 morning). They remain contributed/noncanonical evidence and must be reconciled only at their chronology point.
- Aug. 28 morning includes a high-relevance arXiv preprint on trace-level provenance for agentic CTF evaluation. It remains research evidence only; no benchmark or implementation claim is adopted as repository capability.
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
- PR #118 did not add or change any shared tool/toolset, case, opportunity, primary evidence, or bespoke website HTML.
- Canonical tools, toolsets, cases, source health, repository data, and Agent Operations continue to flow through registries/manifests/site-data builders. PR #118 exact-head Core included dashboard-data generation and the repository's existing discovery/validation contracts.

## Security / maintenance state

- Bounded default-branch searches found no indexed `shell=True`, `os.system(`, or `subprocess` matches in this pass. This is a targeted check, not a complete security audit.
- Daily Repository Maintenance remains the repository-wide non-destructive check for Python compilation, governance files, version drift, root generated artifacts, suspicious secret-like filenames, and the handoff journal.
- No primary research artifact was deleted, moved, or rewritten in this pass.

## Known state / debt

- `docs/WORK_QUEUE.md` still names the original Aug. 28 morning snapshot in its P2 next-step text. The operationally correct replay surface is now the reconciled snapshot above; do not replay the invalid contributed hashes from the raw file.
- `data/integration_queue.json` correctly keeps Aug. 28 at `needs-integration`, but its Aug. 28 record predates PR #118 and does not yet annotate the merged reconciliation path. Preserve its provenance-heavy history; update that record only through a safe complete-file or structured mutation rather than reconstructing it from a truncated view.
- `docs/AGENT_HANDOFF.md` remains append-only and its latest stored integrity handoff is materially older than current state. The available writer is whole-file replacement, so do not risk truncating the historical journal merely to append. Preserve the exact intended new handoff in the coordination PR description when atomic append is unavailable.
- Later raw research must be reconciled only when chronology reaches it. External 310 provenance, root-artifact relocation, and supply-chain/runtime hardening remain separate debt.

## Current operating priorities

1. Create a separate bounded canonical replay for `intelligence/feeds/2026-08-28-source-health-reconciled.json`.
2. Require exactly five Aug. 28 morning records with the corrected fingerprints and exact Aug. 27 predecessors above; advance only their corresponding registry timestamps and preserve registry-level timestamp non-rewind.
3. Rerun source-history, registry, collection report, intelligence validation, site-data/Agent Operations generation, Core, and Daily Maintenance on the replay head; independently review before merge.
4. Process `2026-08-28-afternoon-source-health.json` only after the morning replay is canonical, then continue Aug. 29 → Aug. 30 → Aug. 31 → Sep. 1 → Sep. 2 in timestamp/source-overlap order.
5. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

PR #118 was reconciled directly against current `main`, independently verified, and merged without rewriting the preserved Aug. 28 raw contribution. This preserves compatible contributed research while preventing invalid contributed fingerprints from becoming canonical. No later research branch was allowed to overtake the chronology gate.

## Next handoff

Repo Integrity / Build Integration should replay `intelligence/feeds/2026-08-28-source-health-reconciled.json` in a separate small PR, verify exact corrected hashes and Aug. 27 predecessors again on the replay head, confirm canonical uniqueness/idempotence and registry non-rewind, then require green source/intelligence/site-data/Core/Maintenance validation before merge. Aug. 28 afternoon remains blocked until that succeeds.

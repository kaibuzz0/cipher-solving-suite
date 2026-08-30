# Current Repository State

Last reconciled: 2026-08-30 20:05 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `5441a2fce8abf1fc039daa97305bbad505a491c6`, the merge of PR #100 preserving the exact green coordination head from former draft PR #98 after the connected draft-to-ready mutation failed.
- PR #100 exact head `952374234f35d90417cc1f1998e497e104955459` passed Core validation `33330753366` and Daily Repository Maintenance `33330753324`; no review threads were present.
- Source-health observations through Aug. 26 remain canonical. PR #75 and PR #82 added raw research only; they did not advance canonical source history or source-registry freshness.
- The GitHub Pages REST state endpoint is not exposed by the current connector/runtime. No unsupported fresh browser-render claim is made.

## Build / integration state

- Aug. 27 PR #75 raw evidence remains preserved unchanged on `main`. Every stored `sha256` differs from the repository's canonical `normalize_fingerprint(observed)` result (`observed.strip().lower()` followed by SHA-256).
- Independent recomputation gives: `challenge-gov` `c0e125df5360a452d731c08f76412c7d62381054fca56e6fcb4e2184575d12cf`; `ctftime-upcoming` `ef2d96986e610ccbfbb877ba67ddc2c5f975182de29629b4401a34a81e0d4add`; `sherlock-bounties` `67f240a38ead70926e9776f3e5aa3afb6dc25920b3f7c555f34c7b9dbe262b05`; `arxiv-cryptography` `d126279a1ebded4a02bb4dca40b381c8cf72484831d9913bf924ae5ebfc2b1c9`; `ethglobal-events` `9f0a188daf173966ee324470229a9bfbf2e864807b8f46200ea17f6bca9741dc`.
- PR #75's single introducing commit `3fd83de69a0ec626a6f03143f3207a5c52ec7ade` already contains the current observation strings and mismatched hashes together. No earlier in-repository version of the Aug. 27 snapshot was found, so the exact pre-commit origin of the bad hashes cannot be established from repository history.
- Branch `build/reconcile-aug27-fingerprints-20260830` adds `intelligence/feeds/2026-08-27-source-health-reconciled.json` as an explicit derived correction. It preserves the exact PR #75 observation strings, records all five original hashes and source commits, and substitutes only the recomputed canonical fingerprints in the derived replay surface.
- `tests/test_aug27_source_reconciliation.py` verifies original-vs-derived text identity, original hash preservation, exact corrected hashes, exact Aug. 26 predecessor fingerprints, all-five `changed` classification, direct-script dry-run behavior, and byte-for-byte non-mutation of temporary history/registry files.
- Canonical Aug. 27 replay is still review-gated. `data/source_check_history.json` and `data/intelligence_sources.json` are intentionally unchanged by this reconciliation pass.
- PR #82's Aug. 28 morning and afternoon raw research remains blocked behind valid Aug. 27 reconciliation/replay. Open PRs #85, #91, #95 and #99 preserve later research and must not overtake the chronology gate.

## Current research / intelligence state

- Canonical source history is current through Aug. 26 only.
- The Careers in Your Community Challenge remains specialized opportunity intelligence. Do not treat it as generic individual work; school/Perkins V/team requirements remain participation gates.
- xTech|Search 10 remains non-actionable until authoritative RFI/application evidence resolves conflicting official date surfaces.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.
- Aug. 28+ research remains contributed evidence until chronology and normal verification are satisfied.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`.
- No new tool/toolset registration or bespoke site HTML is introduced by the Aug. 27 reconciliation branch.
- Canonical discovery contracts remain unchanged: tools, toolsets, cases, intelligence, evidence, repository data and Agent Operations should flow through canonical registries/manifests/site-data builders.

## Known state / debt

- Independently verify the derived Aug. 27 reconciliation snapshot and deterministic regression before canonical replay.
- Aug. 28 and later source snapshots remain blocked behind canonical Aug. 27 replay.
- `docs/AGENT_HANDOFF.md` is append-only; do not replace/truncate historical entries when adding this pass's handoff.
- Daily maintenance continues to report known root-generated artifact debt; migration must preserve hashes, references and provenance.
- External provenance/authenticity for `310_challenge.png` remains unresolved.
- Workflow actions use supported major tags and Python CI uses bounded ranges rather than immutable action SHAs/a full lockfile; treat this as non-blocking supply-chain hardening debt.

## Current operating priorities

1. Independently verify `2026-08-27-source-health-reconciled.json` against the preserved PR #75 source strings and Aug. 26 canonical predecessors.
2. Require green Core/Maintenance validation on the exact reconciliation PR head; merge only if the original raw snapshot remains untouched and the dry-run is non-mutating.
3. In a separate bounded pass after merge, canonically replay the reconciled Aug. 27 snapshot and advance only the matching source-registry timestamps.
4. Only after Aug. 27 becomes canonical, process merged Aug. 28 morning/afternoon research, then Aug. 29/Aug. 30 research in timestamp order.
5. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

PR #98 had a clean exact head but could not be marked ready because the connected GitHub GraphQL mutation references an unsupported `fullDatabaseId` field. It was closed unmerged and the exact unchanged tested branch was exposed as non-draft PR #100, then merged without history rewriting as `5441a2fc...`. This reconciliation branch starts from that current main and does not overlap the later raw-research-only PRs.

## Next handoff

Repo Integrity should independently compare all five original and reconciled Aug. 27 observation strings/hashes, verify the expected Aug. 26 predecessor chain, run the direct-script `replay-snapshot --dry-run` regression and the normal Core/Maintenance/site-data checks, and merge the reconciliation PR only if the canonical files remain untouched. Canonical Aug. 27 replay should then occur in its own bounded PR.

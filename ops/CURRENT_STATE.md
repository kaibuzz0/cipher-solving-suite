# Current Repository State

Last reconciled: 2026-08-30 08:02 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `09ccb93b91e2cf4e97c1b388393d8a41cacea77e`, the merge of PR #96, which preserved the exact already-green post-PR93 coordination head after the connector again failed the draft-to-ready transition.
- PR #96 exact head `ccff4f8dd22c4eacc89e7a5b4f1e3a0711209e2e` is identical to draft PR #94 and had already passed Core validation `33299170699` and Daily Repository Maintenance `33299170761` with no review threads.
- PR #93 final head `5403df4d36ce3160db58e45c786b8ca5d2ed84e5` passed Core validation `33272701911` on Python 3.11/3.12/3.13, Intelligence Source Report `33272701915`, and Daily Repository Maintenance `33272701910`; post-merge Core `33299042160` and Deploy operations dashboard `33299042070` succeeded on merge `8d2b20ba...`.
- Source-health observations through Aug. 26 remain canonical and independently verified.

## Build / integration state

- Aug. 26 is integrated; Aug. 27 PR #75 is the next chronological source lane.
- PR #75 cannot currently pass the canonical snapshot replay contract. All five stored `sha256` values in `intelligence/feeds/2026-08-27-source-health.json` differ from `normalize_fingerprint(observed)` in `scripts/source_check_history.py`.
- Independent recomputation from the preserved `observed` strings produced: `challenge-gov` `c0e125df5360a452d731c08f76412c7d62381054fca56e6fcb4e2184575d12cf`; `ctftime-upcoming` `ef2d96986e610ccbfbb877ba67ddc2c5f975182de29629b4401a34a81e0d4add`; `sherlock-bounties` `67f240a38ead70926e9776f3e5aa3afb6dc25920b3f7c555f34c7b9dbe262b05`; `arxiv-cryptography` `d126279a1ebded4a02bb4dca40b381c8cf72484831d9913bf924ae5ebfc2b1c9`; `ethglobal-events` `9f0a188daf173966ee324470229a9bfbf2e864807b8f46200ea17f6bca9741dc`.
- PR #75 instead stores `d2c287eb...`, `fce07b15...`, `09762fba...`, `2eae0878...`, and `b29a7c12...` respectively. Because `_validate_snapshot` fails closed on any fingerprint mismatch, no canonical Aug. 27 history or registry freshness was advanced.
- Do not silently replace the stored PR #75 hashes in place: that raw contribution is provenance evidence. A corrected/reconciled Aug. 27 snapshot must explicitly preserve the contribution origin and explain whether the observed strings or the hashes were stale.
- PR #82 owns Aug. 28 morning/afternoon raw research, PR #85 owns Aug. 29 morning research, PR #91 owns later Aug. 29 ETHOnline prize evidence, and PR #95 owns Aug. 30 research. None should overtake the unresolved Aug. 27 provenance gate.

## Current research / intelligence state

- Aug. 22 morning, Aug. 22 afternoon, Aug. 23, Aug. 24, Aug. 25, and Aug. 26 source-health observations are canonical.
- The Careers in Your Community Challenge remains specialized school/team opportunity intelligence from PR #75, but this build pass did not promote or republish it because the containing raw snapshot fails its internal fingerprint contract before replay.
- xTech|Search 10 remains non-actionable until authoritative RFI/application evidence resolves the conflicting official date surfaces.
- NASA RASC-AL remains specialized research and should not be converted into generic actionable work without complete official competition guidelines.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`.
- No tool/toolset registration, case, opportunity, primary evidence, or bespoke website HTML was changed in this blocker pass.
- The current generated site-data/Agent Operations path remained green through the post-PR93 validation and dashboard deployment cited above.

## Known state / debt

- Repair/reconcile Aug. 27 PR #75 provenance before any canonical replay. Determine whether each stored hash corresponds to an earlier observation string or whether the observation text changed after hashing; preserve both the original raw contribution and the correction trail.
- After a corrected Aug. 27 snapshot passes exact hash/predecessor validation, replay it canonically before processing Aug. 28, Aug. 29, or Aug. 30 research.
- Keep xTech|Search 10 non-actionable until authoritative RFI/application evidence resolves the date conflict.
- Daily maintenance still reports known generated root artifacts; artifact inventory reports duplicates/orphans requiring hash- and reference-preserving migration rather than destructive cleanup.
- External provenance/authenticity for `310_challenge.png` remains unresolved.

## Current operating priorities

1. Treat PR #75 as blocked for canonical integration because all five snapshot fingerprints fail the repository normalization contract.
2. Produce a provenance-preserving corrected Aug. 27 snapshot or recover the exact original observed strings corresponding to the stored hashes; do not rewrite the original evidence silently.
3. Independently recheck the official Careers in Your Community rules before any structured opportunity promotion.
4. Once Aug. 27 is valid and canonical, process Aug. 28 PR #82, Aug. 29 PR #85/#91, and Aug. 30 PR #95 strictly chronologically.
5. Continue 310 external-provenance and hash-preserving root-artifact work without inflating experimental capability claims.

## Coordination note

The build pass first cleared stale shared coordination by merging PR #96 from the exact green PR #94 head after the GitHub ready-for-review connector failed. It then inspected PR #75 before editing canonical source history. The canonical replay implementation explicitly recomputes each fingerprint from `observed.strip().lower()` and rejects mismatches before writing either history or registry. Independent recomputation found all five PR #75 hashes inconsistent, so the safe result is a documented blocker rather than manufactured freshness.

## Next handoff

Investigate PR #75's hash provenance. Preserve `intelligence/feeds/2026-08-27-source-health.json` unchanged as contributed evidence, identify whether the stored hashes were produced from earlier text, and create an explicit corrected/reconciled snapshot only with a documented origin trail. Then run `source-history replay-snapshot --dry-run` against current Aug. 26 canonical history, verify exact predecessors and zero mutation, recheck Careers in Your Community official rules, and only after those gates pass stage the Aug. 27 canonical replay. Do not let PR #82/#85/#91/#95 overtake this lane.

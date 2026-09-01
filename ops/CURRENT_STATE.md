# Current Repository State

Last reconciled: 2026-09-01 20:15 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `fb03976e6ac804cb294c99aabed7d4e8979b1422`, the merge of PR #113 (`Ops: preserve green post-PR110 coordination state`).
- PR #113 preserved the exact unchanged tested head `a3801734bb791370193a0a4458cc51202c501553` from former draft PR #111 after the connected ready-for-review mutation failed on GitHub's unsupported `fullDatabaseId` field. That exact head passed Core validation `33549463149` and had no review threads before merge; no history was rewritten.
- Build replay PR #114 is open from exact post-PR113 `main`. Its source-specific workflows are green on head `6db387931920dc419884b03c82aade5fbed96c38`: Intelligence Source Report `33553774531` and Daily Repository Maintenance `33553774563` succeeded. Core validation `33553774541` is still running at this reconciliation point and must pass before the build handoff is called green.
- Open later research lanes remain contributed/noncanonical evidence: PR #103 (Aug. 31 morning), PR #106 (Aug. 31 afternoon), PR #109 (Sep. 1 morning), and PR #112 (Sep. 1 afternoon). They remain behind chronological source replay and do not authorize testing or establish user-specific actionability.
- No repository issue has displaced the Aug. 27 source replay as the highest-value bounded integration gate.

## Build / integration state

- PR #114 stages the canonical replay of `intelligence/feeds/2026-08-27-source-health-reconciled.json` at `2026-08-27T19:39:25Z`.
- The original PR #75 raw file `intelligence/feeds/2026-08-27-source-health.json` remains unchanged with its original invalid contributed hashes. PR #101's separately derived reconciliation remains the only replay surface.
- Exactly five history records are added and exactly five matching source `last_checked_at` timestamps advance: `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`.
- The five corrected fingerprints are `c0e125df5360a452d731c08f76412c7d62381054fca56e6fcb4e2184575d12cf`, `ef2d96986e610ccbfbb877ba67ddc2c5f975182de29629b4401a34a81e0d4add`, `67f240a38ead70926e9776f3e5aa3afb6dc25920b3f7c555f34c7b9dbe262b05`, `d126279a1ebded4a02bb4dca40b381c8cf72484831d9913bf924ae5ebfc2b1c9`, and `9f0a188daf173966ee324470229a9bfbf2e864807b8f46200ea17f6bca9741dc` respectively.
- Their exact Aug. 26 predecessors are `eb797b905124aa7ca06577aa2eac6f98734601a851ecad7ad53c4e0628b9fc87`, `111f238ab58ed2167d6e1e9ab0072516d8e0777b1c35ba1adc327c51f497afc2`, `c8a1e59f595a1d8d788ca5cfc22f3d4cb6ee782b741a443911347ea0cf935665`, `f58d8d0792b943fde0bab2a867d452c40ff006d243e8d812e984829009890ab9`, and `b9291f5dc88d437f71898fb71674a69535f7083429172423a2422c3e495645d0`.
- `data/source_check_history.json` advances its `updated_at` to the replay timestamp. `data/intelligence_sources.json` keeps registry-level `updated_at` at the already-newer `2026-08-27T20:02:00Z`; the replay does not rewind it.
- `tests/test_aug27_source_reconciliation.py` now verifies original-vs-reconciled provenance, corrected hashes, exactly one canonical record per source/timestamp, exact predecessors, registry advancement, and byte-for-byte idempotence through both the library API and documented direct-script replay.
- Compare-to-base inspection before coordination edits showed only five registry timestamp substitutions and five new source-history records; no older history records were removed.
- `data/integration_queue.json` still labels the Aug. 27 item `needs-integration` because the connected writer replaces the entire provenance-bearing queue. Do not mark it `integrated` before Repo Integrity review. The intended state while PR #114 is open is `needs-review`; this limitation is documented here and in the PR handoff rather than risking loss of queue history.

## Current research / intelligence state

- If PR #114 passes final Core and Repo Integrity review, canonical source history will be current through Aug. 27. Until merge, `main` remains canonical only through Aug. 26.
- Aug. 28 morning/afternoon research on `main` is next in chronological order after PR #114. Aug. 29, Aug. 30, Aug. 31 and Sep. 1 remain blocked behind it.
- PR #112 adds a later Sep. 1 afternoon raw-research lane; its ETHOnline/xTech observations remain contributed evidence and do not overtake earlier timestamps.
- Careers in Your Community remains specialized school/team opportunity intelligence, not generic individual work.
- xTech|Search 10 remains non-actionable until authoritative RFI/application evidence resolves conflicting official date surfaces.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain preservation debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`.
- No tool/toolset registration, maturity change, or bespoke website HTML is part of PR #114.
- Canonical tools, toolsets, cases, source health, repository data and Agent Operations continue to flow through registries/manifests/site-data builders. Core validation is responsible for the relevant generated-data and Agent Operations compatibility checks before this PR is handed to Repo Integrity.

## Known state / debt

- PR #114 must finish Core validation and then receive independent Repo Integrity verification before merge.
- After merge, update `data/integration_queue.json` to mark Aug. 27 integrated and move Aug. 28 morning to the next replay lane; do not process Aug. 28 afternoon first.
- Reconcile stale/later research PRs only when chronology reaches them. Preserve their raw one-file evidence and independently verify source claims before canonical replay or opportunity/case promotion.
- `data/integration_queue.json` does not yet have complete machine-readable records for the Sep. 1 research PRs; add them through a safe queue-preserving update rather than replacing/dropping prior entries.
- `docs/AGENT_HANDOFF.md` remains append-only and materially stale. The connected mutation primitive replaces the whole file rather than atomically appending; do not truncate the historical journal. PR #114 carries the exact intended handoff for a safe append-capable integrity pass.
- External provenance/authenticity for `310_challenge.png`, root-artifact relocation, and supply-chain/runtime hardening remain separate debt.

## Current operating priorities

1. Finish PR #114 Core validation and independently verify its five-record/five-timestamp Aug. 27 contract.
2. Merge PR #114 only if the final head is green and Repo Integrity confirms the corrected hashes/predecessors and idempotence regression.
3. Then mark the Aug. 27 integration-queue item integrated and process Aug. 28 morning before Aug. 28 afternoon.
4. Continue Aug. 29 morning/afternoon, Aug. 30 morning/afternoon, Aug. 31 morning/afternoon, Sep. 1 morning, then Sep. 1 afternoon in timestamp/source-overlap order.
5. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

PR #111 was not discarded: its exact green head was preserved unchanged as non-draft PR #113 and merged. PR #114 starts from that exact merge, so the build replay does not overwrite the integrity coordination work. Later research PRs own separate raw feed files and are preserved behind chronology.

## Next handoff

Repo Integrity should inspect PR #114's final diff and CI, independently recompute the five corrected hashes from the reconciled observation strings, confirm the five Aug. 26 predecessors and registry non-rewind, run/inspect the canonical idempotence regression and generated Agent Operations/site-data checks, and merge only if clean. After merge, Aug. 28 morning is the next canonical replay lane.

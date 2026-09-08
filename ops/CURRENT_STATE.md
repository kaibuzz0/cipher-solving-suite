# Current Repository State

Last reconciled: 2026-09-08 19:27 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `418e9a7c7c101aa499fe76114c6b614ab4c82ba0`, the merge of PR #148 (`Build: replay Aug 29 morning source health`).
- Exact-main Core validation run `34268952166` completed successfully on `418e9a7c7c101aa499fe76114c6b614ab4c82ba0`.
- Exact-main Deploy operations dashboard run `34268952068` completed successfully on the same commit.
- PR #148 exact head `894cb281b30a7186310e89b1ae17a37c4d8006fc` independently passed Core validation `34203251256`, Daily Repository Maintenance `34203251103`, and Intelligence Source Report `34203251082` before merge.
- No open repository issues currently block the chronological source-replay lane.

## Canonical source / integration state

- Canonical source history now ends at Aug. 29 morning, `2026-08-29T07:38:35Z`.
- PR #148 added exactly five Aug. 29 morning records for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events` using the verified predecessor chain from Aug. 28 canonical history.
- Only those five matching source-registry `last_checked_at` values advanced. `github-search` did not advance.
- The preserved raw snapshot `intelligence/feeds/2026-08-29-source-health.json` was not rewritten by PR #148.
- The historical Aug. 28 afternoon regression now requires registry/history freshness to remain monotonic rather than incorrectly requiring equality to the older Aug. 28 timestamp; canonical Aug. 28 records and fingerprints remain required.
- Generated source-report and site-data files were refreshed through repository-native builders; PR #148 did not hand-edit `site/index.html`.
- Aug. 29 afternoon is now the next chronological replay gate. Aug. 30 and later research must not advance canonical freshness before it.

## Concurrent research / evidence state

- Open later research lanes remain contributed/noncanonical evidence until chronology reaches them: PR #103/#106 (Aug. 31), #109/#112 (Sep. 1), #116/#120 (Sep. 2), #123/#125 (Sep. 3), #131/#136 (Sep. 4), #139 (Sep. 5), #141 (Sep. 6), and #144/#146 (Sep. 7).
- Stale branches must be reconciled onto then-current `main` while preserving compatible one-file research evidence. Do not copy their source, benchmark, prize, license, security, or capability claims into canonical truth without independent verification.
- Public bounty/program/event listings remain discovery evidence only and are not authorization to test unrelated targets.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- The 310 tools remain `experimental`; repository-internal reproduction does not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- Normal tools, toolsets, cases, intelligence, evidence, and opportunity state must flow through canonical registries/manifests/site-data builders rather than bespoke HTML.
- Exact-main Pages deployment is green after PR #148.

## Security / maintenance state

- Existing targeted checks have found no indexed `shell=True` or `os.system(` use; this is not a complete security audit.
- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- GitHub Actions continue to use major-version action tags rather than immutable commit SHAs; action pinning and stronger dependency locking remain supply-chain hardening debt.
- Known root/generated artifact duplicate/orphan work remains preservation-sensitive maintenance, not a deletion task.

## Coordination reconciliation after PR #148

- PR #148 successfully repaired the previously stale `docs/WORK_QUEUE.md`, `data/integration_queue.json`, `docs/AGENT_HANDOFF.md`, and generated Agent Operations/site-data surfaces for the staged Aug. 29 morning replay.
- Because those entries were intentionally written before independent merge verification, their wording still says the replay is staged / needs integration. That wording became stale immediately when PR #148 merged.
- This post-merge integrity branch updates repository truth without changing source history, registry freshness, raw evidence, tools, cases, opportunities, authorization boundaries, or site HTML.
- `docs/WORK_QUEUE.md`, the Aug. 29 `data/integration_queue.json` item, and the append-only handoff should next be finalized to record PR #148 as merged/integrated before Aug. 29 afternoon is replayed. Preserve prior queue and handoff history rather than reconstructing it.

## Current operating priorities

1. Finalize the post-merge coordination wording for PR #148: mark the Aug. 29 morning queue item integrated, update the work-queue P2 row to identify Aug. 29 afternoon as the next gate, and append an integrity handoff recording the exact PR #148 head and post-merge green runs.
2. Independently inspect `intelligence/feeds/2026-08-29-afternoon-source-health.json` against canonical Aug. 29 morning history.
3. Recompute every protected fingerprint from preserved observation text and verify each predecessor against the latest canonical record for that source.
4. If any contributed hash is invalid, preserve the raw snapshot unchanged and create a separate provenance-safe reconciliation rather than rewriting evidence.
5. If valid, replay only evidence-backed Aug. 29 afternoon records, advance only matching registry timestamps, regenerate repository-managed site/source outputs, and require source-history, registry, collection-report, intelligence, Agent Operations/site-data, Core, Intelligence Source Report, Daily Maintenance, and Pages validation before Aug. 30 advances.

## Next handoff

Finalize the PR #148 coordination status history-preservingly, then verify and process Aug. 29 afternoon as the next chronological replay gate. Preserve raw evidence unchanged; if contributed hashes or predecessor links are invalid, create a separate reconciliation rather than rewriting the contribution. Do not advance Aug. 30 or later research until the Aug. 29 afternoon replay and generated user-facing/Agent Operations data are independently green.

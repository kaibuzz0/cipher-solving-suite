# Current Repository State

Last reconciled: 2026-09-09 19:20 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `939ae4c978b8ec26d5fe5a13a481f3a2d7cb4a64`, the merge of PR #151 (`Ops: reconcile rapid research merges`).
- Exact-main Core validation run `34326964442` completed successfully on `939ae4c978b8ec26d5fe5a13a481f3a2d7cb4a64` across Python 3.11, 3.12, and 3.13. The matrix passed the test suite, Python compilation, source-registry/history/report validation, intelligence validation, artifact inventory, 310 migration/reproduction checks, dashboard-data generation, maintenance, diagnostics, and the final failure gate.
- Exact-main Deploy operations dashboard run `34326964528` completed successfully on the same commit.
- Later exact-main Daily Repository Maintenance run `34358781997` and Intelligence Source Report run `34365929258` also succeeded.
- No open repository issues currently block the chronological source-replay lane.

## Canonical source / integration state

- Canonical source history still ends at Aug. 29 morning, `2026-08-29T07:38:35Z`.
- PR #148 remains the last canonical replay: exactly five Aug. 29 morning records for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`, with only those five matching source-registry timestamp advances.
- The preserved raw Aug. 29 morning snapshot remains evidence and was not rewritten by later research merges.
- Aug. 29 afternoon remains the next chronological replay gate. Aug. 30 and later evidence must not advance canonical freshness before it.

## Concurrent / stale contribution state

- PR #152 (`Research: preserve Sep 9 Chainlink window and MemSentry lead`) is a one-file contributed research lane created from stale base `d807fd615dfeb3cdc8d6e254f9409277408ca925`, before PR #151 merged. Its head is `c20c1248ab95e2d7a2826c7e39cae8926d566089`; GitHub currently reports it non-mergeable against current `main`.
- PR #152's ETHOnline, Chainlink, MemSentry, CTF schedule, benchmark, prize, and actionability statements remain contributed evidence, not canonical repository truth. Preserve the contribution when reconciling; do not advance source freshness from it ahead of the Aug. 29 afternoon gate.
- Remaining older open research PRs include #116, #123, #125, #131, and #139. They remain contributed/noncanonical until reconciled against current `main` and processed at their chronological gates.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- The 310 tools remain `experimental`; repository-internal reproduction does not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- Normal tools, toolsets, cases, intelligence, evidence, and opportunity state must flow through canonical registries/manifests/site-data builders rather than bespoke HTML.
- Current exact-main Core and Pages workflows successfully exercised dashboard-data generation and deployment; this is the verified release-health basis for the current commit.

## Security / maintenance state

- Fresh bounded default-branch search found no indexed `shell=True` or `os.system(` use; this is not a complete security audit.
- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- GitHub Actions continue to use major-version action tags such as `actions/checkout@v4` and `actions/setup-python@v5` rather than immutable commit SHAs; action pinning and stronger dependency locking remain supply-chain hardening debt.
- Known root/generated artifact duplicate/orphan work remains preservation-sensitive maintenance, not a deletion task.

## Coordination drift requiring follow-up

- `docs/WORK_QUEUE.md` still describes the Aug. 29 morning replay as staged and awaiting independent merge verification even though PR #148 is already merged.
- `data/integration_queue.json` still contains chronology/status text that predates the rapid research merges and the completed Aug. 29 morning replay; reconcile statuses history-preservingly rather than deleting entries.
- `docs/AGENT_HANDOFF.md` latest stored entry still describes the Aug. 29 morning replay as staged/noncanonical. This append-only journal requires a history-preserving follow-up append; do not replace or truncate prior entries merely to add the new state.
- PR #151 itself is now merged, so any coordination text describing #151 as pending is stale.

## Current operating priorities

1. History-preservingly reconcile `docs/WORK_QUEUE.md`, `data/integration_queue.json`, and `docs/AGENT_HANDOFF.md` to record PR #148 and PR #151 as merged and to represent later research PRs as preserved contributed evidence without promoting their claims.
2. Reconcile stale PR #152 from current `main`, preserving its one-file research contribution without overwriting newer coordination state; rerun validation on the reconciled head before merge consideration.
3. Independently inspect `intelligence/feeds/2026-08-29-afternoon-source-health.json` against canonical Aug. 29 morning history.
4. Recompute every protected fingerprint from preserved observation text and verify each predecessor against the latest canonical record for that source.
5. If any contributed hash is invalid, preserve the raw snapshot unchanged and create a separate provenance-safe reconciliation rather than rewriting evidence.
6. If valid, replay only evidence-backed Aug. 29 afternoon records, advance only matching registry timestamps, regenerate repository-managed site/source outputs, and require source-history, registry, collection-report, intelligence, Agent Operations/site-data, Core, Intelligence Source Report, Daily Maintenance, and Pages validation before Aug. 30 advances.

## Next handoff

First finish the history-preserving coordination reconciliation after PR #151 and the completed Aug. 29 morning replay. Then reconcile PR #152 from current `main` without promoting its claims. After that, independently verify and process Aug. 29 afternoon as the next chronological canonical replay gate. Preserve all merged research artifacts and raw evidence unchanged; no later research claim becomes canonical merely because its PR exists or is eventually merged.

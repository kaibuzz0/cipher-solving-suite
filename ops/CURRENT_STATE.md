# Current Repository State

Last reconciled: 2026-09-09 20:00 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `30b1e93361bf367f32fc7993fb354107bae21e92`, the merge of PR #153 (`Ops: reconcile state after PR #151 merge`).
- PR #153 exact head `937897a5d7c67c91bb168370de5b288de92b8e3c` was mergeable, had no review threads, and passed Core validation run `34394808760` before merge.
- PR #151 exact-main Core validation `34326964442`, Pages deployment `34326964528`, Daily Repository Maintenance `34358781997`, and Intelligence Source Report `34365929258` were all successful on the preceding verified main state.
- No open repository issues currently block the chronological source-replay lane.
- A fresh post-PR153 Pages run has not yet been independently observed in this pass; do not infer final merge-commit Pages health from the pre-merge PR check alone.

## Canonical source / integration state

- Canonical source history still ends at Aug. 29 morning, `2026-08-29T07:38:35Z`.
- PR #148 remains the last canonical replay: exactly five Aug. 29 morning records for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`, with only those five matching source-registry timestamp advances.
- The preserved raw Aug. 29 morning snapshot remains evidence and was not rewritten by later research merges.
- Aug. 29 afternoon remains the next chronological replay gate. Aug. 30 and later evidence must not advance canonical freshness before it.

## Concurrent / stale contribution state

- PR #154 is an active one-file Sep. 9 afternoon research contribution created from current main before PR #153 merged. It is noncanonical research and does not own coordination files or the Aug. 29 replay lane.
- PR #152 (`Research: preserve Sep 9 Chainlink window and MemSentry lead`) remains a stale one-file contributed research lane created from pre-PR151 main. Preserve its contribution when reconciling, but do not treat its Chainlink/ETHOnline/MemSentry/CTF claims as canonical truth or advance source freshness ahead of Aug. 29 afternoon.
- Older open research PRs #116, #123, #125, #131, and #139 remain contributed/noncanonical until reconciled against current `main` and processed at their chronological gates.
- Several later research PRs were already merged as preserved evidence only. Merge status does not promote their contained source, benchmark, prize, security, licensing, event-status, or capability claims to canonical truth.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; `source-history` is `verified`, while the 310 case tools remain `experimental`.
- Active structured cases currently include `20260816-310-btc-challenge` and the later contributed `20260906-pwnsec-ctf-2026` triage case. The PwnSec case is an authorized-event planning lane only; its prize remains TBD and event rules must be re-opened before hands-on work.
- Repository-internal 310 reproduction does not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- Normal tools, toolsets, cases, intelligence, evidence, and opportunity state must flow through canonical registries/manifests/site-data builders rather than bespoke HTML.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- GitHub Actions continue to use major-version action tags such as `actions/checkout@v4` and `actions/setup-python@v5` rather than immutable commit SHAs; action pinning and stronger dependency locking remain supply-chain hardening debt.
- Known root/generated artifact duplicate/orphan work remains preservation-sensitive maintenance, not a deletion task.

## Coordination drift requiring follow-up

- `docs/WORK_QUEUE.md` still describes the Aug. 29 morning replay as staged and awaiting independent merge verification even though PR #148 is merged.
- `data/integration_queue.json` still marks the Aug. 29 morning item `needs-integration` and contains stale open-PR wording for several later research contributions that are now merged as preserved evidence. Reconcile statuses history-preservingly rather than deleting entries or promoting claims.
- `docs/AGENT_HANDOFF.md` latest stored entry still describes the Aug. 29 morning replay as staged/noncanonical. This append-only journal requires a history-preserving follow-up append; do not replace or truncate prior entries merely to add the new state.
- PR #153 is now merged, so any coordination text describing it as pending is stale.

## Current operating priorities

1. History-preservingly reconcile `docs/WORK_QUEUE.md`, `data/integration_queue.json`, and `docs/AGENT_HANDOFF.md` to record PR #148, PR #151, and PR #153 as merged while representing later research as preserved contributed evidence without promoting claims.
2. Independently inspect `intelligence/feeds/2026-08-29-afternoon-source-health.json` against canonical Aug. 29 morning history.
3. Recompute every protected fingerprint from preserved observation text and verify each predecessor against the latest canonical record for that source.
4. If any contributed hash is invalid, preserve the raw snapshot unchanged and create a separate provenance-safe reconciliation rather than rewriting evidence.
5. If valid, replay only evidence-backed Aug. 29 afternoon records, advance only matching registry timestamps, regenerate repository-managed site/source outputs, and require source-history, registry, collection-report, intelligence, Agent Operations/site-data, Core, Intelligence Source Report, Daily Maintenance, and Pages validation before Aug. 30 advances.
6. Reconcile stale one-file research PRs from current main only when their chronology gate is reached; preserve their evidence without accepting stale shared coordination state.

## Next handoff

Finish the history-preserving coordination reconciliation after PR #153, then independently verify and process Aug. 29 afternoon as the next chronological canonical replay gate. Preserve all merged research artifacts and raw evidence unchanged; no later research claim becomes canonical merely because its PR exists or has merged.

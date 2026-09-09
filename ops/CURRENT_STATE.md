# Current Repository State

Last reconciled: 2026-09-09 07:20 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `d807fd615dfeb3cdc8d6e254f9409277408ca925`, the merge of PR #112 (`Research: preserve Sep 1 afternoon source health`).
- Exact-main Core validation run `34306464867` completed successfully on `d807fd615dfeb3cdc8d6e254f9409277408ca925`.
- No open repository issues currently block the chronological source-replay lane.
- A fresh exact-main Pages deployment was not independently observed in this pass; do not infer Pages health solely from prior merge state.

## Canonical source / integration state

- Canonical source history still ends at Aug. 29 morning, `2026-08-29T07:38:35Z`.
- PR #148 remains the last canonical replay: exactly five Aug. 29 morning records for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`, with only those five matching source-registry timestamp advances.
- The preserved raw Aug. 29 morning snapshot remains evidence and was not rewritten by the later research merges.
- Aug. 29 afternoon remains the next chronological replay gate. Aug. 30 and later evidence must not advance canonical freshness before it.

## Rapid research-merge reconciliation

- Since the prior integrity reconciliation, multiple previously contributed/noncanonical one-file research PRs were merged into `main` in rapid succession: PR #146, #144, #141, #136, #103, #106, #109, #120, and #112, plus Sep. 8 research PR #150.
- These merges preserve research/evidence files on `main`; they do **not** by themselves make the contained source, benchmark, prize, security, licensing, event-status, or capability claims canonical or independently verified.
- The rapid merges do not change the canonical source-history gate: Aug. 29 afternoon is still next.
- Previously documented statements that those merged PRs are still open/stale are now coordination drift and must be reconciled history-preservingly.
- Remaining open research PRs include #116, #123, #125, #131, and #139. They remain contributed/noncanonical until independently reconciled at their chronological gates.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- The 310 tools remain `experimental`; repository-internal reproduction does not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- Normal tools, toolsets, cases, intelligence, evidence, and opportunity state must flow through canonical registries/manifests/site-data builders rather than bespoke HTML.

## Security / maintenance state

- Existing targeted checks have found no indexed `shell=True` or `os.system(` use; this is not a complete security audit.
- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- GitHub Actions continue to use major-version action tags rather than immutable commit SHAs; action pinning and stronger dependency locking remain supply-chain hardening debt.
- Known root/generated artifact duplicate/orphan work remains preservation-sensitive maintenance, not a deletion task.

## Coordination drift requiring follow-up

- `docs/WORK_QUEUE.md` still describes the Aug. 29 morning replay as staged and awaiting merge verification even though PR #148 merged.
- `data/integration_queue.json` still describes several now-merged research PRs as open/stale/blocked and therefore no longer reflects repository truth.
- `docs/AGENT_HANDOFF.md` latest stored entry still describes the Aug. 29 morning replay as staged; this append-only journal requires a history-preserving follow-up append.
- These coordination files must be reconciled without deleting prior entries or rewriting contributed research evidence.

## Current operating priorities

1. History-preservingly reconcile `docs/WORK_QUEUE.md`, `data/integration_queue.json`, and `docs/AGENT_HANDOFF.md` to record PR #148 as merged/integrated and the rapid research PRs as preserved evidence on `main` without promoting their claims.
2. Independently inspect `intelligence/feeds/2026-08-29-afternoon-source-health.json` against canonical Aug. 29 morning history.
3. Recompute every protected fingerprint from preserved observation text and verify each predecessor against the latest canonical record for that source.
4. If any contributed hash is invalid, preserve the raw snapshot unchanged and create a separate provenance-safe reconciliation rather than rewriting evidence.
5. If valid, replay only evidence-backed Aug. 29 afternoon records, advance only matching registry timestamps, regenerate repository-managed site/source outputs, and require source-history, registry, collection-report, intelligence, Agent Operations/site-data, Core, Intelligence Source Report, Daily Maintenance, and Pages validation before Aug. 30 advances.

## Next handoff

First reconcile the stale coordination surfaces after the rapid evidence-only research merges. Then verify and process Aug. 29 afternoon as the next chronological canonical replay gate. Preserve all merged research artifacts and raw evidence unchanged; no later research claim becomes canonical merely because its PR is now merged.

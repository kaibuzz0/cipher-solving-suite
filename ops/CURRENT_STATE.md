# Current Repository State

Last reconciled: 2026-09-11 07:21 UTC
Default branch: `main`
Reconciled default-branch head: `63862aec8837dba0ea7271b3412dc79970db3d3c`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot, not a self-referential assertion that the commit containing this file must equal the observed base SHA. A merge of this reconciliation will create a newer commit by definition. That SHA difference alone is not coordination drift; re-open this file only when substantive repository facts, health, chronology, risks, or priorities change.

## Verified health

- This pass reconciled against `63862aec8837dba0ea7271b3412dc79970db3d3c`, the merge of PR #159 (`Research: preserve Sep 10 afternoon DHS challenge lead`).
- PR #159 changed one research snapshot only: `intelligence/feeds/2026-09-10-afternoon-source-health.json`. It did not write canonical source history, advance source-registry timestamps, promote intelligence/opportunities, create an active case, register a tool/toolset, or edit website HTML.
- Exact-main Core validation run `34523668122` completed successfully on `63862aec8837dba0ea7271b3412dc79970db3d3c`.
- The latest observed successful Deploy operations dashboard run is `34520467804` on prior main `a6c6cf915f0f7bb96c6fdc7df8972171718f28d8`. PR #159 only added a raw research feed file and did not touch canonical site-data inputs or Pages code; no newer Pages run was observed for its merge commit in this pass.
- No open repository issues currently block the chronological source-replay lane.
- Governance documents remain aligned that current repository state outranks agent memory, external AI output is contributed work rather than automatically trusted truth, primary evidence must be preserved, and normal tools/toolsets/cases/intelligence/evidence must flow through canonical registries/manifests/site-data builders.

## Canonical source / integration state

- Canonical source history still ends at Aug. 29 morning, `2026-08-29T07:38:35Z`.
- PR #148 is the last canonical replay: exactly five Aug. 29 morning records for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`, with only those five matching source-registry timestamp advances.
- The preserved raw Aug. 29 morning snapshot remains evidence and was not rewritten by later research merges.
- Aug. 29 afternoon remains the next chronological replay gate. Aug. 30 and later evidence must not advance canonical freshness before it.
- `docs/WORK_QUEUE.md` is reconciled in the current integrity branch so it no longer describes the already-merged Aug. 29 morning replay as pending.
- `data/integration_queue.json` still requires a history-preserving reconciliation of stale status/text fields; no queue history should be deleted or used to promote later contributed claims.

## Concurrent / stale contribution state

- PR #159 is merged as preserved Sep. 10 afternoon research only. Its DHS challenge, CTFtime, and ETHOnline assertions remain contributed evidence; merge status does not canonize those claims. Its own body records that the complete DHS rules page was not preserved and that stage payouts, judging/submission details, data/IP terms, and biosafety constraints remain unverified.
- Open PR #157 is a one-file Sep. 10 research/source-health contribution from older main. Its DCP, CTFtime, ETHOnline, package, benchmark, and event claims remain contributed evidence until independently verified and chronologically eligible.
- Open PR #154 is a one-file Sep. 9 afternoon research contribution based on stale main. Preserve its Ledger/ETHOnline, CTFtime, and arXiv observations as contributed evidence only.
- Open PR #152 is a stale one-file Sep. 9 morning contribution. Preserve its Chainlink/ETHOnline/MemSentry/CTF contribution without accepting those claims as canonical truth.
- Older open research PRs #116, #123, #125, #131, and #139 remain contributed/noncanonical and stale relative to current main.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; normal additions must continue through canonical registries/manifests/site-data builders rather than bespoke HTML.
- The active 310 case and its migration/reproduction verification remain internal evidence only; they do not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- The contributed PwnSec case remains authorization-bounded event planning only; current organizer rules control any hands-on work and prize claims remain separate from repository truth.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- Previously verified artifact state remains preservation-sensitive: generated/root images, duplicate groups, orphaned items and case-link debt require hash/provenance-preserving cleanup rather than blind deletion.
- Bounded prior searches found no indexed `shell=True`, `os.system(`, `subprocess.run(`, or literal `BEGIN PRIVATE KEY` matches, but those searches were incomplete and are not a comprehensive secrets/code-security audit.
- GitHub Actions still use major-version action tags such as `actions/checkout@v4`, `actions/setup-python@v5`, and `actions/upload-artifact@v4` rather than immutable commit SHAs; stronger action/dependency pinning remains supply-chain hardening debt.
- Legacy root truthfulness debt remains: `QUICK_START_REAL_MONEY.sh` contains unsourced earnings/payout-ceiling marketing claims and direct external-platform launch instructions; `TOOLS_AUDIT.md` remains historical and uses outdated completion/readiness language. Preserve history and reconcile those claims in a separate docs-only cleanup.

## Coordination drift requiring follow-up

- `docs/WORK_QUEUE.md` is being repaired in this branch to record PR #148 as completed and Aug. 29 afternoon as the next replay gate.
- `data/integration_queue.json` remains dated Sep. 8 and contains stale status/open-PR wording. Reconcile it history-preservingly; do not delete prior entries.
- `docs/AGENT_HANDOFF.md` still ends at the Sep. 8 replay-staging entry on current main. This integrity pass successfully retrieved the full append-only blob, so the handoff should now be appended safely on the same branch rather than reconstructed from partial reads.
- Do not reopen `ops/CURRENT_STATE.md` merely because merging this reconciliation creates a newer SHA; use the reconciled-base field plus material-state checks.

## Current operating priorities

1. Complete the history-preserving coordination repair for `docs/WORK_QUEUE.md`, `data/integration_queue.json`, and `docs/AGENT_HANDOFF.md`; keep PR #159 and all later research as contributed evidence only.
2. Independently inspect `intelligence/feeds/2026-08-29-afternoon-source-health.json` against canonical Aug. 29 morning history.
3. Recompute every protected fingerprint from preserved observation text and verify each predecessor against the latest canonical record for that source.
4. If any contributed hash is invalid, preserve the raw snapshot unchanged and create a separate provenance-safe reconciliation rather than rewriting evidence.
5. If valid, replay only evidence-backed Aug. 29 afternoon records, advance only matching registry timestamps, regenerate repository-managed site/source outputs, and require source-history, registry, collection-report, intelligence, Agent Operations/site-data, Core, Intelligence Source Report, Daily Maintenance, and Pages validation before Aug. 30 advances.
6. Reconcile stale one-file research PRs only when their chronology gate is reached; preserve useful evidence without accepting stale coordination state or unsupported claims.
7. In a separate docs-only cleanup, mark `TOOLS_AUDIT.md` and `QUICK_START_REAL_MONEY.sh` explicitly historical/legacy or otherwise reconcile their claims with current capability/payout-evidence policy without erasing provenance.

## Next handoff

Current `main` is `63862aec8837dba0ea7271b3412dc79970db3d3c`; exact-main Core validation `34523668122` is green. PR #159 is preserved research only and did not advance canonical freshness. The immediate repository-health task is to finish the shared coordination repair and then independently verify the Aug. 29 afternoon snapshot before any later source replay. Preserve all raw and merged research evidence unchanged; no agent-authored source, prize, security, benchmark, solve, or readiness claim becomes canonical merely because its PR exists or has merged.
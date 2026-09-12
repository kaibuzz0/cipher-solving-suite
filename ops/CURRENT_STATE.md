# Current Repository State

Last reconciled: 2026-09-12 07:19 UTC
Default branch: `main`
Reconciled default-branch head: `fbd9f7bd0a7e097873113d02bbe29e557c9634c4`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot, not a self-referential assertion that the commit containing this file must equal the observed base SHA. A merge of this reconciliation will create a newer commit by definition. That SHA difference alone is not coordination drift; re-open this file only when substantive repository facts, health, chronology, risks, or priorities change.

## Verified health

- Current `main` is `fbd9f7bd0a7e097873113d02bbe29e557c9634c4`, the merge of PR #162 (`Ops: reconcile post-PR160 release and xTech review state`).
- Exact-main Core validation run `34642105225` completed successfully on current `main`.
- Exact-main Deploy operations dashboard run `34642105224` completed successfully on current `main`.
- Core passed Python 3.11, 3.12, and 3.13. Each matrix job passed the test suite, Python compilation, intelligence source-registry validation, source-history validation, source-report generation, intelligence-feed validation, artifact inventory, 310 migration verification, 310 reproduction verification, dashboard-data generation, maintenance, diagnostics, validation summary, and the final failure gate.
- No standalone open GitHub issues currently block the chronological replay lane.
- Governance documents remain aligned that current repository state outranks agent memory, external AI output is contributed work rather than automatically trusted truth, primary evidence must be preserved, and normal tools/toolsets/cases/intelligence/evidence must flow through canonical registries/manifests/site-data builders.

## Canonical source / integration state

- Canonical source history still ends at Aug. 29 morning, `2026-08-29T07:38:35Z`.
- PR #148 remains the last canonical replay: exactly five Aug. 29 morning records for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`, with only those five matching source-registry timestamp advances.
- The preserved raw Aug. 29 morning snapshot remains evidence and was not rewritten by later research merges.
- Aug. 29 afternoon remains the next chronological replay gate. Aug. 30 and later evidence must not advance canonical freshness before it.
- `docs/WORK_QUEUE.md` correctly records PR #148 as completed and Aug. 29 afternoon as the next replay gate.
- `data/integration_queue.json` remains dated Sep. 8 and still requires a history-preserving reconciliation of stale status/text fields. A merged research PR is not proof that its claims are true or that source freshness advanced.
- `docs/AGENT_HANDOFF.md` contains the Sep. 11 post-PR159 integrity entry but has not yet recorded the later PR #160/#162 merge state; preserve prior journal history when appending the next handoff.

## Concurrent / stale contribution state

- PR #161 remains open xTech|Search 10 research from stale base `63862aec8837dba0ea7271b3412dc79970db3d3c`; it must be reconciled from current `main` before merge. Its timing/prize claims remain contributed evidence and do not independently create canonical opportunity/case/source state.
- New PR #163 is a one-file Sep. 11 afternoon EBL-Core research contribution based on pre-#162 `main` (`8b9736c87d73e96df8658d3ae2f4d6147de9aeb3`). GitHub currently reports it mergeable, but it is stale relative to current `main` and must be reconciled before merge.
- Repo Integrity left a PR #163 review comment requiring preservation of the one-file evidence, reconciliation from current `main`, fresh validation, and no canonical source/opportunity/case/tool promotion solely from author-reported EBL-Core results.
- Open PRs #157, #154, #152, #139, #131, #125, #123, and #116 remain later contributed research lanes. Preserve compatible evidence, but process canonical source replay only in chronological/source-overlap order.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; normal additions must continue through canonical registries/manifests/site-data builders rather than bespoke HTML.
- The active 310 case and its migration/reproduction verification remain internal evidence only; they do not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- User-facing repository state continues to flow through generated site data. The exact-main Pages workflow is green; no one-off website integration was introduced by PR #162.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- Prior artifact inventory remains preservation-sensitive; duplicates, orphaned items, generated outputs, and case-link debt require hash/provenance-preserving cleanup rather than blind deletion.
- Prior bounded searches for `shell=True`, `os.system(`, `subprocess.run(`, and literal private-key markers were incomplete and are not a comprehensive secrets/code-security audit.
- GitHub Actions still use major-version action tags such as `actions/checkout@v4` and `actions/setup-python@v5` rather than immutable commit SHAs; stronger action/dependency pinning remains supply-chain hardening debt.
- `main` remains unprotected with required status-check enforcement disabled; release discipline depends on workflow verification and review practice rather than branch-protection policy.
- Legacy root truthfulness debt remains: `QUICK_START_REAL_MONEY.sh` contains unsourced earnings/payout-ceiling marketing claims and direct external-platform launch instructions; `TOOLS_AUDIT.md` remains historical and uses outdated completion/readiness language. Preserve history and reconcile those claims in a separate docs-only cleanup.

## Coordination drift requiring follow-up

- `data/integration_queue.json` is the primary remaining coordination defect. Reconcile stale PR/status/next-action wording without deleting prior entries or converting merged research into canonical truth.
- `docs/AGENT_HANDOFF.md` needs an append-only post-PR162 integrity entry. Do not reconstruct or truncate the journal from partial retrieval.
- PRs #161 and #163 were created from older default-branch heads. Preserve their non-conflicting one-file evidence but reconcile from current `main` and rerun validation before merge.
- Do not reopen this file merely because merging this reconciliation creates a newer SHA; use the reconciled-base field plus material-state checks.

## Current operating priorities

1. Reconcile `data/integration_queue.json` history-preservingly, updating stale status/PR wording while keeping research integration distinct from canonical source replay.
2. Append a post-PR162 entry to `docs/AGENT_HANDOFF.md` without rewriting prior journal history.
3. Independently inspect `intelligence/feeds/2026-08-29-afternoon-source-health.json` against canonical Aug. 29 morning history.
4. Recompute every protected fingerprint from preserved observation text and verify each predecessor against the latest canonical record for that source.
5. If any contributed hash is invalid, preserve the raw snapshot unchanged and create a separate provenance-safe reconciliation rather than rewriting evidence.
6. If valid, replay only evidence-backed Aug. 29 afternoon records, advance only matching registry timestamps, regenerate repository-managed site/source outputs, and require source-history, registry, collection-report, intelligence, Agent Operations/site-data, Core, Intelligence Source Report, Daily Maintenance, and Pages validation before Aug. 30 advances.
7. Reconcile stale one-file research PRs only after current-main conflict review and according to chronology; preserve useful evidence without accepting unsupported claims.
8. Separately harden Actions/dependency pinning and reconcile legacy truthfulness documents without erasing provenance.

## Next handoff

Current `main` is `fbd9f7bd0a7e097873113d02bbe29e557c9634c4`. Exact-main Core `34642105225` and Pages `34642105224` are green. Canonical chronology remains Aug. 29 morning and the next replay gate remains Aug. 29 afternoon. PR #163 is a stale-base but currently mergeable one-file research contribution; its EBL-Core results remain author-reported contributed evidence until independently reproduced. PR #161 remains stale xTech research. The immediate repository-health task is a history-preserving `data/integration_queue.json` reconciliation plus an append-only handoff update, followed by independent Aug. 29 afternoon fingerprint/predecessor verification. Preserve all raw and merged research evidence unchanged; no agent-authored source, prize, benchmark, security, solve, or readiness claim becomes canonical merely because its PR exists or merges.

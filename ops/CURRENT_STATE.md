# Current Repository State

Last reconciled: 2026-09-12 08:08 UTC
Default branch: `main`
Reconciled default-branch head: `ce565c7c08f5ae849bfc2805e74529574be46464`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot, not a self-referential assertion that the commit containing this file must equal the observed base SHA. A merge of this reconciliation will create a newer commit by definition. That SHA difference alone is not coordination drift; re-open this file only when substantive repository facts, health, chronology, risks, or priorities change.

## Verified health

- Current `main` is `ce565c7c08f5ae849bfc2805e74529574be46464`, the merge of PR #166 (`Test Aug 29 afternoon source replay readiness`).
- PR #164 first reconciled the post-PR162 coordination snapshot and merged as `4e52ccc426ea2af859fb12d2e6930287b4fa8718`; exact-head Core `34680544151` succeeded.
- Exact-main Core `34682359600` and Deploy operations dashboard / Pages `34682359491` succeeded on PR #164's merge commit.
- PR #166 exact head `6f719e849117f528208432eac0e46945ed7089bd` passed Core `34682416236` and Daily Repository Maintenance `34682416267` before merge.
- Post-merge Core `34682454290` succeeded on current `main` `ce565c7c08f5ae849bfc2805e74529574be46464`.
- No standalone open GitHub issues currently block the chronological replay lane.
- Governance documents remain aligned that current repository state outranks agent memory, external AI output is contributed work rather than automatically trusted truth, primary evidence must be preserved, and normal tools/toolsets/cases/intelligence/evidence must flow through canonical registries/manifests/site-data builders.

## Canonical source / integration state

- Canonical source history still ends at Aug. 29 morning, `2026-08-29T07:38:35Z`.
- PR #148 remains the last canonical replay: exactly five Aug. 29 morning records for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`, with only those five matching source-registry timestamp advances.
- Aug. 29 afternoon remains the next canonical replay gate; PR #166 did not write source history or source-registry freshness.
- The preserved Aug. 29 afternoon snapshot contains exactly one `ethglobal-events` observation at `2026-08-29T19:40:52Z`.
- Build Integration independently recomputed that observation to SHA-256 `361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179` and verified its latest canonical predecessor is the Aug. 29 morning ETHGlobal fingerprint `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c` at `2026-08-29T07:38:35Z`.
- `tests/test_aug29_afternoon_source_readiness.py` now protects the exact snapshot hash, predecessor linkage, canonical uniqueness, and absent-or-exact idempotence contract before replay.
- `docs/WORK_QUEUE.md` correctly records PR #148 as completed and Aug. 29 afternoon as the next replay gate.
- `data/integration_queue.json` remains dated Sep. 8 and still requires a history-preserving reconciliation of stale status/text fields. A merged research PR is not proof that its claims are true or that source freshness advanced.

## Concurrent / stale contribution state

- PR #165 is a Sep. 12 research contribution that updates the existing PwnSec case and preserves a later source-health snapshot; it explicitly does not advance canonical source history and must not bypass the Aug. 29 afternoon replay gate.
- PR #161 remains open xTech|Search 10 research from a stale base and must be reconciled from current `main` before merge.
- PR #163 remains a stale-base Sep. 11 afternoon EBL-Core research contribution; preserve its one-file evidence but require current-main reconciliation and fresh validation before merge.
- Older open research PRs remain contributed evidence lanes and must be reconciled only when chronology/source-overlap order permits.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; `source-history` remains verified and the 310 solver/analyzer/reproduction tools remain explicitly `experimental`.
- Structured active cases remain `20260816-310-btc-challenge` and `20260906-pwnsec-ctf-2026`.
- The 310 case remains internal evidence only and does not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- PwnSec remains an authorization-bounded event case; organizer rules and participant state control any hands-on action, and no prize claim is canonical merely because research exists.
- User-facing repository state continues through generated site data; normal additions must not require bespoke `site/index.html` edits.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- Prior artifact inventory remains preservation-sensitive; duplicates, orphaned items, generated outputs, and case-link debt require hash/provenance-preserving cleanup rather than blind deletion.
- Prior bounded searches for unsafe shell patterns and literal private-key markers were incomplete and are not a comprehensive security audit.
- GitHub Actions still use major-version action tags rather than immutable commit SHAs; stronger action/dependency pinning remains supply-chain hardening debt.
- `main` remains unprotected with required status-check enforcement disabled; release discipline depends on workflow verification and review practice.
- Legacy root truthfulness debt remains in `QUICK_START_REAL_MONEY.sh` and `TOOLS_AUDIT.md`; preserve history and reconcile those claims separately.

## Coordination drift requiring follow-up

- `data/integration_queue.json` is the primary remaining coordination defect. Reconcile stale PR/status/next-action wording without deleting prior entries or converting merged research into canonical truth.
- `docs/AGENT_HANDOFF.md` still needs an append-only entry covering PR #164, PR #166, the independently verified Aug. 29 afternoon fingerprint/predecessor, exact CI, collision handling, and the next replay action. The GitHub connector used in this pass exposes whole-file replacement rather than a safe append mutation; do not reconstruct or truncate the journal from partial state merely to satisfy the update.
- Stale research PRs must be reconciled from current `main` and rerun through validation before merge.
- Do not reopen this file merely because merging this reconciliation creates a newer SHA; use the reconciled-base field plus material-state checks.

## Current operating priorities

1. Reconcile `data/integration_queue.json` history-preservingly while keeping research integration distinct from canonical source replay.
2. Append the missing post-PR166 entry to `docs/AGENT_HANDOFF.md` using a complete-file checkout or other append-safe mechanism.
3. Execute the repository-native replay of `intelligence/feeds/2026-08-29-afternoon-source-health.json`, expecting exactly one `ethglobal-events` history addition at `2026-08-29T19:40:52Z` and one matching registry timestamp advance.
4. Require the new readiness regression plus source-history, registry, collection-report, intelligence, Agent Operations/site-data, Core, Intelligence Source Report, Daily Maintenance, and Pages validation before Aug. 30 advances.
5. Independently verify the replay diff and exact-head CI before merge; preserve the raw snapshot unchanged.
6. Reconcile later research PRs only after current-main conflict review and according to chronology/source overlap.
7. Separately harden Actions/dependency pinning and reconcile legacy truthfulness documents without erasing provenance.

## Next handoff

Current `main` is `ce565c7c08f5ae849bfc2805e74529574be46464`. PR #164 cleared the active shared-state collision and its post-merge Core/Pages runs are green. PR #166 added and merged a deterministic Aug. 29 afternoon replay-readiness regression; exact-head Core `34682416236`, Daily Maintenance `34682416267`, and post-merge Core `34682454290` succeeded. Canonical history itself still ends at Aug. 29 morning. The independently verified next replay is one ETHGlobal observation with fingerprint `361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179` and predecessor `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`. Reconcile the stale integration queue and append the handoff safely, then execute only the native bounded afternoon replay and require full validation before Aug. 30 or later research advances.

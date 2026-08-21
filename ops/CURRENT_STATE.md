# Current Repository State

Last reconciled: 2026-08-21 08:09 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `f61910fa8acf5064f757178688e279232265528d`, the merge of documentation-only PR #38 (`Ops: reconcile state after PR #37 merge`). PR #38 head `f925513f17a417e9f436846131568252ac764537` passed Core validation run `32458426799` before merge.
- PR #37 remains merged and independently integrity-reviewed. `nih-challenge-evidence` stays at `tested`, not `live`.
- Public GitHub Pages is reachable at the Operations Workspace and exposes Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry, prompts, workflow and Agent Operations surfaces.
- `data/integration_queue.json` remains empty and no open repository issues were found in this build pass.
- Open research PR #36 remains isolated to `data/intelligence_sources.json` and `data/source_check_history.json`; it does not overlap the active 310 solver implementation paths.

## Build / integration state

- PR #39 (`Build: integrate portable 310 password candidate solver`) is the current bounded build contribution on branch `agent/310-password-candidate-solver-20260821`.
- The pass identified root `brute_force.py` as broken/unintegrated legacy 310 code: it hard-codes `/root/310_btc_challenge/alpha_row310.bin`, mixes `Crypto` and `Cryptodome` namespaces, contains an undefined `ciphertext` reference in its PBKDF1 fallback, and writes a root-level result file.
- Rather than deleting legacy code without provenance/reference review, PR #39 adds the case-local `research/active-puzzles/20260816-310-btc-challenge/tools/password_candidate_solver.py` and preserves the legacy hint-derived candidate hypothesis in deterministic order.
- Candidate listing and payload validation use only the Python standard library. Optional decrypt mode lazy-loads `pycryptodomex` and tests only the legacy PBKDF2-HMAC-SHA256 / AES-256-CBC hypothesis against validated OpenSSL `Salted__` payloads.
- Malformed base64, non-OpenSSL payloads, invalid arguments and missing optional crypto dependencies fail non-destructively. A result file is written only on a plausible candidate match and only to an explicitly requested path.
- `btc310-password-candidates` is registered in `data/tools.json` at `experimental` maturity and linked to case `20260816-310-btc-challenge`. The maturity is intentionally not promoted because CI verifies deterministic candidate/payload behavior but does not establish the optional decrypt hypothesis as correct.
- The active case metadata now lists the solver as an analysis script and its next action requires provenance verification plus SHA-256 comparison of regenerated row-310 evidence before candidate testing. No puzzle solve is claimed.
- Case documentation was reconciled with current code: `alpha_extract.py` is already portable/parameterized and defaults generated outputs to the managed case evidence directory. The stale README claim that it still hard-coded `/root/...` was removed.
- No bespoke `site/index.html` changes were made. Tool visibility continues through the canonical `data/tools.json` -> generated site-data / Command Site contract.
- PR #39 implementation head `406ef51ded0eabe58157b4e9c37f7e97d4cc267a` passed Core validation run `32461566520` on Python 3.11, 3.12 and 3.13 plus Daily Repository Maintenance run `32461566492`. All matrix jobs passed tests, compilation, source registry/history/feed validation, collection reporting, artifact inventory, 310 migration verification, dashboard-data generation and maintenance.
- A local clone was unavailable because the container could not resolve `github.com`; GitHub-hosted CI is the verification basis for this pass.

## Current research / case state

- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`. Its solver lane is now better integrated, but original challenge source/provenance and regenerated row-310 evidence equality remain required before interpreting decrypt attempts.
- Root `brute_force.py` is preserved as legacy code pending reference/provenance review; it is not a registered working command.
- Research PR #36 remains open with federal challenge source/history updates and should be preserved as a separate research lane.
- NCI ODS Impact Prize remains an evidence-enrichment candidate; exact eligibility, prize, entry/submission criteria and supporting primary-source evidence should be preserved before canonical promotion.
- Cap, Aave V4, Midas and Puffer remain discovery/watch leads only; no security target testing started.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost and deterministic-fixture review.

## Known state / debt

- `password_candidate_solver.py` is `experimental`: deterministic candidate generation and fail-closed payload handling are tested, but the optional PBKDF2/AES hypothesis has not been independently established against verified challenge evidence.
- Root `brute_force.py` and `char_locator.py` remain legacy/unregistered. Continue the solver inventory module-by-module; do not delete them until references/provenance are checked.
- Generated root artifacts still require hash/provenance-preserving relocation. Primary 310 evidence remains protected in place.
- Source freshness debt remains and is separate from this solver pass.
- Existing merged/topic branches remain cleanup candidates but may retain useful provenance or external references.
- GitHub Actions continues to pass while action-runtime deprecation warnings remain bounded maintenance debt.
- After the final coordination commits on PR #39, fresh PR CI must be checked again before the branch is considered ready for independent integrity review.

## Current operating priorities

1. Repo Integrity should independently review PR #39's deterministic candidate ordering, malformed-payload fail-closed behavior, case/tool registration, generated website discovery, and `experimental` maturity boundary before merge.
2. For the 310 case, regenerate `alpha_row310.bin` with the already-portable extractor, compare SHA-256 against preserved migrated evidence, and only then exercise the optional password hypothesis. Treat any plausible plaintext as a hypothesis, not a solve claim.
3. Continue the legacy solver inventory with `char_locator.py` and other unregistered modules, preserving references/provenance before relocation or deletion.
4. Review/reconcile research PR #36 against current `main` without overwriting the solver/build lane.
5. Continue root-artifact migration only with hash/provenance preservation and case-link reconciliation.

## Next handoff

PR #38 was merged first to clear the shared coordination lane. PR #39 now contains the bounded 310 solver integration and its implementation head is green across Core and Daily Maintenance. After this coordination update and the append-only handoff are committed, re-check final-head CI, move PR #39 out of draft if green/mergeable, and leave merge to the independent Repo Integrity pass. No solve, live crypto capability, security finding, or destructive evidence migration should be inferred from this build.

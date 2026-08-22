# Current Repository State

Last reconciled: 2026-08-22 08:12 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `d0ecc6671a24b00fa30f44bed71f004a412fa42f`, the merge of coordination PR #43 after independent PR #42 verification.
- PR #43 final head `6d8188a9b6ca2d27ec3ea0039539649be48c919d` was mergeable and passed Core validation run `32559384728`; it changed only `ops/CURRENT_STATE.md` and was merged before the current build branch was created.
- PR #42 remains merged as `b90d87d4f18e24c56c2d30a7ee7065251d4d4376`; `btc310-character-locator` remains `experimental` and no solve is claimed.
- Public GitHub Pages was previously independently reachable with Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry and Agent Operations surfaces. The existing generic tool-visibility contract remains the required discovery path for new tools.
- `data/integration_queue.json` remains empty and `toolsets/catalog.json` still contains only `repo-factory` at `experimental`.
- Open research PR #44 owns `data/opportunities.json` and `intelligence/feeds/2026-08-22-source-health.json`; the current build branch deliberately does not touch those lanes.

## Build / integration state

- Active build PR: #45, branch `agent/310-reproduction-verifier-20260822`.
- PR #45 adds `scripts/verify_310_reproduction.py`, a non-destructive verifier that runs the existing portable alpha extractor against protected `310_challenge.png` in a temporary directory, hashes all four regenerated alpha outputs, compares them with migrated evidence, and writes only `artifacts/310-reproduction-verification.json`.
- `tests/test_310_reproduction_verifier.py` covers deterministic match, mismatch failure, missing-input fail-closed behavior, and preservation of expected evidence using a synthetic extractor fixture.
- Core CI installs bounded NumPy/Pillow versions, compiles the verifier, runs the real repository reproduction check on Python 3.11/3.12/3.13, uploads per-version reproduction reports, shows the result in the validation summary, and fails the job if reproduction fails.
- Implementation/coordination head `97be73ec0b07c59168c8425deb1071fd1171ac60` passed Core validation run `32561375768` across Python 3.11, 3.12 and 3.13 plus Daily Repository Maintenance run `32561375823`. All Core matrix jobs passed tests, compilation, source registry/history/feed validation, source reporting, artifact inventory, 310 migration verification, the new 310 reproduction check, dashboard-data generation and maintenance.
- `btc310-reproduction-verifier` is registered in `data/tools.json` at `experimental` pending independent integrity review, linked to case `20260816-310-btc-challenge`, and flows through the existing canonical registry/site-data contract without bespoke `site/index.html` changes.
- The active case metadata/README point to the non-destructive verifier as the safe reproduction path.

## Current research / case state

- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`.
- The Python 3.12 reproduction artifact from Core run `32561375768` reports status `pass`, extractor return code 0, and exact matches for all four regenerated alpha artifacts.
- Protected `310_challenge.png`: 3,488,848 bytes, SHA-256 `2f9235c0d7d983da80ac9757f728c0f1ce24ab4763909dda314281510d984e16`.
- Regenerated/migrated `alpha_lsb.bin`: 703,616 bytes, SHA-256 `4a9b97264e0b78704fb79d2049a3c5804e05da31cf175b59e5489edcd0fcb57b`.
- Regenerated/migrated `alpha_pattern.bin`: 1,274 bytes, SHA-256 `20c6ab3d608d65c25239cde155ce88401d07795b98161079037df8af280dcc11`.
- Regenerated/migrated `alpha_2bit.bin`: 1,407,232 bytes, SHA-256 `8a23ff07bdf49964f4805468d0827858c64850b46165d01c34d1e7a908bf1020`.
- Regenerated/migrated `alpha_row310.bin`: 368 bytes, SHA-256 `cffcecf0fc90fb313b58e90ee452427f94204c86970afd297606a0ca46d3f2f8`.
- This closes the repository-internal extraction reproducibility gate: the current portable extractor reproduces the migrated alpha evidence from the protected repository image in the tested environments. It does **not** verify the external provenance of the image or the correctness of any hidden-data/password hypothesis.
- Password/decrypt and character-position hypotheses remain `experimental`; plausible output is not a solve claim.
- PR #44's Code4rena/Sherlock/CTFtime source-health work remains separate research state and has not been absorbed into this build branch.

## Known state / debt

- External source/provenance for `310_challenge.png` remains unresolved and is now the primary evidence gate before treating puzzle hypotheses as source-authentic.
- Root `brute_force.py` and `char_locator.py` remain preserved legacy code pending reference/provenance review and eventual hash-preserving migration decisions.
- Generated root artifacts still require hash/provenance-preserving relocation; primary 310 evidence remains protected in place.
- Source freshness debt remains separate from the solver lane.
- `docs/AGENT_HANDOFF.md` remains append-only and still lacks several preserved entries. The available connected write primitive replaces whole files, so this pass preserves its exact build handoff in PR #45 rather than risk truncating the journal.
- This coordination-only state update moves the PR head after the green implementation run; final-head Core/Maintenance should be rechecked before marking PR #45 ready.

## Current operating priorities

1. Recheck PR #45 final-head Core and Daily Maintenance after this coordination update, then move it to ready-for-review only if green and mergeable.
2. Repo Integrity should independently inspect a reproduction artifact, confirm canonical evidence was not mutated, mismatch/missing-input paths fail closed, the `experimental` capability boundary is appropriate, and `btc310-reproduction-verifier` appears through generated website/Command Site data.
3. Separately verify external source/provenance for `310_challenge.png`; reproducibility alone is insufficient provenance.
4. Reconcile PR #44 independently without overwriting this case/tool lane.
5. Continue legacy solver/root-artifact inventory only with evidence preservation.

## Next handoff

The build pass began from synchronized current `main` after merging green, one-file coordination PR #43. It avoided open research PR #44's paths and chose the documented 310 reproduction gate as the highest-value bounded objective. PR #45 introduces a temporary-workspace reproduction verifier, synthetic deterministic tests, real-image Core CI coverage, canonical tool registration and case linkage without moving primary evidence or hardcoding website HTML. Core `32561375768` and Daily Maintenance `32561375823` are green on head `97be73ec...`; the Python 3.12 uploaded report independently records exact matches for all four regenerated alpha outputs, including row 310 SHA-256 `cffcecf0...f2f8`. External image provenance remains unresolved, so no solve or source-authenticity claim is made. Final-head CI after this state-only update remains the last build-side gate.

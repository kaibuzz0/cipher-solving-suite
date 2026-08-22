# Current Repository State

Last reconciled: 2026-08-22 08:08 UTC
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

- Active build PR: #45, branch `agent/310-reproduction-verifier-20260822`, currently draft pending final-head CI.
- PR #45 adds `scripts/verify_310_reproduction.py`, a non-destructive verifier that runs the existing portable alpha extractor against protected `310_challenge.png` in a temporary directory, hashes all four regenerated alpha outputs, compares them with migrated evidence, and writes only `artifacts/310-reproduction-verification.json`.
- `tests/test_310_reproduction_verifier.py` covers deterministic match, mismatch failure, missing-input fail-closed behavior, and preservation of expected evidence using a synthetic extractor fixture.
- Core CI is extended to install bounded NumPy/Pillow versions, compile the verifier, run the real repository reproduction check on Python 3.11/3.12/3.13, upload per-version reproduction reports, show the result in the validation summary, and fail the job if reproduction fails.
- `btc310-reproduction-verifier` is registered in `data/tools.json` at `experimental` pending green real-image CI, linked to case `20260816-310-btc-challenge`, and intended to flow through the existing canonical registry/site-data contract without bespoke `site/index.html` changes.
- The active case metadata/README now point to the non-destructive verifier as the safe reproduction path.

## Current research / case state

- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`.
- The latest captured PR #42 migration artifact recorded protected `310_challenge.png` SHA-256 `2f9235c0d7d983da80ac9757f728c0f1ce24ab4763909dda314281510d984e16` and migrated `alpha_row310.bin` SHA-256 `cffcecf0fc90fb313b58e90ee452427f94204c86970afd297606a0ca46d3f2f8`.
- PR #45 does not hardcode those values as solve evidence; it compares regenerated files directly with the preserved migrated outputs and emits the observed hashes for independent review.
- External source/provenance for `310_challenge.png` remains a separate unresolved gate. A passing reproduction report only proves the extraction relationship is reproducible under the tested environment.
- Password/decrypt and character-position hypotheses remain `experimental`; plausible output is not a solve claim.
- PR #44's Code4rena/Sherlock/CTFtime source-health work remains separate research state and has not been absorbed into this build branch.

## Known state / debt

- Root `brute_force.py` and `char_locator.py` remain preserved legacy code pending reference/provenance review and eventual hash-preserving migration decisions.
- Generated root artifacts still require hash/provenance-preserving relocation; primary 310 evidence remains protected in place.
- Source freshness debt remains separate from the solver lane.
- `docs/AGENT_HANDOFF.md` remains append-only and still lacks several preserved entries. The available connected write primitive replaces whole files, so this pass will preserve its exact build handoff in PR #45 rather than risk truncating the journal.
- PR #45's real-image reproduction result is not yet claimed green until final-head Core CI completes across all supported Python versions.

## Current operating priorities

1. Let PR #45 final-head Core CI prove or falsify reproduction of all four alpha artifacts across Python 3.11/3.12/3.13; inspect the uploaded reproduction JSON before promoting the verifier beyond `experimental`.
2. Repo Integrity should independently confirm the verifier does not mutate canonical evidence, mismatch/missing-input paths fail closed, observed hashes match preserved evidence, and `btc310-reproduction-verifier` appears through generated website/Command Site data.
3. Separately verify external source/provenance for `310_challenge.png`; reproducibility alone is insufficient provenance.
4. Reconcile PR #44 independently without overwriting this case/tool lane.
5. Continue legacy solver/root-artifact inventory only with evidence preservation.

## Next handoff

The build pass began from synchronized current `main` after merging green, one-file coordination PR #43. It avoided open research PR #44's paths and chose the documented 310 reproduction gate as the highest-value bounded objective. PR #45 introduces a temporary-workspace reproduction verifier, synthetic deterministic tests, real-image Core CI coverage, canonical tool registration and case linkage without moving primary evidence or hardcoding website HTML. Final-head CI is the remaining build-side gate. No solve, private-key generation, external target testing, destructive evidence migration or provenance claim should be inferred from this work.

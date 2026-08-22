# Current Repository State

Last reconciled: 2026-08-22 07:25 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `b90d87d4f18e24c56c2d30a7ee7065251d4d4376`, the merge of PR #42 (`Build: integrate portable 310 character region locator`).
- PR #42 final head `9a4b0c1dae7cc46808e1f56a0dc018d4fe2e4765` was mergeable and passed Core validation run `32522050484` on Python 3.11, 3.12 and 3.13 plus Daily Repository Maintenance run `32522050416` before merge. Every Core matrix job passed the test suite, compilation, source registry/history/feed validation, source collection report, artifact inventory, 310 migration verification, dashboard-data generation and maintenance.
- PR #41 remains merged as `16d62558ba7f6fae0516ab95e798b060a65e166b`; its Structured Totient item remains medium-confidence research, not a security reduction or imported tool claim.
- Public GitHub Pages is reachable at `https://kaibuzz0.github.io/cipher-solving-suite/` and exposes Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry and Agent Operations surfaces.
- `data/integration_queue.json` remains empty, `toolsets/catalog.json` still contains only `repo-factory` at `experimental`, and no open repository issues were found during this integrity pass.
- No open PR remained after PR #42 was merged; this reconciliation branch is intentionally limited to post-merge coordination truth.

## Build / integration state

- `btc310-character-locator` is now integrated through canonical `data/tools.json` at `experimental`, linked to case `20260816-310-btc-challenge`, and covered by the existing generic tool-visibility contract.
- The locator preserves the known-character/hex material as explicitly labeled legacy hypotheses, performs deterministic horizontal edge-density analysis, supports dependency-free ASCII P2 PGM fixtures, lazy-loads Pillow for PNG/JPEG input and crop extraction, and writes JSON/crops only when an explicit output path/directory is supplied.
- `tests/test_310_character_locator.py` exercises direct-script hint output, deterministic P2 region detection, missing-image fail-closed behavior, required-input handling, and explicit-only output writing. Final-head Core CI executed the repository test suite on all supported Python versions.
- Canonical discovery remains intact: `tests/test_tool_visibility_contract.py` derives user-visible tools from `data/tools.json`, verifies Command Site snapshot inclusion and repository-browser source discovery, and verifies Pages/workspace consume the canonical registry. No bespoke `site/index.html` change was introduced for PR #42.
- Root `char_locator.py` remains preserved as legacy/unregistered evidence-bearing code pending reference/provenance review; it was not silently deleted or rewritten.

## Current research / case state

- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`.
- The primary 310 case gate is unchanged: verify original challenge provenance, regenerate row-310 evidence with the portable alpha extractor, compare SHA-256 against preserved migrated output, and only then interpret password-candidate decrypt attempts.
- The character-position hypothesis is testable through the portable locator, but detected edge regions are analysis candidates only and are not solve evidence.
- PR #41 refreshed CTFtime/arXiv/Sherlock/ETHGlobal/federal challenge source state and published arXiv:2608.19191, *The Structured Totient Preimage Problem: Reconstruction, Collisions, and Cryptographic Implications*, at medium confidence. Its ancillary scripts remain an evaluation lead, not imported tooling.
- NCI ODS remains an evidence-enrichment candidate. Cap, Aave V4, Midas and Puffer remain discovery/watch leads only; no security target testing started.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost and deterministic-fixture review.

## Known state / debt

- `btc310-password-candidates` and `btc310-character-locator` remain `experimental`; deterministic CI does not establish the underlying puzzle hypotheses as correct.
- Root `brute_force.py` and `char_locator.py` remain preserved legacy code pending reference/provenance review and eventual hash-preserving migration decisions.
- Generated root artifacts still require hash/provenance-preserving relocation. Primary 310 evidence remains protected in place.
- Source freshness debt remains separate from the solver lane; broader official-source adapters and richer eligibility/prize/submission evidence are still incomplete.
- Action-runtime deprecation warnings remain bounded maintenance debt.
- `docs/AGENT_HANDOFF.md` still lacks the preserved PR #39 integrity and PR #41 research entries plus the PR #42 build/integrity entries because the connected update primitive replaces the full append-only file rather than appending atomically. Their exact text remains preserved in PR #42's body and this reconciliation PR must retain the new integrity handoff for a safe append-capable pass.
- Post-merge Actions/Pages runs for merge commit `b90d87d...` were not yet independently observed in this pass; final PR-head green CI plus live Pages reachability are the current release-health basis.

## Current operating priorities

1. Safely append the preserved PR #39 integrity, PR #41 research, PR #42 build, and PR #42 integrity handoffs to `docs/AGENT_HANDOFF.md` without truncating existing history.
2. Confirm post-merge Core/Maintenance/Pages state for `b90d87d...` when the runs surface; do not infer failure merely from delayed run visibility.
3. For the 310 case, regenerate `alpha_row310.bin`, compare SHA-256 against preserved migrated evidence, and only then test candidate decrypt output.
4. Continue legacy solver/root-artifact inventory without deleting or moving evidence until references and hashes are reconciled.
5. Evaluate the Structured Totient ancillary scripts and `RsaCtfTool/RsaCtfTool` for deterministic-fixture value, overlap, dependencies, license and maintenance cost before importing external code.

## Next handoff

Repo Integrity independently reviewed PR #42 from current repository truth, verified its final-head CI, direct-script test coverage, fail-closed behavior, lazy Pillow boundary, canonical registry/site-discovery contract, case linkage and `experimental` maturity boundary, then merged it as `b90d87d4f18e24c56c2d30a7ee7065251d4d4376`. Public Pages remained reachable. This post-merge branch updates only coordination truth. The next role should safely append the preserved handoffs, inspect post-merge workflow/Pages state when available, and then advance the 310 evidence-hash gate or the next bounded legacy-solver inventory item. No solve, live crypto capability, private-key generation, security finding or destructive evidence migration is implied by this integration.

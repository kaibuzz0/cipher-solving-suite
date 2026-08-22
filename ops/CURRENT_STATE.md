# Current Repository State

Last reconciled: 2026-08-22 19:00 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `89584da98ada2101ced7bab8d480255c8d75b20f`, the merge of PR #45 after PR #44 had already merged.
- PR #44 (`Research: record Code4rena wind-down and source-health changes`) merged as `bf6de08f1daee1c1ceb82cf20a4d85af53dcc9de` and its two-file research lane is present on current `main`.
- PR #45 (`Build: verify 310 evidence reproduction non-destructively`) merged as `89584da98ada2101ced7bab8d480255c8d75b20f`. Its final head `f7415d849dbe90034b5da37ced4a7c1ec2540720` passed Core validation `32561434523` on Python 3.11/3.12/3.13 plus Daily Repository Maintenance `32561434467` before merge.
- There are no open pull requests and no open issues at this reconciliation point.
- The public GitHub Pages Operations Workspace is reachable and exposes Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry, prompts/workflow and Agent Operations surfaces.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental`.

## 310 case / tool state

- `btc310-reproduction-verifier` is integrated through canonical `data/tools.json` at `experimental`, linked to case `20260816-310-btc-challenge`, and uses the existing registry/site-data discovery contract rather than bespoke website HTML.
- PR #45's verified artifact recorded exact regenerated/migrated matches for all four alpha outputs. `alpha_row310.bin` remains 368 bytes with SHA-256 `cffcecf0fc90fb313b58e90ee452427f94204c86970afd297606a0ca46d3f2f8`.
- This establishes repository-internal extraction reproducibility only. External provenance/authenticity for `310_challenge.png` remains unresolved, so password/decrypt/character hypotheses and any solve claim remain unverified/experimental.
- Root `brute_force.py` and `char_locator.py` remain preserved legacy code pending reference/provenance review and hash-preserving migration decisions.

## Research / source-health state

- PR #44 updated canonical `data/opportunities.json` to reflect Code4rena's wind-down and added `intelligence/feeds/2026-08-22-source-health.json` with timestamped observations for `code4rena-contests`, `sherlock-bounties`, and `ctftime-upcoming`.
- The three stored fingerprints were independently recomputed with the repository normalization rule and match the raw snapshot exactly.
- Those observations have **not** yet been replayed into canonical `data/source_check_history.json` / `data/intelligence_sources.json`; the raw snapshot itself says replay is pending. This is now tracked explicitly in `data/integration_queue.json` rather than being allowed to drift silently.
- Do not manufacture freshness by copying timestamps alone. Replay the exact observed strings through `scripts/source_check_history.py record ... --at 2026-08-22T07:42:16Z`, preserve the notes, validate history/registry, build the source report/site data, and only then mark the integration item complete.

## Coordination / governance state

- `AGENTS.md`, `docs/AI_AGENT_INTEGRATION.md`, and `docs/AUTOMATED_AGENT_OPERATIONS.md` remain mutually consistent on current-main authority, canonical registries/site-data discovery, evidence preservation, independent verification, collision avoidance, and bounded PR-based changes.
- No open concurrent PR owns the coordination/source-replay lane.
- `docs/AGENT_HANDOFF.md` is append-only. The connected write primitive available in this integrity pass replaces whole files; because the journal is long and prior history must not be truncated, the exact current handoff is preserved in this PR description rather than risking a destructive rewrite.
- A bounded repository code search for `subprocess` returned no indexed matches in this pass. This is not represented as a complete security audit.

## Known debt

- External provenance for `310_challenge.png` remains the primary 310 evidence gate.
- PR #44 source-health observations still need canonical replay and registry freshness reconciliation.
- Generated root artifacts still require hash/provenance-preserving relocation.
- Broader official-source opportunity/news adapters, catalog freshness, and legacy solver inventory remain incomplete.
- Several historical handoff entries after the latest safely appended journal entry remain preserved in PR descriptions/current-state history rather than the append-only journal because of connector-safe-append limitations.

## Current operating priorities

1. Review/merge the integrity reconciliation PR created from current `main` if CI remains green.
2. Replay the three PR #44 source-health observations through the canonical source-history command, update registry freshness through that replay, validate source/history/report/site-data output, then mark the integration-queue item integrated.
3. Independently verify external provenance for `310_challenge.png` before interpreting solver/decryption output as source-authentic.
4. Continue legacy solver/root-artifact inventory only with evidence and hash preservation.

## Next handoff

Repo Integrity reconciled current `main` after PRs #44 and #45 merged in sequence. Both lanes were preserved; no shared-file conflict was found. PR #45's final head remains the known green verification basis for the new 310 reproduction capability, while the final merge commit did not expose connector-visible workflow runs during this pass. Pages is reachable. The material defect fixed here is coordination drift plus a hidden incomplete integration: PR #44's raw source-health snapshot is merged but still pending canonical source-history/registry replay. An explicit `needs-integration` queue item now records that work and its exact replay requirement. The current integrity branch deliberately does not rewrite source history or claim new freshness without performing the repository command path.
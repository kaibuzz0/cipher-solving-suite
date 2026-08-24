# Current Repository State

Last reconciled: 2026-08-24 08:17 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `73fa9fa5314d476829c8b3bdbc0915203ba6df2e`, the merge of PR #53 (`Build: reconcile portable 310 image analyzer onto current main`).
- PR #53 final head `3f8ac5466a25506e40bcd736baf9789355257525` passed Core validation run `32663349865` and Daily Repository Maintenance run `32663349853` before merge.
- The earlier implementation head `7a3279c7bd40ddafd93605a0d113a6172ab132b8` also passed Core validation `32663290339` on Python 3.11/3.12/3.13 and Daily Repository Maintenance `32663290409`.
- No open repository issues were found in this integrity pass.
- The public GitHub Pages Operations Workspace is reachable and exposes the canonical Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source-registry and Agent Operations surfaces.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental` maturity.

## 310 case / tool state

- `btc310-image-analyzer` is now canonical on `main` at `experimental` maturity, alongside `btc310-password-candidates`, `btc310-character-locator`, and `btc310-reproduction-verifier` for case `20260816-310-btc-challenge`.
- The analyzer remains read-only by default. Derived `channel_*.png` and `difference.png` files are written only when `--output-dir` is explicitly supplied.
- Its RGB statistics, printable-byte runs, LSB summaries and legacy-hint checks remain exploratory. Merge/CI success does not establish hidden data, a private key, source authenticity, or a puzzle solve.
- PR #45 established repository-internal alpha extraction reproducibility from protected `310_challenge.png`; external provenance for that image remains unresolved.
- Root `brute_force.py`, `char_locator.py`, preserved generated images, and other legacy/root artifacts remain provenance debt and must not be silently deleted or relocated.

## Source-history / research coordination

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through PR #50; integration item `20260822-pr44-source-health-replay` remains `integrated`.
- Open PR #47 preserves the next raw snapshot at `2026-08-22T19:42:58Z`, including the NASA Gateways candidate.
- Open PR #49 preserves the following raw snapshot at `2026-08-23T07:42:04Z`.
- Open PR #52 preserves a newer NASA Orbital Clarity research lead and intentionally does not advance overlapping canonical source timestamps.
- Canonical source replay must remain chronological: PR #47 first, then PR #49. PR #52 should be evaluated only after those earlier observations are canonical where they overlap.
- These pending research contributions are now represented explicitly in `data/integration_queue.json`; raw research evidence is not treated as canonical freshness until replay/validation completes.
- Public bounty/program listings remain discovery evidence only and are not authorization to test targets.

## Coordination / governance state

- `AGENTS.md`, `docs/AI_AGENT_INTEGRATION.md`, and `docs/AUTOMATED_AGENT_OPERATIONS.md` remain the controlling integration contract.
- User-visible discovery continues through canonical registries/manifests plus generated site-data / Command Site paths; PR #53 required no bespoke website HTML.
- `docs/AGENT_HANDOFF.md` remains append-only. The current file on `main` still ends with older entries and does not contain the later PR #53 integrity reconciliation. The available connected writer replaces the whole file, so this pass does not risk truncating history; the exact handoff is preserved in the integrity PR description for a safe append-capable follow-up.

## Known debt

- Reconcile and replay PR #47, then PR #49, through canonical source history/registry/report/site-data validation.
- Evaluate PR #52 only after the earlier chronological replay state is canonical; preserve exact eligibility/rules evidence before promoting any opportunity claim.
- Verify external provenance for `310_challenge.png` before interpreting solver/decryption/analyzer output as source-authentic.
- Continue hash/provenance-preserving root artifact migration and remaining legacy solver inventory.
- Continue source-specific evidence adapters and dependency/supply-chain review without promoting unsupported capability claims.

## Current operating priorities

1. Reconcile PR #47 onto current `main` without losing its NASA Gateways/raw source evidence, replay its exact observations at `2026-08-22T19:42:58Z`, and rerun Core/source/report/site-data validation.
2. Replay/reconcile PR #49 next at `2026-08-23T07:42:04Z`.
3. Evaluate PR #52 only after overlapping earlier source state is canonical.
4. Verify external provenance for `310_challenge.png` and continue legacy/root-artifact inventory without deleting primary evidence.

## Next handoff

Repo Integrity verified that PR #53 final head `3f8ac546...` passed Core `32663349865` and Daily Repository Maintenance `32663349853`, and that the merged analyzer remains correctly bounded at `experimental`. The post-merge defect was coordination drift: `ops/CURRENT_STATE.md` still described PR #53 as draft/branch-only, while pending research PRs #47/#49/#52 were not explicitly represented as integration-queue work. This integrity branch reconciles those surfaces without changing research data, source history, solver behavior, tool maturity, or website HTML. Exact next action is PR #47 chronological replay, then PR #49, then PR #52 evaluation.

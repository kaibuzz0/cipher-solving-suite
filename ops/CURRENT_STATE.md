# Current Repository State

Last reconciled: 2026-08-17 19:39 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `d234397d20607a7b4f98cd8df184fcbe382e7d86`, the merge of research PR #23.
- The latest scheduled Intelligence Source Report run `32022878957` and Daily Repository Maintenance run `32017729563` both completed successfully on that main commit.
- GitHub Pages was previously verified built, public, HTTPS-enforced and workflow-backed; canonical user-facing intelligence/source changes continue to flow through the existing generated-data/Pages pipeline rather than one-off HTML edits.
- `data/integration_queue.json` remains empty; no unverified external-agent contribution was promoted during this research pass.
- PR #24 (`Build: add deterministic catalog link health checker`) is open and mergeable from `agent/build-link-health-20260817`; it owns the link-health/source-migration implementation objective and this research branch does not modify that tool work.

## Current research/intelligence state

- `github-search` has now received its first real bounded source check. The pass independently inspected `RsaCtfTool/RsaCtfTool`: GitHub reports the repository public, non-archived, MIT-licensed, Python-based and pushed on August 12, 2026; its README documents broad RSA/CTF attack methods and pytest coverage. It is a tool-evaluation lead, not an automatic dependency adoption.
- `arxiv-cryptography` has now received its first successful real check after the prior timeout. The official cs.CR recent list was reopened and two relevant preprints were inspected directly.
- A high-relevance arXiv preprint, `2608.13792`, analyzes 135 first-half-2026 DeFi incidents and distinguishes project audit history from whether the actual incident path fell inside identified pre-incident audit scope. It is published to the canonical intelligence feed with medium confidence because it is a preprint.
- CTFtime changed materially: PwnSec CTF 2026 is now explicitly marked postponed. A correction/watch item was published so planning does not rely on its previously shown dates; the broader late-August CTF window remains listed.
- Sherlock bug-bounty state changed materially again: Puffer now appears as the most recent bounty, marked Upcoming with a 100,000 USDC payout and Last Updated August 17, 2026. It is published as a watch item only. No Puffer case was created and no target testing was performed.
- Aave V4 remains a previously verified LIVE $2.5M discovery lead and Midas remains a previously verified LIVE 500,000 USDC discovery lead; both still require exact scope/rules preservation before case activation or testing.
- Generic opportunity catalogs were not duplicated or expanded merely because existing registered platforms remained reachable.

## Known state / debt

- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes/provenance before relocation.
- Exact Aave V4 and Midas scope/exclusions/prohibited-technique/severity/submission material remains unpreserved in canonical case evidence.
- Puffer is Upcoming, not a live testing case; exact program scope/rules must be preserved after launch before any consideration of security work.
- `RsaCtfTool/RsaCtfTool` is only a candidate for evaluation. Before integrating it, review dependency/license implications, overlap with existing solvers/toolsets, deterministic fixture value and whether adoption adds enough capability to justify maintenance cost.
- Several 12-hour discovery sources remain due or near-due; only sources actually reviewed in a way that supported a stable check fingerprint were marked fresh in this pass.
- Security opportunity listings are discovery only; public pages, contracts, repositories or bounty listings are not authorization beyond exact published scope/rules.

## Current operating priorities

1. Independently verify PR #24's deterministic link-health/source-migration tool, including direct-script behavior, replay semantics, registry/site-data visibility and bounded live redirect handling before promoting maturity.
2. Preserve exact Aave V4 and Midas Sherlock scope, exclusions, prohibited techniques, severity/reward rules and submission terms before deciding whether either merits an active case.
3. Watch Puffer until it becomes live; only then preserve and review its exact program rules before any case activation.
4. Evaluate `RsaCtfTool/RsaCtfTool` as a possible reusable CTF/crypto tool candidate without automatically importing it; compare overlap, dependencies, license posture and deterministic testability first.
5. Preserve root/legacy evidence and inventory legacy solver modules before cleanup/refactoring.

## Next handoff

The build/integration agent should finish and independently verify PR #24 without losing this newer research state if `main` moves. After link-health work, the next bounded capability decision is whether `RsaCtfTool/RsaCtfTool` adds enough tested RSA/CTF value to justify integration into an existing toolset. Case advancement remains gated on exact published bounty scope/rules; do not test first.

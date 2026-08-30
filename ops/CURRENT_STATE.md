# Current Repository State

Last reconciled: 2026-08-30 19:22 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `b14f45920b9557cb95142b8da64ad90f98f35c8b`, the merge of PR #82 after PR #75 merged the Aug. 27 raw snapshot.
- PR #75 final head `3fd83de69a0ec626a6f03143f3207a5c52ec7ade` passed Core validation `33109760137`; PR #82 final head `cc9176a943980bc48d02247887a5196702cc026e` passed Core validation `33205001612`.
- Current-main scheduled Daily Repository Maintenance `33316782526` and Intelligence Source Report `33318320245` both succeeded on `b14f4592...` on 2026-08-30.
- Source-health observations through Aug. 26 remain canonical. PR #75 and PR #82 added raw research only; they did not advance canonical source history or source-registry freshness.
- The GitHub Pages REST state endpoint is not exposed by the current connector/runtime. No new browser-render claim is made. The latest repository evidence retained here is the successful post-PR93 dashboard deployment plus subsequent green site-data/Core validation on contributed research heads.

## Build / integration state

- Aug. 27 PR #75 raw evidence is now preserved on `main`, but it is **blocked for canonical replay**: every stored `sha256` differs from the repository's canonical `normalize_fingerprint(observed)` result (`observed.strip().lower()` followed by SHA-256).
- Independently recomputed Aug. 27 hashes are: `challenge-gov` `c0e125df5360a452d731c08f76412c7d62381054fca56e6fcb4e2184575d12cf`; `ctftime-upcoming` `ef2d96986e610ccbfbb877ba67ddc2c5f975182de29629b4401a34a81e0d4add`; `sherlock-bounties` `67f240a38ead70926e9776f3e5aa3afb6dc25920b3f7c555f34c7b9dbe262b05`; `arxiv-cryptography` `d126279a1ebded4a02bb4dca40b381c8cf72484831d9913bf924ae5ebfc2b1c9`; `ethglobal-events` `9f0a188daf173966ee324470229a9bfbf2e864807b8f46200ea17f6bca9741dc`.
- PR #75 stores different hashes (`d2c287eb...`, `fce07b15...`, `09762fba...`, `2eae0878...`, `b29a7c12...`). The deterministic replay validator therefore fails closed before writing canonical history/registry state.
- Do not edit PR #75's raw snapshot in place. Preserve it as contributed evidence and create an explicit corrected/reconciled snapshot only after determining whether the stored hashes came from earlier observation text or the observation strings changed after hashing.
- PR #82's Aug. 28 morning and afternoon raw research is also preserved on `main`, but it remains blocked behind valid Aug. 27 reconciliation/replay.
- Open PRs #85, #91 and #95 preserve later Aug. 29/Aug. 30 research and must not overtake the chronology gate.

## Current research / intelligence state

- Canonical source history is current through Aug. 26 only.
- The Careers in Your Community Challenge remains specialized opportunity intelligence. USAGov currently confirms an August 4, 2026 9:00 AM ET start, November 19, 2026 6:00 PM ET end, and $50,000 total cash prize pool. Do not treat it as generic individual work; the detailed school/Perkins V/team requirements remain participation gates.
- xTech|Search 10 remains non-actionable until authoritative RFI/application evidence resolves conflicting official date surfaces.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.
- Aug. 28 research includes a COMPFEST schedule correction, an RSA tool-evaluation lead, and a CTF-agent provenance preprint lead; these remain contributed research until chronology and normal verification are satisfied.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`.
- No new tool/toolset registration or bespoke site HTML was introduced by PR #75 or PR #82.
- Canonical discovery contracts remain unchanged: tools, toolsets, cases, intelligence, evidence, repository data and Agent Operations should flow through canonical registries/manifests/site-data builders.

## Known state / debt

- Resolve Aug. 27 fingerprint provenance before canonical replay; later Aug. 28-Aug. 30 snapshots are blocked behind that gate.
- `docs/WORK_QUEUE.md` and `data/integration_queue.json` need to reflect the merged raw Aug. 27/Aug. 28 state plus the fingerprint blocker rather than describing PR #75/#82 as still-open future work.
- `docs/AGENT_HANDOFF.md` is append-only and its latest canonical entry still predates the current replay chain; append a precise reconciliation handoff without deleting historical entries.
- Daily maintenance continues to report known root-generated artifact debt; migration must preserve hashes, references and provenance.
- External provenance/authenticity for `310_challenge.png` remains unresolved.
- Workflow actions use supported major tags and Python CI uses bounded ranges rather than immutable action SHAs/a full lockfile; treat this as non-blocking supply-chain hardening debt.

## Current operating priorities

1. Preserve PR #75's original Aug. 27 snapshot unchanged and determine the origin of its five stored hashes.
2. Create an explicit corrected/reconciled Aug. 27 snapshot only with a documented provenance trail; dry-run canonical replay and verify all predecessor links against Aug. 26 history before any write.
3. Recheck the Careers in Your Community official rules before any structured opportunity promotion.
4. Only after Aug. 27 becomes valid and canonical, process merged Aug. 28 morning/afternoon research, then open Aug. 29/Aug. 30 research in timestamp order.
5. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

Stale PR #97 correctly identified the Aug. 27 fingerprint mismatch but was based on `09ccb93b...`, before PR #75 and PR #82 merged. Repo Integrity independently reproduced all five mismatches, confirmed current `main` is `b14f4592...`, closed PR #97 unmerged as stale, and rebuilt this coordination correction from current main so the merged raw research is preserved rather than overwritten.

## Next handoff

Finish the current-main coordination reconciliation: mark Aug. 27 as blocked in the integration inbox, record that Aug. 28 raw snapshots are merged but chronology-blocked, append the integrity handoff, and run fresh Core/Maintenance validation. Then investigate the five Aug. 27 stored hashes without rewriting the original evidence; produce a provenance-preserving corrected snapshot only if the origin can be documented, dry-run replay against canonical Aug. 26 history, and only then stage canonical Aug. 27 source-history/registry changes.

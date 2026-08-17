# Current Repository State

Last reconciled: 2026-08-17 07:23 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Latest `main` commit inspected: `cb98f15caa294e4f54be1e8db5bffc62cb6072eb` (`Merge pull request #21 ... Command site: export repository tree metadata`).
- Core validation run `31981879956` passed on Python 3.11, 3.12, and 3.13. Each matrix job passed the test suite, core compile checks, intelligence source/history validation, collection report generation, intelligence validation, artifact inventory, 310 migration verification, dashboard-data generation, and maintenance check.
- Pages workflow run `31981879953` passed for the same `main` commit. GitHub Pages reports `built`, public, HTTPS-enforced, and workflow-backed at `https://kaibuzz0.github.io/cipher-solving-suite/`.
- No open pull requests or open GitHub issues were present at this reconciliation point.
- Canonical tool registry exists at `data/tools.json`; canonical intelligence source/feed/history files and `data/integration_queue.json` are active.
- `toolsets/catalog.json` currently registers the reusable `repo-factory` toolset as experimental.
- The repository is connected to `kaibuzz0/Git-hub-command-site` through `scripts/export_command_site_snapshot.py`; PR #21 added bounded repository-tree metadata while preserving the existing canonical tools, toolsets, cases, intelligence, evidence, prompts, and Agent Operations snapshot surfaces.
- Direct-script execution of `scripts/export_command_site_snapshot.py` is covered by `tests/test_command_site_snapshot.py`.
- Repository code-search checks used in this pass found no `subprocess`, `shell=True`, `os.system`, `eval`, or `exec` matches in the queried indexed code surface. Treat this as a bounded search result, not a formal security proof.

## Integration reconciliation in progress

- This integrity pass found that the documented Command Site snapshot exporter was not registered in the canonical `data/tools.json` registry even though it is an agent/operator-facing direct-script command and is independently tested.
- Branch `agent/integrity-reconcile-command-site` registers the exporter as a verified integration tool so normal website/tool discovery remains data-driven rather than special-cased.
- `data/integration_queue.json` is currently empty; no contributed item is waiting for integration review.

## Current research/intelligence state

- Challenge.gov was sunset on March 30, 2026. The stable `challenge-gov` source ID now points to the official USA.gov active federal challenges page for compatibility.
- USA.gov lists the Connecting Talent to Opportunity Challenge through April 1, 2028 with $15,000,000 in total cash prizes; eligibility is specialized and must be checked on the hosting competition page before treating it as directly actionable.
- ETHGlobal's official calendar lists ETHOnline 2026 for September 4-16, followed by Tokyo and Mumbai events later in 2026.
- Sherlock bounty discovery records include current LIVE programs such as Midas; listings are discovery leads only and do not authorize testing beyond the exact published program scope/rules.

## Known state / debt

- Generated/legacy root artifacts remain a documented P1 cleanup item. The repository still contains large root research images/binaries; preserve hashes/provenance and migration verification before relocation.
- Link-health/catalog freshness automation remains P2 work and is important because the Challenge.gov migration demonstrated real source drift.
- Legacy solver inventory/input-output/dependency documentation remains P2 work.
- Several merged topic branches remain on the remote, including `feature/command-site-repository-tree` and multiple older `agent/*` branches. No open PR currently depends on them. Treat them as cleanup candidates only after confirming no preserved evidence or active external workflow references them; do not delete them automatically.
- The GitHub Pages UI should continue to derive normal tools/toolsets/cases/intelligence/evidence and Agent Operations data from canonical files/manifests rather than one-off HTML.

## Current operating priorities

1. Finish and review the scoped Command Site tool-registry reconciliation PR; confirm CI and Pages/site-data generation still pass with the new registry entry.
2. Continue deterministic link-health/source-migration tooling and real source checks for due/never-checked lanes.
3. Preserve and inventory remaining root/legacy artifacts before any relocation or deletion.
4. Inventory legacy solver modules and reconcile shared tools/toolsets with canonical registries where appropriate.
5. Keep `main`, CI, Pages, registries, handoffs, Command Site snapshot output, Agent Operations data, and documentation aligned.

## Next handoff

The next integrity/build role should inspect the reconciliation PR CI. If green, merge it and verify that the newly registered `command-site-snapshot` tool appears through the normal generated tool/Command Site data path. Do not manually hardcode it into website HTML. After that, link-health/source-migration tooling remains the highest-value bounded integration debt.

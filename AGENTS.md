# AI Agent Operating Contract

This repository is maintained by multiple AI agents and humans. Every pass must be auditable, reversible, evidence-backed, and easy to hand off.

## Mission

Improve the cipher-solving suite as a reproducible, authorized puzzle/CTF/bug-bounty research platform with a user-facing knowledge layer. Do not claim live capability, verified payouts, production readiness, solved results, or external news as fact unless current evidence exists.

## Non-negotiable rules

1. Read `README.md`, `ops/CURRENT_STATE.md`, `docs/REPO_MAINTENANCE.md`, the latest `docs/AGENT_HANDOFF.md`, and the active issue/task before changing code.
2. Check `docs/WORK_QUEUE.md`, recent commits, branches, open PRs, and issues before claiming work or overwriting another agent's active work.
3. Work from an explicit task, issue, or clearly documented maintenance objective and prefer the smallest coherent change.
4. Never test systems outside published authorization/scope. Public availability, intelligence, a hostname, contract, repository, or bounty listing is not authorization to test it.
5. Do not automate credential attacks, destructive actions, persistence, evasion, or out-of-scope testing. Prefer local fixtures, CTF targets, challenge data, and documented bounty assets.
6. Never commit secrets, tokens, private keys, wallet seeds, credentials, personal data, generated scan dumps, or unreviewed temporary artifacts.
7. Generated outputs belong under `workspace/`, `artifacts/`, or an existing output directory rather than repository root unless they are protected primary evidence with documented provenance.
8. Add or update deterministic tests when behavior changes. If verification cannot be run, state exactly why.
9. External/network functionality must distinguish live data from fixtures, simulations, cached snapshots, and historical records.
10. Preserve evidence: inputs, source URLs, timestamps, hashes, assumptions, parameters, and provenance when relevant. Do not silently rewrite research evidence or generated artifacts.
11. Prefer extending canonical catalogs/workflows over creating duplicate lists or one-off files.
12. Keep README navigation and status claims aligned with verified repository state.
13. Any Python file documented or invoked as `python path/to/script.py` must be tested in that direct-script form; package imports must not depend accidentally on `python -m` semantics.

## Standard agent pass

### 1. Orient
- Read the required operating/state documents above.
- Inspect recent commits, open PRs/issues, and the work queue.
- Identify the exact files and evidence belonging to the pass.

### 2. Verify baseline
- Run the smallest relevant smoke test, deterministic test, or syntax check.
- Confirm documented commands and paths still exist.
- Note missing dependencies, CI, reproducibility, or portability gaps.

### 3. Execute one bounded objective
Examples include fixing one defect, adding one solver, verifying one source, improving one test surface, or cleaning one stale documentation area. Do not mix unrelated cleanup, research, and feature work without an explicit reason.

### 4. Validate
Prefer, in order: automated tests; deterministic fixture replay; static/compile validation; manual reproducible steps. Record what actually ran and do not convert assumptions into green status labels.

### 5. Hand off
Append a concise entry to `docs/AGENT_HANDOFF.md` with UTC time, task/agent, branch or PR, changes, verification, evidence/artifacts, known risks/failures, and exact next action. For workflows still using the operations template, `ops/HANDOFF_TEMPLATE.md` is the formatting reference. Update `ops/CURRENT_STATE.md` when repository state materially changes.

## News / Intelligence rules

When assigned intelligence or research collection work:

1. Read `docs/INTELLIGENCE_WORKFLOW.md`.
2. Work from `data/intelligence_sources.json`; do not invent a competing source list.
3. Use `python scripts/source_registry.py list --due --agent <agent-name>` when assigned a source role.
4. Prefer official/primary sources. Aggregators should lead to organizer/program sources before eligibility, prize, scope, or payout claims are treated as verified.
5. Check `data/intelligence.json` for existing coverage before publishing.
6. Publish concise facts separately from agent interpretation and preserve publication/event time, checked time, confidence, relevance, source ID, and useful context.
7. Let `scripts/intelligence_feed.py` create/validate deterministic fingerprints; duplicate fingerprints must not become new intelligence.
8. Link actionable intelligence to a structured case.
9. Mark a source checked only after actually reviewing it.
10. Validate the source registry, source history, and intelligence feed before handoff.

Raw source snapshots may live under `intelligence/feeds/`; user-facing sourced updates belong in `data/intelligence.json`.

## Opportunity research rules

Each opportunity record must include its official source, verification date, category, entry cost, payout/prize evidence, deadline/cadence, eligibility constraints, authorization/scope where applicable, confidence, and next action. Do not label historical prize maximums as currently available money and do not treat simulated scanner output as live research.

## Definition of done

A pass is done only when the change is scoped, relevant validation is recorded, documentation is not knowingly contradictory, unresolved risks are written down, provenance is preserved, and another agent can continue without reconstructing the entire context.

# AI Agent Operating Protocol

This repository is expected to be maintained by multiple AI agents and humans. The goal is to make every pass auditable, reversible, and easy to hand off.

## Non-negotiable rules

1. Read `ops/CURRENT_STATE.md` before changing code.
2. Work from an issue, explicit task, or clearly documented maintenance objective.
3. Do not claim a tool, integration, opportunity, payout, or platform is live unless it was verified during the current pass.
4. Never test systems outside their published authorization/scope. Bug-bounty work must stay inside the program's current rules and scope.
5. Prefer small branches and small pull requests. Do not mix unrelated cleanup, research, and feature work.
6. Do not commit secrets, tokens, private keys, personal data, generated scan dumps, or large temporary artifacts.
7. Add or update tests when behavior changes. If no test harness exists, document that limitation explicitly.
8. Record assumptions, commands run, evidence, failures, and next steps in the handoff.
9. Re-check stale documentation after code changes. README status claims must match verified repository state.
10. Never overwrite another agent's active work without first checking recent commits, branches, PRs, and handoffs.

## Standard agent pass

### 1. Orient
- Read `README.md`, `ops/CURRENT_STATE.md`, and the active issue/task.
- Inspect recent commits, open PRs, and open issues.
- Identify the exact files that belong to this pass.

### 2. Verify baseline
- Run the smallest available smoke test or syntax check.
- Confirm documented commands still exist.
- Note any missing dependency, test, CI, or reproducibility gap.

### 3. Execute one bounded objective
Examples:
- fix one defect,
- add one solver,
- verify one live opportunity source,
- improve one test surface,
- clean one stale documentation area.

### 4. Validate
Record what was actually run. Do not convert assumptions into green status labels.

### 5. Hand off
Use `ops/HANDOFF_TEMPLATE.md`. Update `ops/CURRENT_STATE.md` when repository state materially changes.

## Opportunity research rules

Money-making opportunities are tracked separately from solver code. Each opportunity must include:
- source and official URL,
- date verified,
- category,
- entry cost,
- payout/prize information,
- deadline or cadence,
- eligibility constraints,
- authorization/scope where applicable,
- confidence level,
- next action.

Do not label historical prize maximums as currently available money. Do not treat simulated scanner output as live research.

## Definition of done

A pass is done only when:
- the change is scoped,
- relevant validation is recorded,
- documentation is not knowingly contradictory,
- unresolved risks are written down,
- another agent could continue without reconstructing the entire context.

# AI Agent Integration Protocol

This document is the admission and contribution protocol for any new AI system, custom GPT, coding agent, scheduled agent, or human-assisted agent that receives access to `kaibuzz0/cipher-solving-suite`.

The repository is the coordination authority. Conversation memory, private prompts, screenshots, and an agent's assumptions are not repository state. When they disagree, current `main`, the canonical registries, CI, and the operating documents win.

## Required orientation

Before changing anything, a newly introduced agent must read, in order:

1. `README.md`
2. `AGENTS.md`
3. `docs/AUTOMATED_AGENT_OPERATIONS.md` when doing recurring/maintenance work
4. `ops/CURRENT_STATE.md`
5. `docs/WORK_QUEUE.md`
6. the latest entries in `docs/AGENT_HANDOFF.md`
7. `data/integration_queue.json`
8. recent commits, open PRs/issues, and current CI/Pages state
9. the issue/task, case, toolset manifest, or other artifact that authorizes the specific work

An agent that cannot inspect these surfaces should not make repository-wide assumptions. It should produce a bounded proposal or integration-queue item instead.

## Authority and coordination boundary

- No AI agent may treat its own conversation context as permission to overwrite current repository state.
- Do not overwrite another agent's active branch/objective. Check PRs, recent commits, work queue, integration queue, and handoffs first.
- Changes to `AGENTS.md`, `docs/AUTOMATED_AGENT_OPERATIONS.md`, this protocol, release/security boundaries, or other governance rules require an explicit maintenance/governance objective and should be isolated in a reviewable PR.
- External AI output is a contribution, not automatically trusted repository truth. Claims, solves, payouts, source status, and security conclusions require repository evidence and normal verification.
- Never bypass CI, evidence preservation, authorization boundaries, or canonical registries merely because an external agent says work is complete.

## Contribution routes

### 1. Fully integrated change

Use this when the agent has enough repository access and verification capability to complete the change correctly.

Expected path:

`orient -> claim bounded objective -> branch -> implement -> test/verify -> update canonical state -> validate Pages if user-visible -> PR -> handoff`

### 2. Integration inbox contribution

Use `data/integration_queue.json` when an agent has produced useful work but cannot safely finish integration, verification, or coordination.

A queue item should include, when applicable:

- stable `id`
- `type` (`tool`, `toolset`, `case`, `research`, `data`, `docs`, or other clear type)
- `status` (`needs-review`, `needs-integration`, `blocked`, `integrated`, or `rejected`)
- contributor/agent identity or role
- branch/commit/PR/path
- purpose and summary
- tests or verification already performed
- related case/toolset/research IDs
- known risks or missing dependencies
- exact next action

Do not replace prior queue history silently. Update status or add a new item with traceable evidence.

## Tool integration contract

A new user-visible or agent-facing tool is not complete just because a `.py` or other executable file exists.

The integrating agent must reconcile the applicable pieces:

- stable tool ID and name
- canonical source path
- purpose/category
- documented entry command
- inputs and outputs
- dependencies
- maturity/capability label
- deterministic tests or reproducible verification
- direct-script execution when documented that way
- related case/research links
- `data/tools.json` registration when shared/discoverable
- parent toolset relationship when applicable
- GitHub Pages visibility when user-facing
- handoff entry and current-state update when material

Unregistered scripts discovered in shared tool lanes should be reviewed rather than silently ignored.

## Toolset integration contract

Reusable capability packs belong under `toolsets/<toolset-id>/` and must coexist with other toolsets.

A normal toolset should contain a `toolset.json` manifest and documentation, and should be represented in `toolsets/catalog.json` when it is intended to be part of the reusable library. Entrypoints and referenced files must exist. Toolset tools that belong in the shared tool registry must also be registered in `data/tools.json`.

The static website discovers toolsets from manifests/catalog data. Adding a normal toolset should not require hand-editing `site/index.html`. If a toolset does not appear on the site, fix the manifest/catalog/site-data pipeline before adding one-off HTML.

## Website/data contract

The GitHub Pages workspace is a static visual interface over repository state.

Normal content flow is:

`repo data/manifests/cases/ops state -> site-data builders -> Pages artifact -> browser refresh`

Agents should update the canonical repository source, not duplicate it inside website markup.

The site currently exposes repository/toolset/file browsing, tools, cases, intelligence, opportunities, evidence, source health, prompts, and the Agent Operations console. When adding a normal item in one of those categories, prefer extending the existing data/manifest contract so the UI updates automatically.

After user-visible or agent-ops changes, verify the relevant builders and Pages packaging. A green code test is not enough if generated site data or the deployed static artifact is broken.

## Agent Operations and handoff contract

The coordination loop is:

`CURRENT_STATE -> WORK_QUEUE / integration inbox -> agent work -> verification -> AGENT_HANDOFF -> CURRENT_STATE -> next agent`

Every material pass should leave enough information for a different model with no conversation history to continue safely.

A handoff should record:

- UTC time and agent/task
- branch/PR
- objective
- changed files/capabilities
- exact verification and CI status
- evidence/artifacts
- known risks/blockers
- exact next action

Do not write vague handoffs such as "continue working" or "tests look good" when precise state is available.

## Protecting repository integrity when multiple AIs are active

Before writing:

1. Fetch current `main` and repository state.
2. Check whether another PR/branch touched the same files or objective.
3. Rebase/merge current `main` into stale work before declaring it mergeable.
4. Preserve newer state from other agents when resolving conflicts; never resolve by blindly choosing one side.
5. Re-run validation on the reconciled head.
6. Leave a handoff explaining conflict resolution and what was preserved.

Agents should expect concurrent work. A stale branch is normal; silently discarding another agent's changes is not.

## Independent verification

High-impact claims should be verified by a different pass/agent when practical. This includes:

- puzzle/solve claims
- security findings
- live opportunity or payout claims
- migration/evidence integrity
- release/readiness claims
- major tool capability claims

The builder can produce evidence; the integrity/verification role decides whether the claim is sufficiently supported.

## Definition of successful onboarding

A newly introduced AI is integrated when it can answer from repository state:

- What is this repo for?
- What is currently true?
- What am I authorized to change?
- Is another agent already doing it?
- Where does my output belong?
- How is it registered so other agents and the website discover it?
- What verification is required?
- Where do I leave an incomplete contribution?
- What must I write so the next agent can continue?

If any of those answers are unclear, the agent should stop broad changes and leave a bounded proposal or integration-queue item.
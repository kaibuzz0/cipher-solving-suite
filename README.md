# Cipher Solving Suite v3.1.0

A multi-agent research and operations hub for cipher puzzles, CTFs, hackathons, authorized bug-bounty/audit work, coding challenges, GitHub research, reusable prompts, notes, and earnings tracking.

**Start here.** This README is the repository front door for humans and AI agents. Use it to navigate the repo, find commands, locate active work, and understand the operating workflow before changing anything.

## Quick navigation

| I want to… | Go here |
|---|---|
| Open the human-facing dashboard | [`site/index.html`](site/index.html) |
| See what an AI agent must read/do | [`AGENTS.md`](AGENTS.md) |
| Find the next task | [`docs/WORK_QUEUE.md`](docs/WORK_QUEUE.md) |
| Read the latest agent notes | [`docs/AGENT_HANDOFF.md`](docs/AGENT_HANDOFF.md) |
| Understand repo maintenance rules | [`docs/REPO_MAINTENANCE.md`](docs/REPO_MAINTENANCE.md) |
| Start a new puzzle/challenge/research case | [`docs/CASE_WORKFLOW.md`](docs/CASE_WORKFLOW.md) |
| Generate a standardized case folder | [`scripts/new_case.py`](scripts/new_case.py) |
| Browse money/skill opportunity links | [`data/opportunities.json`](data/opportunities.json) |
| Browse reusable AI prompts | [`data/prompts.json`](data/prompts.json) |
| Search opportunities from terminal | [`tools/opportunity_finder.py`](tools/opportunity_finder.py) |
| Track attempts/earnings | [`tools/earnings_tracker.py`](tools/earnings_tracker.py) |
| Create a timestamped opportunity snapshot | [`tools/scanning/opportunity_scanner.py`](tools/scanning/opportunity_scanner.py) |
| Run the main command router | [`suite.py`](suite.py) |
| Run repo hygiene checks | [`scripts/maintenance_check.py`](scripts/maintenance_check.py) |
| Run core tests | [`tests/test_core.py`](tests/test_core.py) |
| Inspect active research | [`research/active-puzzles/`](research/active-puzzles/) |
| Inspect solver modules | [`solvers/`](solvers/) |
| Inspect generated/active work | [`workspace/`](workspace/) |
| Inspect CI | [`.github/workflows/ci.yml`](.github/workflows/ci.yml) |
| Inspect daily maintenance automation | [`.github/workflows/daily-maintenance.yml`](.github/workflows/daily-maintenance.yml) |
| Inspect Pages deployment | [`.github/workflows/pages.yml`](.github/workflows/pages.yml) |

## Agent start sequence

Every AI or human agent should use this order:

1. **README.md** — orient and navigate.
2. **AGENTS.md** — read operating and authorization rules.
3. **docs/AGENT_HANDOFF.md** — learn what the previous agent did.
4. **docs/WORK_QUEUE.md** — choose/claim the smallest useful task.
5. **Open PRs/issues** — avoid duplicated or conflicting work.
6. **Relevant code/data/research files** — inspect before editing.
7. **Tests / maintenance checks** — verify before handoff.
8. **Append a handoff entry** — leave exact next steps for the next agent.

## Command center

```bash
# Repository status / command router
python suite.py --status

# Create a standardized new case
python scripts/new_case.py --name "Puzzle 310 follow-up" --type puzzle --source "source name" --url "https://example.com/challenge"

# Opportunity discovery from the shared catalog
python suite.py --opportunities
python tools/opportunity_finder.py --list
python tools/opportunity_finder.py --search crypto
python tools/opportunity_finder.py --category hackathon

# Earnings / attempt tracking
python tools/earnings_tracker.py stats

# Timestamped catalog snapshot (not a live scrape)
python suite.py --scan

# Health / validation
python suite.py --maintenance
python -m unittest discover -s tests -v
```

## What works now

- `suite.py` — top-level status and command router.
- `data/opportunities.json` — canonical opportunity/link catalog used by CLI and website.
- `data/prompts.json` — reusable AI prompt library.
- `tools/opportunity_finder.py` — list/search/filter/open catalog entries.
- `tools/earnings_tracker.py` — record attempts and verified earnings.
- `tools/scanning/opportunity_scanner.py` — timestamped catalog snapshots; deliberately **not labeled as live scraping**.
- `scripts/new_case.py` — standardized challenge/opportunity case generator.
- `docs/CASE_WORKFLOW.md` — case lifecycle, evidence, attempts, verification, and handoff rules.
- `AGENTS.md` — operating contract for AI and human agents.
- `docs/AGENT_HANDOFF.md` — append-only agent journal.
- `docs/WORK_QUEUE.md` — shared claimable work queue.
- `docs/REPO_MAINTENANCE.md` — maintenance rules and definition of done.
- `scripts/maintenance_check.py` — deterministic hygiene/compile checks.
- `tests/test_core.py` — deterministic catalog, earnings, and case-generation tests.
- `site/` — static Operations Hub dashboard deployed through GitHub Pages after merge/configuration.

## Repository map

```text
cipher-solving-suite/
├── README.md                    # FRONT DOOR + navigation
├── AGENTS.md                    # agent rules / authorization boundary
├── suite.py                     # top-level command router
├── data/
│   ├── opportunities.json       # canonical opportunity/link catalog
│   └── prompts.json             # reusable AI prompts
├── docs/
│   ├── AGENT_HANDOFF.md         # append-only notes between agents
│   ├── CASE_WORKFLOW.md         # standardized challenge/case lifecycle
│   ├── REPO_MAINTENANCE.md      # maintenance / definition of done
│   └── WORK_QUEUE.md            # shared work claims and priorities
├── site/                        # GitHub Pages Operations Hub
├── tools/                       # opportunity, earnings and scanning tools
├── scripts/
│   ├── maintenance_check.py     # repository hygiene checks
│   └── new_case.py              # creates standardized case directories
├── tests/                       # deterministic validation
├── research/                    # active cases, research and solutions
├── intelligence/               # timestamped feeds / snapshots
├── solvers/                     # solving modules
├── workspace/                   # active/generated work
└── legacy/                      # older consolidated material
```

## Where new things belong

Do not create another random root-level file when an existing lane fits.

- New opportunity/platform link → `data/opportunities.json`
- Reusable AI prompt → `data/prompts.json`
- New puzzle/challenge/bounty/research investigation → create a case with `scripts/new_case.py`
- Active challenge/case research → `research/active-puzzles/<case-id>/`
- Successful/reproducible solution → `research/solutions/`
- Timestamped discovery/feed output → `intelligence/feeds/`
- Solver code → `solvers/` or the appropriate existing tool module
- Temporary/generated work → `workspace/` or `artifacts/`
- Agent-to-agent notes → `docs/AGENT_HANDOFF.md`
- Future work → `docs/WORK_QUEUE.md`
- Stable process/rules → `docs/`

## Standard case workflow

When an opportunity becomes real work, convert it into a case rather than scattering notes across the repository. A generated case contains `case.json`, `README.md`, `notes.md`, `attempts.md`, and `evidence/`.

That gives agents one place to preserve source URLs, authorization, evidence, hypotheses, commands, failed attempts, outcomes, ownership, and next actions. See [`docs/CASE_WORKFLOW.md`](docs/CASE_WORKFLOW.md).

## Opportunity pipeline

The catalog is a launchpad, not a promise of payout. It includes categories such as bug bounties, Web3 audit contests, CTFs, cryptography/security training, hackathons, government prize challenges, and GitHub research.

Availability, prizes, eligibility, rules, and scopes change. Verify those facts on the official linked page before investing time or testing a target.

## Security authorization boundary

Security tooling is for authorized CTFs, labs, audits, puzzles, and bug-bounty programs. Before testing a real target, save the official rules/scope and confirm the asset/action is allowed. A public hostname, contract, repository, or IP address is **not** authorization by itself.

## Static Operations Hub

`site/` is the human-facing dashboard. It exposes opportunities, tools and commands, reusable AI prompts, agent workflow/handoffs, and research launch links.

`.github/workflows/pages.yml` assembles the site with the same JSON catalogs and publishes it through GitHub Pages on `main` changes. The repository Pages setting may need to be set to **GitHub Actions** once.

## Validation and maintenance

Pull requests run Python 3.11, 3.12, and 3.13 unit tests plus compile and maintenance checks through `.github/workflows/ci.yml`.

The daily maintenance workflow checks missing required files, Python compile failures, version drift, generated files at repository root, and suspicious secret-like filenames. Findings become cleanup work; automation does not silently delete research evidence.

## Known cleanup debt

Older generated images/binaries and legacy research still exist at the root. They should be inventoried with hashes and references before relocation so research provenance is preserved. Older research documents may also contain stale payout/platform claims and should be treated as historical notes until revalidated.

## Mission

The repository should help a human or AI agent quickly answer:

- What legitimate opportunity should we investigate next?
- What tools do we already have?
- What has already been tried?
- What evidence and authorization do we have?
- What did the previous agent learn?
- What is broken or missing?
- What is the next highest-value piece of work?

License: MIT

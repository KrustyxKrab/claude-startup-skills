# Claude Startup Skills

Three Claude Code skills that take a rough idea from first sentence to investor-ready Figma pitch deck — using structured research, a 5-stage validation pipeline, and Figma MCP integration.

---

## Skills at a Glance

| Skill | What it does | Run when |
|-------|-------------|----------|
| `/startup-research` | Researches your idea across 8 dimensions in parallel — competitors, market size, trends, regulatory risk, patents, customer pain — and writes a Research Briefing | You have a new idea |
| `/startup-validator` | 5-stage validation pipeline with enforced gate criteria. Produces interview scripts, Excel models, and a pitch deck outline where every claim traces to evidence | You're ready to validate |
| `/startup-pitch-deck` | Builds a professional 10-slide Sequoia-format deck directly inside Figma using your validator output | You want investor-ready slides |

```
/startup-research ──► Stage 0 ──► Stage 1 ──► Stage 2 ──► Stage 3 ──► Stage 4 ──► Synthesis
       │              Idea        Problem     Solution     Market     Business      Pitch Deck
  Research Briefing  Intake     Validation  Validation   Validation    Model      + Scorecard
                                                                                      │
                                                                             /startup-pitch-deck
                                                                              (Figma via MCP)
```

---

## Install

### One-command (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/KrustyxKrab/claude-startup-skills/main/install.sh | bash
```

This clones the repo, symlinks all three skills into `~/.claude/skills/`, and installs Python dependencies.

### Manual

```bash
git clone https://github.com/KrustyxKrab/claude-startup-skills.git ~/.claude/startup-skills
cd ~/.claude/startup-skills

# Link skills
ln -sfn "$(pwd)/startup-research"   ~/.claude/skills/startup-research
ln -sfn "$(pwd)/startup-validator"  ~/.claude/skills/startup-validator
ln -sfn "$(pwd)/startup-pitch-deck" ~/.claude/skills/startup-pitch-deck

# Python dependencies (used by background data scripts)
pip install pytrends openpyxl
```

### Options

```bash
./install.sh --skill startup-research   # Install a single skill
./install.sh --no-python                # Skip Python deps
./install.sh --list                     # Show available skills
```

Restart Claude Code after installing. Skills appear in the `/` menu immediately.

---

## Usage

### 1. Research

```
/startup-research I want to build a SaaS tool for freelance designers to manage client feedback
```

Claude asks 5 targeted questions, then researches 8 dimensions in parallel using subagents:

- Existing competitors and market gaps
- Market size and growth rate (TAM/SAM/SOM)
- Customer pain points (Reddit, HN, Quora)
- Industry trends and "Why Now" factors
- Technology feasibility (GitHub, blog posts)
- Regulatory and legal environment
- Business model precedents (pricing, revenue models)
- Adjacent innovation and IP activity

**Output:** `[idea-slug]/[slug]-research-briefing.md` + optional Excel data files

---

### 2. Validate

```
/startup-validator
```

Works through 5 stages sequentially. Claude handles all analysis autonomously — you run the experiments and paste results back.

| Stage | Core question | Key outputs |
|-------|--------------|-------------|
| **0 — Idea Intake** | What's the positioning and riskiest assumption? | T1: Idea Framing, Assumption Map |
| **1 — Problem Validation** | Does this problem exist and is it painful enough? | T2: Problem Report, interview scripts, tracker |
| **2 — Solution Validation** | Will people change behavior for this solution? | T3: Experiment Cards, T4: Validation Report |
| **3 — Market Validation** | Is the market big and reachable? | T5: Market Sizing (Excel), T6: Competitive Matrix, T7: Why Now |
| **4 — Business Model** | Can we build a sustainable business? | T8: Unit Economics (Excel), T9: Pricing Analysis |
| **Synthesis** | Ready to pitch? | T10: Scorecard, T11: Pitch Deck Outline, T12: Risk Register |

Gate criteria are enforced — you cannot advance to Stage 2 without meeting Stage 1 thresholds. Every pitch deck claim links back to a completed validation template.

---

### 3. Build the Deck

```
/startup-pitch-deck my-idea-slug
```

Requires the [claude-talk-to-figma MCP](startup-pitch-deck/references/setup-guide.md) running. Claude reads all validator output, confirms 5 key data points per slide, then builds all 10 slides in Figma using exact pixel positions, RGB values, and typography from the design system.

---

## API Keys

All keys are optional — scripts gracefully skip unavailable sources and print the signup link.

| Service | Key required | Free | Get key |
|---------|-------------|------|---------|
| World Bank | No | — | Always works |
| BLS | No | — | Always works |
| SEC EDGAR | No | — | Always works |
| crt.sh (domain saturation) | No | — | Always works |
| pytrends (Google Trends) | No key, needs install | — | `pip install pytrends` |
| FRED | Yes | ✓ | [fred.stlouisfed.org](https://fred.stlouisfed.org/docs/api/api_key.html) |
| Census Bureau | Yes | ✓ | [api.census.gov](https://api.census.gov/data/key_signup.html) |
| PatentsView | Yes | ✓ | [patentsview.org/apis/api-key](https://patentsview.org/apis/api-key) |
| NewsAPI | Yes | ✓ | [newsapi.org/register](https://newsapi.org/register) |

Add to your shell profile (`~/.zshrc` or `~/.bashrc`):

```bash
export FRED_API_KEY=your_key
export CENSUS_API_KEY=your_key
export PATENTSVIEW_API_KEY=your_key
export NEWS_API_KEY=your_key
```

---

## What Gets Generated

Running all three skills produces this folder structure:

```
my-idea-slug/
├── my-idea-slug-research-briefing.md    # Research Briefing (12 sections)
├── my-idea-slug-competitive-scan.xlsx   # Domain saturation, SEC filings, patents
├── my-idea-slug-market-data.xlsx        # FRED / World Bank / BLS data
├── my-idea-slug-trends.xlsx             # Google Trends + NewsAPI
├── my-idea-slug-patents.xlsx            # Patent landscape
│
├── stage-0/
│   └── idea-framing.md                  # T1: Geoffrey Moore positioning + Assumption Map
│
├── stage-1/
│   ├── interview-scripts.md             # Mom Test / stakeholder scripts per archetype
│   ├── interview-tracker.xlsx           # Tracking table for all interviews
│   └── problem-validation-report.md     # T2: Findings, severity matrix, commitment signals
│
├── stage-2/
│   ├── experiment-cards.md              # T3: Experiment design + success criteria
│   ├── landing-page-copy.md             # B2C: Fake Door copy
│   ├── outreach-templates.md            # B2B: Cold email + LOI templates
│   └── solution-validation-report.md    # T4: Results, conversion rates, learnings
│
├── stage-3/
│   ├── my-idea-slug-market-sizing.xlsx  # T5: 3-method TAM/SAM/SOM (live Excel formulas)
│   ├── my-idea-slug-competitive-matrix.xlsx  # T6: Competitor positioning (sortable)
│   └── market-analysis.md              # T7: Porter's Five Forces + Why Now brief
│
├── stage-4/
│   ├── my-idea-slug-unit-economics.xlsx # T8: LTV:CAC, payback, churn, sensitivity
│   ├── my-idea-slug-pricing-analysis.xlsx  # T9: Van Westendorp analysis
│   └── business-model-slides.md        # Slide-ready business model content
│
└── synthesis/
    ├── validation-scorecard.md          # T10: Stage scores, risks, bias alerts
    ├── pitch-deck-outline.md            # T11: Sequoia 10-slide with evidence links
    └── risk-register.md                 # T12: Risk tracking table
```

---

## Architecture

### Subagent Orchestration

The research skill uses parallel subagents to research all 8 dimensions simultaneously, not sequentially. Each dimension is an independent task — market sizing doesn't depend on competitor research. Parallel execution cuts research time from ~20 minutes to ~5 minutes.

The validator uses a similar pattern for background scans: market data, competitive domains, and trend analysis all run as concurrent background tasks while Claude handles the interactive conversation with the founder.

### Environment Detection

Skills detect the runtime environment automatically:

| Environment | Output mode |
|-------------|------------|
| Claude.ai / cowork | Interactive HTML charts rendered inline |
| Claude Code (terminal) | Files saved to disk, 3–5 bullet summary in terminal |

### B2B/B2C Routing

Every stage of the validator adjusts automatically based on archetype:

| | B2C | B2B SMB | B2B Enterprise | Marketplace |
|--|-----|---------|----------------|------------|
| Interviews needed | 20–30 | 10–15 | 10–15 (economic buyers) | Both sides |
| Success signal | Emotional intensity | Quantified cost | Budget commitment | Both-side commitment |
| Experiment type | Fake Door / Crowdfunding | Concierge MVP | Pilot program | Concierge |
| LTV:CAC target | >3:1 | >3:1 | >5:1 | Varies |

---

## Figma Setup

The `/startup-pitch-deck` skill requires the `claude-talk-to-figma` MCP. See the [setup guide](startup-pitch-deck/references/setup-guide.md) for installation instructions.

Once running, the skill builds 10 slides (1280×720px, Sequoia format) using an exact design system — specific RGB values, Inter typography, pixel positions — so the output is consistent and production-quality.

---

## Updating

```bash
cd ~/.claude/startup-skills
git pull origin main
```

Or re-run the one-liner installer — it updates in place.

---

## License

MIT

# Claude Startup Skills

Two Claude Code skills for structured startup research and validation.

---

## Skills

### `/startup-research`
Researches a startup idea across 8 dimensions in parallel — competitors, market size, customer pain points, trends, technology, regulatory environment, business model precedents, and adjacent innovation. Uses web search plus free public APIs (World Bank, BLS, SEC EDGAR, Google Trends, PatentsView). Produces a Research Briefing that feeds directly into `/startup-validator`.

### `/startup-validator`
Five-stage validation pipeline with explicit gate criteria at each step. Covers problem validation, solution validation, market sizing, business model, and synthesis. Generates interview scripts, Excel workbooks for market sizing and unit economics, and a Sequoia-format pitch deck outline where every claim traces back to a completed validation stage.

```
/startup-research → Stage 0 → Stage 1 → Stage 2 → Stage 3 → Stage 4 → Synthesis
                     Idea     Problem   Solution   Market   Business   Pitch Deck
                    Intake   Validation Validation  Sizing    Model    + Scorecard
```

---

## Install

```bash
git clone https://github.com/KrustyxKrab/claude-startup-skills.git
cd claude-startup-skills
ln -sfn "$(pwd)/startup-research" ~/.claude/skills/startup-research
ln -sfn "$(pwd)/startup-validator" ~/.claude/skills/startup-validator
pip install pytrends openpyxl
```

Both skills appear in Claude Code's `/` menu immediately after install.

---

## Usage

```
/startup-research I want to build [your idea]
```

Claude asks five questions, researches all 8 dimensions, and saves a Research Briefing to `[idea-slug]/[idea-slug]-research-briefing.md`.

```
/startup-validator
```

Works through the five stages sequentially. Claude handles the analysis (interview scripts, competitor matrices, Excel models) — you run the experiments and paste back results. Gate criteria are enforced; you don't advance until the current stage meets the threshold.

---

## API Keys

All keys are optional. Scripts skip unavailable sources and print the signup link.

| Service | Key required | Get key |
|---------|-------------|---------|
| World Bank | No | — |
| BLS | No | — |
| SEC EDGAR | No | — |
| crt.sh (domain saturation) | No | — |
| pytrends (Google Trends) | No key, install needed | `pip install pytrends` |
| FRED | Free | [fred.stlouisfed.org](https://fred.stlouisfed.org/docs/api/api_key.html) |
| Census Bureau | Free | [api.census.gov](https://api.census.gov/data/key_signup.html) |
| PatentsView | Free | [patentsview.org/apis/api-key](https://patentsview.org/apis/api-key) |
| NewsAPI | Free | [newsapi.org/register](https://newsapi.org/register) |

```bash
export FRED_API_KEY=your_key
export PATENTSVIEW_API_KEY=your_key
export CENSUS_API_KEY=your_key
export NEWS_API_KEY=your_key
```

---

## License

MIT

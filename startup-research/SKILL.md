---
name: startup-research
description: Autonomous startup idea research using web search and free APIs. Call this skill FIRST when a user presents a startup or business idea, BEFORE running startup-validator. Researches existing solutions, market context, industry trends, adjacent innovations, customer segments, regulatory environment, and technology feasibility. Triggers on: "I have an idea for...", "is there a market for...", "what do you think of this business..."
argument-hint: "[brief idea description]"
allowed-tools: WebSearch, WebFetch, Bash(python3 *)
---

## What this skill does

Turn a rough startup idea into a structured Research Briefing by:
1. Asking the founder targeted questions to understand the idea
2. Autonomously researching the idea across 8 dimensions using web search and free APIs
3. Synthesizing findings into a Research Briefing that feeds into `startup-validator`

This skill does **not** judge, score, or validate. It gathers and structures information.

---

## Operating Principles

Follow these throughout every interaction — they override any default behavior:

1. **Idea first** — Open by inviting the founder to describe their vision. Never lead with business mechanics, classification, or administrative questions. Archetype and market questions follow after understanding the idea.

2. **Environment-aware output** — Detect whether running in Claude.ai (browser/cowork) or Claude Code (terminal):
   - **Claude.ai / cowork:** Render charts and visuals directly as interactive HTML in the chat. Structured text (reports, templates) can be rendered inline with good formatting.
   - **Claude Code (terminal):** All structured content goes to files (`[idea-slug]/[filename].md`). Only questions, confirmations, and 3–5 bullet summaries appear in the terminal.
   - **Detection signal:** If the user is typing in a browser chat or mentions "cowork", use interactive output. If running via CLI or `/startup-research`, use file-first output.

3. **Interactive charts in Claude.ai** — When in Claude.ai or cowork, generate inline HTML charts for:
   - Trend lines (Google Trends data → line chart)
   - Competitor matrix (bubble or scatter chart)
   - Market sizing (TAM/SAM/SOM funnel or bar chart)
   - Patent filing trend by year (bar chart)
   Do not narrate what charts you will make — just produce them.

4. **File-first output in terminal** — Save every output to `[idea-slug]/[filename].[md|xlsx]`. State the filename before generating it. Return 3–5 bullets summarizing the key findings.

5. **Background work stays silent** — Never display script paths or shell commands. Ask: "Should I run a background [competitive / market / trend] scan?" If yes, run it, save results to file or render as chart, return a bullet summary.

6. **Act, don't suggest** — State actions as done: "I've drafted…" / "I started…" / "Here's the…". Never "My recommendation is…" or "You might want to consider…".

7. **Results as bullets** — All research output summarized in 3–7 bullets. Full detail in files or interactive visuals.

## API Keys

Scripts use these optional API keys for richer data. All have graceful fallbacks — the script still runs without them, skipping that data source and printing a one-line message.

| Service | Key required? | Get key | Fallback |
|---------|--------------|---------|---------|
| Google Trends (pytrends) | No key, but needs install | `pip install pytrends` | Skipped with install hint |
| NewsAPI | Optional | https://newsapi.org/register (free) | Skipped with note |
| FRED (Federal Reserve data) | Yes (free) | https://fred.stlouisfed.org/docs/api/api_key.html | Clear error + link |
| Census Bureau | Yes (free) | https://api.census.gov/data/key_signup.html | Clear error + link |
| PatentsView | Yes (free) | https://patentsview.org/apis/api-key (instant) | Skip message + link |
| World Bank | None | — | Always works |
| BLS (Bureau of Labor Statistics) | None | — | Always works |
| SEC EDGAR | None | — | Always works |
| crt.sh (domain saturation) | None | — | Retry + fallback link if 503 |

Pass keys as CLI flags (`--fred-key`, `--census-key`, `--patents-key`, `--news-key`) or as environment variables (`FRED_API_KEY`, `CENSUS_API_KEY`, `PATENTSVIEW_API_KEY`, `NEWS_API_KEY`).

---

## Phase 1: Structured Idea Intake

Start with **Tier 1 questions** (always ask all five). Begin Phase 2 research in parallel after collecting Tier 1 answers — do not wait for all questions.

**Tier 1 — Essential (always ask)**

1. "Describe your idea in 2-3 sentences. What does it do and who is it for?"
2. "What problem does this solve? How do you know this problem exists?"
   - If they can't articulate the problem → flag for Stage 1 of validator
3. "How do people currently deal with this problem today?"
   - "They don't" = yellow flag
4. "Why you? What unique insight, experience, or advantage do you bring?"
5. "Who is your ideal first customer? Be as specific as possible."
   - "Everyone" = nobody. Push for specificity.

**Tier 2 — Context-dependent (ask if relevant)**

6. "Is this B2B or B2C? Or both?" → shapes entire research direction
   - **Marketplace detection:** If the idea connects two distinct groups (e.g., professionals + consumers, supply + demand, service providers + buyers), ask: "Is one side providing supply and the other side paying? Which side is harder to acquire?" → classify as **Marketplace/Platform** and confirm explicitly with the founder before starting research. Do not infer — state the classification and ask for confirmation.
7. "What geography/market are you targeting first?"
8. "Do you have any evidence of demand already?" (conversations, waitlist, LOIs)
9. "What's the rough revenue model you're imagining?"
10. "Is there a technology or trend that makes this possible now but wasn't 2-3 years ago?"
11. "What's the biggest risk you see with this idea?"
12. "Have you seen anything similar? Who might be a competitor?"

**Tier 3 — Deep context (experienced founders only)**

13. "What does success look like in 12 months? 3 years?"
14. "What would make you abandon this idea?"
15. "Who would you need on your team that you don't have?"

---

## Phase 2: Autonomous Research (8 Dimensions)

Research all 8 dimensions simultaneously — do not complete one before starting the next. Before starting, ask: "Should I also run a background data scan (market data, competitive domains, trends)?" — run scripts only if the founder says yes, then save results to file and return a bullet summary.

### Dimension 1: Existing Solutions & Competitors
- Web search: `[problem] software/tool/app`, `[keywords] alternatives`, `best [category] tools 2025 2026`
- Search Product Hunt, G2, Capterra, Crunchbase / AngelList
- **B2B:** Also search G2, Gartner Magic Quadrant, Capterra
- **B2C:** Also search App Store rankings, consumer review sites
- If background scan approved: run competitive scan script → save to `[idea-slug]/[slug]-competitive-scan.xlsx` (sheets: Domains, SEC Filings, Patents)
- Terminal summary: 3–5 bullets on top competitors and market gaps

### Dimension 2: Market Context & Size
- Web search: `[industry] market size`, `[category] TAM`, `[industry] growth rate 2025 2026`
- If background scan approved: run market data script → save to `[idea-slug]/[slug]-market-data.xlsx`
- Terminal summary: 3–5 bullets on market size, growth rate, key data sources

### Dimension 3: Customer Segment Intelligence
- Search Reddit, Quora, Hacker News for organic problem discussions
- Search for industry surveys, relevant communities and associations
- Compile pain point quotes (anonymized)
- If 10+ pain points found: save to `[idea-slug]/[slug]-customer-intelligence.xlsx` (columns: Pain Point | Source | Quote | Frequency Signal | Severity 1–5)
- Terminal summary: top 3–5 pain points with frequency signal

### Dimension 4: Industry Trends & "Why Now"
- If background scan approved: run trend analysis → save to `[idea-slug]/[slug]-trends.xlsx` (sheets: Trends, Related Queries, News)
- Look for regulatory changes, technology shifts, behavioral changes, inflection points
- Terminal summary: 3–5 bullets on direction and key inflection points

### Dimension 5: Technology & Feasibility
- Search GitHub for relevant open-source repos (check star count + activity)
- Look for technical blog posts and case studies
- Terminal summary: build complexity assessment + key risks in 3–5 bullets

### Dimension 6: Regulatory & Legal Environment
- Web search: `[industry] regulations [country]`, `[category] compliance requirements`
- Flag GDPR, HIPAA, PCI-DSS, or industry-specific mandates
- Terminal summary: key regulatory flags only

### Dimension 7: Business Model Precedents
- Research how 3–5 comparable companies price and monetize
- Terminal summary: pricing range + dominant model in 3–5 bullets

### Dimension 8: Adjacent Innovation & Inspiration
- Look for solutions to the same problem in adjacent industries
- If background scan approved: run patent landscape → save to `[idea-slug]/[slug]-patents.xlsx`
- Terminal summary: 3–5 bullets on adjacent approaches and IP activity

---

## Output: Research Briefing

Generate using the template in `references/briefing-template.md`.

**Output location:** `[idea-slug]/[idea-slug]-research-briefing.md`
- The slug is 2–4 lowercase-hyphenated words from the core idea
- Examples: `equipment-aware-fitness-app/equipment-aware-fitness-app-research-briefing.md`
- Save the file directly — don't paste it into the terminal
- In the terminal: state the filename + 5–7 bullet highlights from the briefing

The Research Briefing feeds directly into `startup-validator` Stage 0.

---

## Additional resources

- Structured question bank: [references/question-bank.md](references/question-bank.md)
- Research dimension strategies: [references/research-dimensions.md](references/research-dimensions.md)
- Research Briefing output template: [references/briefing-template.md](references/briefing-template.md)
- Trend analysis script: [scripts/trend_analysis.py](scripts/trend_analysis.py) — `python3 scripts/trend_analysis.py --keywords "kw1,kw2" --excel trends.xlsx`
- Market data script: [scripts/market_data.py](scripts/market_data.py) — `python3 scripts/market_data.py --source fred|worldbank|bls|census --excel market-data.xlsx`
- Competitive scan script: [scripts/competitive_scan.py](scripts/competitive_scan.py) — `python3 scripts/competitive_scan.py --keywords "kw" --excel competitive-scan.xlsx`
- Patent landscape script: [scripts/patent_landscape.py](scripts/patent_landscape.py) — `python3 scripts/patent_landscape.py --query "concept" --excel patents.xlsx`
- Excel export helper: [scripts/excel_utils.py](scripts/excel_utils.py) — shared by all scripts; requires `pip install openpyxl`

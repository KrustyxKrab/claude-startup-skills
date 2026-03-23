---
name: startup-research
description: Autonomous startup idea research using web search, free APIs, and parallel subagents. Call this skill FIRST when a user presents a startup or business idea, BEFORE running startup-validator. Researches existing solutions, market context, industry trends, adjacent innovations, customer segments, regulatory environment, and technology feasibility. Triggers on: "I have an idea for...", "is there a market for...", "what do you think of this business..."
argument-hint: "[brief idea description]"
allowed-tools: WebSearch, WebFetch, Bash(python3 *), Task
---

## What this skill does

Turn a rough startup idea into a structured Research Briefing by:
1. Asking the founder targeted questions to understand the idea
2. Launching parallel subagent tasks to research all 8 dimensions simultaneously
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

5. **Parallel subagents for research** — Launch all 8 research dimensions as simultaneous Task calls, not sequential operations. Collect results, then synthesize. See "Subagent Orchestration" section below.

6. **Background scans via scripts** — Ask: "Should I also run background data scans (market data, competitive domains, trends)?" If yes, run scripts in parallel with web research tasks; save results to files.

7. **Act, don't suggest** — State actions as done: "I've drafted…" / "I started…" / "Here's the…". Never "My recommendation is…" or "You might want to consider…".

8. **Results as bullets** — All research output summarized in 3–7 bullets in the terminal. Full detail in files or interactive visuals.

---

## Visual Feedback Standards

Use consistent status headers in terminal output so the founder can track progress at a glance:

```
━━━ RESEARCHING [idea name] ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  [PHASE 1 of 3]  Idea intake
  [PHASE 2 of 3]  Parallel research (8 dimensions)
  [PHASE 3 of 3]  Synthesis → Research Briefing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Dimension status during parallel research:
```
  ✓  Competitors & market gaps (12 sources)
  ✓  Market size & growth (World Bank, FRED)
  ✓  Customer pain points (Reddit, HN)
  ✓  Industry trends & Why Now
  ✓  Technology & feasibility
  ✓  Regulatory environment
  ✓  Business model precedents
  ✓  Adjacent innovation & IP
```

Final summary format:
```
━━━ RESEARCH BRIEFING COMPLETE ━━━━━━━━━━━━━━━━━━━━━━━━━

  File saved:  [idea-slug]/[slug]-research-briefing.md
  Excel files: [slug]-competitive-scan.xlsx  (if scan ran)
               [slug]-market-data.xlsx       (if scan ran)
               [slug]-trends.xlsx            (if scan ran)

  Key findings:
  • [bullet 1]
  • [bullet 2]
  • [bullet 3]
  • [bullet 4]
  • [bullet 5]

  Next step: /startup-validator

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

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

## Phase 2: Subagent Orchestration (8 Dimensions in Parallel)

**CRITICAL:** Do not research dimensions sequentially. Launch all 8 as simultaneous Task calls immediately after collecting Tier 1 answers. Each task is fully independent.

### How to orchestrate

After Tier 1 intake, announce:
```
Starting parallel research across 8 dimensions...
```

Then launch these Task calls simultaneously (in a single response, if the tool allows multiple parallel invocations):

**Task 1 — Competitors & Market Gaps**
```
Search for existing solutions to [problem].
Keywords: "[problem] software/tool/app", "[keywords] alternatives", "best [category] tools 2025 2026".
Also search Product Hunt, G2, Capterra, Crunchbase.
B2B: Also check Gartner Magic Quadrant.
B2C: Also check App Store rankings, consumer reviews.
Return: top 5 competitors, their pricing, positioning, key gaps.
```

**Task 2 — Market Size & Growth**
```
Research market size and growth for [industry/category].
Keywords: "[industry] market size", "[category] TAM", "[industry] growth rate 2025 2026".
Look for analyst reports, industry associations, government data.
Return: best TAM estimate with source, CAGR, key market segments.
```

**Task 3 — Customer Pain Points**
```
Search Reddit, Quora, Hacker News for organic discussions about [problem].
Keywords: "r/[relevant subreddit] [problem]", "[problem] frustrating", "[category] alternatives".
Find community threads with the most engagement.
Return: top 5 pain points by frequency, strongest quotes (anonymized), workaround behaviors.
```

**Task 4 — Industry Trends & Why Now**
```
Research what trends, regulatory changes, or technology shifts make [idea] relevant now.
Keywords: "[industry] trends 2025 2026", "[technology] adoption", "[regulatory change] impact".
Look for inflection points in the last 2 years.
Return: 3-5 timing factors, data points for each, "Why Now" narrative.
```

**Task 5 — Technology & Feasibility**
```
Assess the technical feasibility of [idea].
Search GitHub for relevant open-source repos (check stars + recent activity).
Look for technical blog posts and case studies about building similar systems.
Return: build complexity (simple/medium/hard), key technical risks, relevant open-source building blocks.
```

**Task 6 — Regulatory & Legal Environment**
```
Research regulations affecting [idea] in [geography].
Keywords: "[industry] regulations [country]", "[category] compliance requirements", "[industry] licensing".
Flag: GDPR, HIPAA, PCI-DSS, or industry-specific mandates.
Return: key regulatory requirements, major risks, jurisdictions to watch.
```

**Task 7 — Business Model Precedents**
```
Research how comparable companies in [category] price and monetize.
Find 3-5 companies with similar business models.
Look for pricing pages, investor decks, or analysis of their revenue model.
Return: pricing range, dominant model (SaaS/usage/marketplace fee/etc), unit economics benchmarks if available.
```

**Task 8 — Adjacent Innovation & IP**
```
Search for solutions to [problem] in adjacent industries (not direct competitors).
Search for recent patents related to [core technology or method].
Keywords: "[technology] patent", "[problem] novel approach", "[adjacent industry] [same problem]".
Return: 3-5 adjacent approaches with lessons, IP activity signal (active/quiet/contested).
```

### After all tasks complete

Collect all 8 results, then:
1. Print dimension status summary (use visual feedback format above)
2. If background scan approved: run Python scripts in parallel (competitive_scan.py, market_data.py, trend_analysis.py, patent_landscape.py)
3. Synthesize all findings into Research Briefing using `references/briefing-template.md`
4. Save briefing to `[idea-slug]/[idea-slug]-research-briefing.md`
5. Print final summary (use visual feedback format above)

---

## Phase 3: Output — Research Briefing

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

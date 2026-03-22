# Research Dimensions Reference

Eight dimensions to cover in every `startup-research` run. Depth per dimension should be proportional to founder's known uncertainty — if the founder has deep industry experience, skip what they already know and go deeper on blind spots.

---

## Dimension 1: Existing Solutions & Competitors

**Goal:** Map the competitive landscape. Never trust the founder's list — they always miss at least two.

**Search strategies:**
- `"[problem]" site:producthunt.com` — early-stage products
- `[category] alternatives 2025` — comparison intent searches
- `[category] site:g2.com` or `site:capterra.com` — B2B review sites
- `[company name] crunchbase funding` — funding status of known players
- `competitive_scan.py --keywords "[space]" --domain-search "[keyword]"` — domain saturation

**Output structure:**
| Competitor | Founded | Funding | Positioning | Pricing | Gap |
|-----------|---------|---------|-------------|---------|-----|

**Interpretation signals:**
- **Greenfield:** <5 direct competitors, no well-funded incumbents → validate demand carefully (may mean no market)
- **Emerging:** 5-20 players, some with seed/Series A → good timing, differentiation needed
- **Crowded:** 20+ players, unicorns present → need strong niche or disruptive angle

---

## Dimension 2: Market Context & Size

**Goal:** Give the founder a reality check on market scale before they build.

**Data sources:**
- FRED: GDP, PCE (consumer spending by category), employment
- BLS: Industry employment by NAICS code
- World Bank: International market context
- Census CBP: Establishment count by NAICS (B2B sizing)
- Industry reports: Look for snippets on Statista, IBISWorld, Grand View Research

**B2C sizing formula:**
```
TAM = Population in geography × % in target demographic × % with problem × ARPU
SAM = TAM × % reachable through planned channels
SOM = SAM × realistic Y1 adoption rate (1-3%)
```

**B2B sizing formula:**
```
TAM = Company count in target segment × Average Contract Value (ACV)
SAM = TAM × % with the specific pain × % with budget for category
SOM = Realistic customer count Y1 × ACV
```

---

## Dimension 3: Customer Segment Intelligence

**Goal:** Understand the target customer better than the founder does.

**Search strategies:**
- `reddit.com/r/[relevant sub] [problem keywords]` — organic frustration signals
- `news.ycombinator.com/item?id=` searches for "Ask HN: does anyone else..."
- `quora.com [problem question]`
- `[job title] pain points 2025`
- `[industry] challenges survey 2024 2025`

**What to compile:**
- Top pain points with frequency (how often mentioned)
- Current workarounds (what they use instead — reveals switching cost)
- Communities where segment congregates (subreddits, LinkedIn groups, Slack/Discord)
- Language they use to describe the problem (adopt their vocabulary)

---

## Dimension 4: Industry Trends & "Why Now"

**Goal:** Find the inflection point that makes this idea timely.

**Using trend_analysis.py:**
```bash
python scripts/trend_analysis.py \
  --keywords "[keyword1],[keyword2],[keyword3]" \
  --timeframe "today 5-y" \
  --geo US \
  --news-key YOUR_KEY \
  --news-query "[problem space] startup"
```

**Interpretation:**
- `trend_direction: rising` + `yoy_change_pct > 20%` → strong timing signal
- `trend_direction: declining` → may be fad or post-peak
- News volume spike → regulatory change or technology shift happened recently

**"Why Now" categories to look for:**
- Regulatory changes (new law, enforcement action)
- Technology maturity (AI, cloud, mobile, 5G hitting inflection)
- Behavioral shifts (COVID aftermath, remote work, Gen Z entering workforce)
- Market consolidation (incumbent acquired → customers left without support)
- Cost curves (hardware, compute, or logistics costs crossed a threshold)

---

## Dimension 5: Technology & Feasibility

**Goal:** Assess whether the idea is buildable, at what cost, and what the risks are.

**Search strategies:**
- `github.com/search?q=[core technology]` — open-source building blocks
- `[technology] tutorial site:medium.com OR site:dev.to` — developer adoption signals
- `[API / service] pricing` — infrastructure cost inputs
- `[technical approach] case study` — precedents for the approach

**Output:**
- Core technology readiness (mature / emerging / experimental)
- Key open-source dependencies (GitHub stars, last commit date)
- Build complexity estimate (weeks / months / years for MVP)
- Top 2-3 technical risks

---

## Dimension 6: Regulatory & Legal Environment

**Goal:** Surface any legal blockers or compliance costs before the founder commits.

**Search strategies:**
- `[industry] regulations [country] 2025`
- `[data type] compliance requirements GDPR HIPAA PCI`
- `[product category] license required`
- `[industry] regulatory risk`

**Red flags:**
- Requires government license to operate (healthcare, fintech, legal)
- Handles sensitive data with heavy compliance burden (HIPAA, PCI, financial data)
- Industry undergoing active regulatory scrutiny (AI, crypto, gig economy)

---

## Dimension 7: Business Model Precedents

**Goal:** Show the founder how comparable companies make money, with data.

**Research targets:**
- Pricing pages of 3-5 direct/adjacent competitors
- "How [similar company] makes money" blog posts / case studies
- Unit economics benchmarks: LTV:CAC ratios by category, churn benchmarks
- Business model evolution: how did successful companies in this space pivot?

**B2B benchmarks to find:**
- ACV (Annual Contract Value) ranges in the category
- Typical sales cycle length
- Common pricing model (per-seat, usage-based, flat rate)

**B2C benchmarks to find:**
- ARPU in comparable consumer apps
- Freemium-to-paid conversion rates in the category
- Key acquisition channels and their CPCs

---

## Dimension 8: Adjacent Innovation & Inspiration

**Goal:** Find cross-industry solutions that could be adapted or inspire differentiation.

**Search strategies:**
- `[problem] solved in [adjacent industry]` (e.g., "scheduling problem solved in healthcare")
- `[core mechanism] applied to [new domain]`
- `patent landscape` via patent_landscape.py
- `[behavior change] behavior design` — look for psychology/design inspiration

**Patent research:**
```bash
python scripts/patent_landscape.py --query "[core concept]" --limit 50
```

**Interpretation:**
- `ip_activity: high` → incumbents are protecting territory, design-arounds needed
- `top_assignees` → shows which big companies view this space as strategic
- `filing_trend: rising` → confirms corporate interest and validates market

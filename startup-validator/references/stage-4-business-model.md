# Stage 4: Business Model Validation Reference

---

## Unit Economics Definitions

**CAC (Customer Acquisition Cost)**
```
CAC = Total sales + marketing spend in period
      ÷ New customers acquired in same period

Split into:
CAC-organic = Marketing spend on organic channels ÷ organic new customers
CAC-paid    = Paid marketing spend ÷ paid new customers
```

**LTV (Lifetime Value)**
```
B2C:  LTV = ARPU ÷ Monthly churn rate
      (or: Average order value × Purchase frequency × Average customer lifespan)

B2B:  LTV = ACV × (1 ÷ Annual churn rate) × Gross margin
      Net LTV = LTV × Net Revenue Retention (NRR)
```

**Payback Period**
```
Payback = CAC ÷ (ARPU × Gross margin ÷ 12)   [in months]
```

**Magic Number (B2B efficiency)**
```
Magic Number = Net new ARR / Sales & Marketing spend
  >0.75 = efficient growth
  0.5-0.75 = acceptable
  <0.5 = burning cash inefficiently
```

**Net Revenue Retention (B2B)**
```
NRR = (Starting MRR + Expansion - Contraction - Churn) ÷ Starting MRR × 100
  >120% = excellent (expansion revenue covers churn)
  100-120% = good
  <100% = leaky bucket — fix before scaling
```

---

## Benchmarks by Archetype

| Metric | B2C | B2B SMB | B2B Mid-Market | B2B Enterprise |
|--------|-----|---------|----------------|----------------|
| LTV:CAC target | >3:1 | >3:1 | >4:1 | >5:1 |
| CAC payback | <3 mo | <6 mo | <12 mo | <18 mo |
| Monthly churn | <5% | <3% | <2% | <1% |
| Gross margin | >60% | >70% | >70% | >70% |
| NRR (B2B) | — | >100% | >110% | >120% |
| Magic Number | — | >0.75 | >0.75 | >0.5 |

---

## Van Westendorp Pricing Survey

Ask in this exact order (never show prior answers):

1. **"At what price would [product] be so expensive you wouldn't consider buying it?"** (Too expensive)
2. **"At what price would you start to think the quality is questionable — too cheap?"** (Too cheap)
3. **"At what price would [product] be a bargain — a great deal for what you get?"** (Cheap/acceptable)
4. **"At what price would [product] be getting expensive, but you'd still consider it?"** (Expensive/acceptable)

**Minimum viable sample:** 30+ respondents. Less than 30 → results are unreliable.

**Analysis:**
- Acceptable price range: between "too cheap" and "too expensive"
- Optimal price point: intersection of "getting expensive" and "bargain"
- Point of marginal cheapness (PMC): intersection of "too cheap" and "bargain"
- Point of marginal expensiveness (PME): intersection of "too expensive" and "getting expensive"

**B2B pricing note:** Van Westendorp is less reliable for B2B (buyers think in budgets, not price sensitivity). Better approach: "What's the cost of NOT solving this problem per year?" → price at 10-20% of that value.

---

## Revenue Model Selection Guide

| Model | Best for | Key variable | Complexity |
|-------|---------|-------------|-----------|
| Flat subscription | Predictable usage, SaaS | Retention | Low |
| Per-seat | Team tools, collaboration | Expansion | Medium |
| Usage-based | Infra, APIs, consumption | Unit economics | Medium |
| Freemium | B2C or PLG B2B | Free→paid conversion | High |
| Marketplace take-rate | Two-sided, transactions | GMV + take rate | High |
| One-time + maintenance | Enterprise, complex install | Renewal rate | Medium |
| Outcome-based | Professional services, B2B | Measurement | High |

---

## Financial Model Inputs (from validation data)

To build credible projections, you need these validated inputs:

| Input | Where validated | Acceptable source |
|-------|----------------|------------------|
| ACV / ARPU | Stage 2 (Van Westendorp) | Actual pricing test or LOI price |
| Monthly churn | Early pilot data | Industry benchmark if <3 mo data |
| CAC | Stage 2 channel tests | Actual ad spend data |
| Gross margin | First principles | COGS estimate + benchmark |
| Conversion rate (freemium) | Stage 2 | Industry benchmark if no data |
| Sales cycle | Stage 1-2 interviews | Actual observed cycles |

**Never accept:** "We assume 1% of the market" as a growth input. Ground all assumptions in validated data from Stage 1-4.

---

## Sean Ellis PMF Test

**Survey template:**
> "How would you feel if you could no longer use [product]?"
> - Very disappointed
> - Somewhat disappointed
> - Not disappointed (it isn't really that useful)
> - N/A — I no longer use [product]

**Threshold:** ≥40% "very disappointed" = product-market fit achieved

**Who to survey:**
- B2C: Users who have used the product at least 3 times in the last 30 days
- B2B End Users: Users who use the product at least weekly
- B2B Economic Buyers: SEPARATE survey asking about renewal likelihood and ROI

**If score is <40%:**
1. Look at what the "very disappointed" segment has in common
2. Double down on that segment — they're your real market
3. Identify the feature/use case they value most
4. Consider narrowing focus to that use case only

---

## Channel Validation Experiments

Test channels with minimum viable budget before scaling. Pre-register success thresholds.

**B2C channel benchmarks (industry averages, validate against your own):**
| Channel | Typical CPC | Typical conversion | Notes |
|---------|------------|-------------------|-------|
| Meta (Facebook/Instagram) | €0.50-2.00 | 2-5% (email) | Intent varies |
| Google Search | €1-5 | 3-8% (signup) | High intent |
| TikTok Organic | €0 | Viral unpredictable | Build for virality |
| Content/SEO | €0 (time cost) | 1-3% (of organic) | 6-12 mo runway |
| Email list | €0.01/email | 5-15% | Must build list first |

**B2B channel benchmarks:**
| Channel | Typical CPL | Typical conversion to meeting | Notes |
|---------|------------|------------------------------|-------|
| LinkedIn Ads | €50-150/lead | 10-20% to meeting | Expensive but targeted |
| Cold email | €5-20/meeting | 1-3% open→meeting | Volume + personalization |
| LinkedIn outreach | €0 | 5-15% reply rate | Time-intensive |
| Content inbound | €0 (time) | 2-5% visitor→lead | Long-term play |
| Events/conferences | €500-2K/event | 10-30% attendee→meeting | High ROI if targeted |

---

## Business Model Kill Criteria

- LTV:CAC ratio <1:1 with no credible path to improvement
- CAC payback >36 months (enterprise exception: >24 months)
- Monthly churn >10% with no identified cause
- Unit economics require 10x better performance than industry benchmarks to work
- Pricing required to hit LTV:CAC target is above Van Westendorp "too expensive" threshold
- Gross margin <40% (software business)

# T8: Unit Economics Model

> **Generated at:** Stage 4
> **Purpose:** CAC/LTV/payback calculations with data sources
> **Save as:** `[idea-slug]-unit-economics.xlsx` (Excel — preferred) or `[idea-slug]-unit-economics.md`
>
> **Excel workbook:** The sensitivity analysis and benchmark comparison tables use live formulas. Generate the scaffold with:
> ```python
> python3 scripts/generate_t8_workbook.py --slug [idea-slug]
> # Or: ask Claude to generate the openpyxl scaffold inline
> ```
>
> **Sheets:** `Inputs` (founder fills yellow cells) | `B2C Model` | `B2B Model` | `Sensitivity` (auto-calculated) | `Benchmark` | `Path to Profitability`

---

# Unit Economics Model: [Idea]

**Date:** [auto]
**Archetype:** [B2C / B2B + sub-type]
**Currency:** [€ / $]

---

## Revenue Inputs

| Input | Value | Source | Confidence |
|-------|-------|--------|-----------|
| Price (monthly or ACV) | €[X] | [Van Westendorp / LOIs / pricing test] | H/M/L |
| Gross margin | [X]% | [COGS analysis / benchmark] | H/M/L |
| Monthly churn rate | [X]% | [Pilot data / industry benchmark] | H/M/L |

---

## Unit Economics (B2C)

```
ARPU (annual)   = €[monthly price] × 12 = €[X]
Gross margin    = [X]%
Gross profit    = ARPU × Gross margin = €[X]

Monthly churn   = [X]%
LTV             = Gross profit ÷ Monthly churn = €[X]

CAC             = €[total spend] ÷ [customers] = €[X]
LTV:CAC ratio   = [X]:[1]  (target: >3:1)

Payback period  = CAC ÷ (ARPU × gross margin ÷ 12) = [X] months  (target: <3 mo)

K-factor        = [invites/user] × [conversion rate] = [X]  (>1 = viral growth)
```

---

## Unit Economics (B2B)

```
ACV             = €[X]/year
Gross margin    = [X]%

Annual churn    = [X]%
LTV             = ACV × (1 ÷ annual churn) × gross margin = €[X]

CAC (total)     = (Sales cost + Marketing spend) ÷ New logos = €[X]
  CAC-organic   = €[X]
  CAC-paid      = €[X]

LTV:CAC ratio   = [X]:[1]  (target: >4:1 Mid-Market; >5:1 Enterprise)

Payback         = CAC ÷ (ACV × gross margin ÷ 12) = [X] months  (target: <12-18 mo)

NRR             = [X]%  (target: >110-120%)
Magic Number    = Net new ARR ÷ S&M spend = [X]  (target: >0.75)
```

---

## Benchmark Comparison

| Metric | Our model | B2C bench | B2B SMB bench | B2B Mid bench | B2B Ent bench |
|--------|-----------|-----------|--------------|----------------|---------------|
| LTV:CAC | [X]:1 | >3:1 | >3:1 | >4:1 | >5:1 |
| Payback | [X] mo | <3 mo | <6 mo | <12 mo | <18 mo |
| Churn | [X]%/mo | <5% | <3% | <2% | <1% |

**Assessment:** [Above / At / Below benchmarks — with implications]

---

## Sensitivity Analysis

What if key assumptions are wrong?

| Scenario | ACV | Churn | CAC | LTV:CAC | Viable? |
|---------|-----|-------|-----|---------|--------|
| Base case | €[X] | [X]% | €[X] | [X]:1 | Yes |
| Pessimistic (churn 2×) | €[X] | [X]% | €[X] | [X]:1 | [Yes/No] |
| Optimistic (CAC 50% lower) | €[X] | [X]% | €[X] | [X]:1 | Yes |
| Break-even | €[X] | [X]% | €[X] | 3:1 | Minimum |

---

## Path to Profitability

**Current state:** [Pre-revenue / Revenue, losing money / Revenue, profitable]

**Key lever to improve unit economics:**
- [Primary lever: e.g., reduce CAC through content / increase ACV through upsell / reduce churn through onboarding]

**Projected unit economics at [N] customers:**
- Expected CAC: €[X] (scale effects on marketing)
- Expected LTV:CAC: [X]:1
- Break-even customer count: [N]

---

## Inputs Data Sources

| Input | Value | Source |
|-------|-------|--------|
| Price | €[X] | [Van Westendorp survey / pricing test / LOIs] |
| Gross margin | [X]% | [COGS breakdown: hosting €X, support €X, etc.] |
| Churn | [X]% | [Pilot data / [industry] SaaS benchmark] |
| CAC | €[X] | [Stage 2 channel experiment: €[spend] → [N] customers] |
| Sales cycle | [X] mo | [Stage 1-2 interview data] |

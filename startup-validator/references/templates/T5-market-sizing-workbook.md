# T5: Market Sizing Workbook

> **Generated at:** Stage 3
> **Purpose:** TAM/SAM/SOM with three-method triangulation
> **Save as:** `[idea-slug]-market-sizing.xlsx` (Excel — preferred) or `[idea-slug]-market-sizing.md`
>
> **Excel workbook:** Generate using the Python snippet below, then fill in the yellow input cells. Formulas are pre-wired; only override the shaded input fields.
>
> ```python
> # Run once to create the Excel workbook scaffold
> python3 scripts/generate_t5_workbook.py --slug [idea-slug]
> # Or: ask Claude to generate the openpyxl scaffold inline
> ```
>
> **Sheets:** `Inputs` (founder fills) | `Bottom-Up` (formula-driven) | `Top-Down` (formula-driven) | `Value-Theory` | `Triangulation` | `Data Sources`

---

# Market Sizing: [Idea]

**Date:** [auto]
**Archetype:** [B2C / B2B]
**Geography:** [Target market]

---

## Bottom-Up Calculation (PRIMARY)

### B2C version:

- Total population in geography: [N]
  - Source: [Census data / World Bank]
- % in target demographic: [X]%
  - Source: [Census/BLS or survey]
- % with the problem: [X]%
  - Source: [Industry survey / organic forum research]
- ARPU (annual): €[X]
  - Source: [Van Westendorp / pricing test / comparable products]

**TAM = [N] × [X]% × [X]% × €[X] = €[result]**

- % reachable through planned channels: [X]%
- % willing to pay (not just use): [X]%

**SAM = TAM × [X]% × [X]% = €[result]**

**SOM (Year 1, realistic [X]% adoption) = €[result]**

---

### B2B version:

- Total companies in target industries: [N]
  - Source: [Census CBP NAICS [code] / BLS data]
- Average Contract Value (ACV): €[X]/year
  - Source: [Stage 2 LOIs / Van Westendorp / comparable SaaS pricing]

**TAM = [N] × €[X] = €[result]**

- % with the specific problem: [X]%
- % with budget for this category: [X]%

**SAM = TAM × [X]% × [X]% = €[result]**

**SOM = [N customers Y1] × €[ACV] = €[result]**

---

## Top-Down Calculation (CROSS-CHECK)

- Industry total revenue / market size: €[X]B
  - Source: [Report name, year]
- Relevant segment: [X]%
- Geographic slice: [X]%

**TAM (top-down) = €[X]B × [X]% × [X]% = €[result]**

---

## Value Theory Calculation (SANITY CHECK)

- Target users/companies: [N]
- Annual value created per customer: €[X]
  - Basis: [X hours saved × €Y/hr] or [X% revenue uplift]
- Pricing capture rate: [X]% of value created

**Value-based TAM = [N] × €[X] × [X]% = €[result]**

---

## Triangulation

| Method | Result | Confidence |
|--------|--------|-----------|
| Bottom-up | €[X] | High |
| Top-down | €[X] | Medium |
| Value-theory | €[X] | Low |
| **Divergence** | **[X]%** | <15%: proceed; 15-30%: investigate; >30%: revise inputs |

**Triangulation assessment:** [Consistent / Minor divergence: [explanation] / Major divergence: [what to revise]]

---

## Final Estimates

| | Amount | Method | Confidence |
|--|--------|--------|-----------|
| **TAM** | €[X] | [primary method] | [H/M/L] |
| **SAM** | €[X] | Bottom-up | [H/M/L] |
| **SOM Y1** | €[X] | [N customers × ACV] | [H/M/L] |
| **SOM Y3** | €[X] | [growth assumption] | [H/M/L] |

---

## Data Sources Used

| Source | Series/Indicator | Value/Finding |
|--------|-----------------|---------------|
| FRED API | [series ID] | [value] |
| Census CBP | NAICS [code] | [establishment count] |
| BLS | [series ID] | [employment/wage data] |
| World Bank | [indicator] | [country value] |
| [Web source] | [report name] | [specific finding] |

---

## Investor Sanity Check

- Is the SAM at least €100M? [Yes / No — if No, explain niche strategy]
- Does the SOM represent a realistic market share? [X]% of SAM — [reasonable / aggressive / conservative]
- Are the growth assumptions grounded in validated data? [Yes / No]
- Is the market growing, flat, or shrinking? [Growing [X]%/yr / Flat / Shrinking]

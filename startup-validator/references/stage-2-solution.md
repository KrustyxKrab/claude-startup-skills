# Stage 2: Solution Validation Reference

---

## Experiment Design Principles

1. **One variable at a time** — don't test messaging and pricing simultaneously
2. **Minimum viable test** — the cheapest experiment that could answer the question
3. **Real stakes required** — asking for real money, real email, real time commitment
4. **Pre-register success criteria** — define what "proceed" looks like BEFORE running the test
5. **Time-box ruthlessly** — set a deadline; open-ended experiments run forever

---

## Experiment Card Template

See `templates/T3-experiment-card.md` for the full template.

Core fields:
- **Riskiest assumption being tested**
- **Experiment type** (Fake Door / Concierge / Wizard of Oz / etc.)
- **Success metric + threshold** (pre-registered)
- **Kill threshold** (pre-registered)
- **Budget and timeline**
- **Results** (fill after running)
- **Decision** (proceed / iterate / kill + reasoning)

---

## Fake Door Test (B2C Primary)

**What it is:** A landing page with a CTA (sign up, pre-order) that reveals you're testing demand before building. The "door" leads to a waitlist or "coming soon" message.

**When to use:** B2C with clear value proposition. Digital product. Low-ticket (<€50/month).

**Minimum viable setup:**
1. One-page site: problem statement, solution description, single CTA
2. Drive traffic: €150-300 in targeted ads (Meta or Google)
3. CTA: email signup OR pre-order with payment

**Conversion benchmarks:**
- Email signup from cold ad traffic: >5% = strong signal; <2% = weak
- Pre-order from cold traffic: >1% = strong signal
- Pre-order from warm traffic (people who already have the problem): >3% = strong

**Copy structure:**
```
Headline: [Desired outcome] without [current pain]
Sub-headline: [Specific mechanism that creates the outcome]
Social proof: [If available — number of beta users, quotes, logos]
CTA: [Get early access / Pre-order / Join the waitlist]
```

**What NOT to do:** Don't count email signups from people you personally asked to sign up. Cold traffic only.

---

## Concierge MVP (B2B Primary)

**What it is:** You manually deliver the value proposition to 3-5 customers, pretending the product exists. You are the product. No automation, no software.

**When to use:** B2B with complex workflow or judgment required. Proving the value before building the engine.

**Examples:**
- HR software: manually pull reports and email them daily to the customer
- Legal research tool: researcher manually answers queries via a shared doc
- Logistics optimizer: operations person manually optimizes routes in Excel and shares results

**Success criteria:**
- Customer pays for the concierge service (even at a discount)
- Customer says "how soon can we do this for our whole team?"
- Customer doesn't want to stop when you say the pilot is ending

**Kill signals:**
- Customer accepts the free concierge trial but won't pay even a token amount
- "This was useful but we'd only pay if it was fully automated"
- No engagement — they don't use what you deliver

---

## Wizard of Oz

**What it is:** Product looks automated to the customer, but humans are doing it manually behind the scenes.

**When to use:** When automation IS the value proposition, but automation is expensive/complex to build first.

**Examples:**
- "AI" recommendation engine: human curator makes the recommendations
- Chatbot: human answers through a chat interface
- Document processing: humans extract data manually and populate the output

**Setup:**
1. Build only the customer-facing interface (can be very rough)
2. Manual processes behind the interface (spreadsheet, Zapier, human operator)
3. Customer interacts with the "product" normally
4. Internal: humans fulfill within the response time the product would need

**Success criteria:** Same as concierge — did the customer pay? Did they want to continue?

---

## LOI / Pre-Sales (B2B Primary)

**What it is:** Letter of Intent — a non-binding commitment from a potential customer to purchase once the product is built. Or actual pre-payment for a pilot.

**How to get an LOI:**
1. Run discovery calls (problem validation done)
2. Present the solution concept (not the product)
3. Ask: "If this existed and solved the problems we discussed, would your company purchase it?"
4. If yes: "Would you be willing to put that in writing as a letter of intent?"
5. LOI content: company name, problem statement, commitment to purchase / evaluate, budget range, timeline

**Success threshold:** 3+ LOIs = proceed to build; 1 LOI from a named enterprise customer = proceed

**B2B Sales Conversation Test:**
1. 20-30 target companies identified via LinkedIn
2. Cold outreach: problem-focused, not product pitch
3. Goal: 10 discovery calls booked
4. In calls: present value proposition with slides
5. Ask: "If this existed today, what would next steps look like?"
- Strong proceed: 10+ calls from 30 outreach; 3+ say "send proposal"; 1+ offers to pay
- Kill: <3 calls booked; all end with "interesting, keep me posted"

---

## Solution Validation Interview Questions

After showing a prototype, mockup, or description:

**What to ask:**
- "What would you expect this to do?" (comprehension check)
- "Walk me through how you'd use this in a typical week."
- "What's missing from this that you'd need?"
- "How does this compare to what you're doing today?"
- "What would have to be true for your company to buy this?" (B2B)
- "At what price would this be a no-brainer? At what price would you hesitate?" (Van Westendorp seed)

**What NOT to ask:**
- "Do you like it?" (opinion, not behavior)
- "Is this something you'd use?" (hypothetical)
- "What do you think about the design?" (not the question yet)

---

## Van Westendorp Pricing Questions

Ask in this exact order to avoid anchoring:

1. "At what price would you consider this too expensive to consider?"
2. "At what price would you start to think the quality might be questionable — too cheap?"
3. "At what price would you consider this a bargain — a great deal?"
4. "At what price would you consider this expensive but still acceptable?"

**Analysis:**
- Acceptable price range = between "too cheap" and "too expensive"
- Sweet spot = intersection of "acceptable expensive" and "bargain"
- If sweet spot is below your required price → pivot model or segment

---

## Iteration vs. Kill Decision

**Iterate (not kill) when:**
- The problem is validated but the solution framing needs work
- The wrong segment was tested (test a different one)
- The experiment design was flawed (bad traffic source, wrong CTA)
- Conversion is low but commitment signals are strong (people who did convert are highly engaged)

**Kill when:**
- 3+ experiment iterations with no improvement
- Committed customers can't be found despite reaching correct segment
- Unit economics are fundamentally broken at any realistic price
- Riskiest assumption is definitively false

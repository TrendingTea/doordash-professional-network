# DoorDash Professional Network - Independent Product Proposal

> **Author perspective and relationship:** This independent proposal is authored from the perspective of an active **Gold Status Dasher with 4+ years of first-hand experience** using the Dasher app and working directly with restaurant pickup workflows, delivery operations, and customer service. The author has a genuine service-provider relationship with DoorDash through the Dasher platform. This repository is **not an official DoorDash, Inc. product and does not imply corporate sponsorship, endorsement, approval, or employment.**

## Product thesis

DoorDash already connects customers, merchants, and Dashers. This proposal adds a fourth layer: **professional development and economic mobility.**

Structured merchant feedback, voluntary Dasher professional profiles, customer-facing professional cards, positive recognition, career interests, transferable skills, and pilot analytics can turn repeated service work into optional professional evidence.

## Founder insight

Four-plus years of direct Dasher experience revealed an opportunity beyond delivery logistics: Dashers repeatedly demonstrate reliability, communication, customer service, time management, problem solving, navigation, merchant relations, and independent work discipline, yet much of that performance is difficult to translate into portable career evidence.

## Why this matters

The U.S. Bureau of Labor Statistics reports approximately **1.53 million delivery truck driver and driver/sales-worker jobs in 2024** and projects about **171,400 openings per year** over 2024-2034, with overall employment projected to grow **8%**, faster than the average for all occupations.

Pew Research Center found a career-development gap in platform work: **94%** of U.S. adults viewed gig-platform work as a good way to earn extra money and **94%** viewed it as a good way to work a flexible schedule, but only **31%** viewed it as a good way to build a career.

> **Delivery platforms coordinate a large professional network, but workers inside that network have limited infrastructure for portable reputation, transferable-skill evidence, professional recognition, and career mobility.**

### Sources

- U.S. Bureau of Labor Statistics - Delivery Truck Drivers and Driver/Sales Workers: https://www.bls.gov/ooh/transportation-and-material-moving/delivery-truck-drivers-and-driver-sales-workers.htm
- Pew Research Center - Americans' views of gig platform work and related policy issues: https://www.pewresearch.org/internet/2021/12/08/americans-views-of-gig-platform-work-and-related-policy-issues/
- Pew Research Center - Americans' experiences earning money through online gig platforms: https://www.pewresearch.org/internet/2021/12/08/americans-experiences-earning-money-through-online-gig-platforms/

## Proposed experience

```text
Merchant pickup
      |
      v
Structured pickup feedback
      |
      v
Recognition + coaching signals
      |
      v
Dasher Professional Profile
      |
      v
Optional "Get to Know Your Dasher" card
      |
      v
Career + networking opportunities
```

## Merchant Quality Loop

After an eligible pickup, a participating restaurant can provide concise structured feedback:

- Was the Dasher well presented?
- Was the Dasher respectful?
- Was an appropriate insulated delivery bag used?
- Were pickup instructions followed?
- Was the order handled carefully?
- Was the interaction efficient?

Managers can recognize positive behaviors such as professionalism, preparation, efficiency, helpfulness, reliability, and excellent communication.

The design favors **recognition and longitudinal development**, not a one-interaction punitive score.

## Dasher Professional Profile

Dashers voluntarily control a professional profile containing:

- professional headline
- biography
- transferable skills
- education
- career interests
- aggregate recognition metrics
- optional professional-development goals

Private contact information is not displayed by default.

## "Get to Know Your Dasher"

Customers could optionally see a limited professional card containing only Dasher-approved information. The goal is a controlled digital business card that lets service work create professional visibility without exposing unnecessary private identity data.

## Career Mobility Layer

```text
427 rated pickups
98% respectful interaction
97% professional presentation
96% pickup-instruction adherence
+ verified skills
+ education
+ career interests
          |
          v
Professional evidence
          |
          v
Training / networking / merchant opportunities /
internal opportunities / external career mobility
```

## Working prototype

This repository contains a runnable Flask application with:

- merchant feedback workflow
- manager mobile-friendly interface
- Dasher professional profiles
- customer-facing professional cards
- SQLite persistence
- pilot analytics dashboard
- JavaScript Object Notation Application Programming Interface endpoint
- automated tests
- synthetic 50-location McDonald's case study
- 1,000 simulated deliveries
- privacy and safeguards documentation

**API** means Application Programming Interface.  
**JSON** means JavaScript Object Notation.  
**POS** means Point of Sale.  
**MVP** means Minimum Viable Product.

## Hypothetical McDonald's case study

McDonald's is used solely as a **hypothetical high-volume restaurant case study**. No claim is made that McDonald's Corporation has approved, tested, sponsored, or endorsed this proposal.

The simulator models 50 synthetic restaurant locations and 1,000 synthetic deliveries. A real pilot could measure pickup dwell time, merchant complaints, handling incidents, merchant satisfaction, positive recognition, and Dasher professional-profile participation.

## Architecture

```text
Order / Pickup Event
        |
        v
Merchant Feedback Service
        |
        v
Trust + Aggregation Layer
        |
        v
Dasher Professional Profile
        |
        +-------------------+
        |                   |
        v                   v
Customer Card       Career Opportunity Layer
```

## Safeguards

A restaurant manager should not be able to materially damage a Dasher's livelihood because of one subjective interaction.

Production requirements should include:

- minimum sample sizes before aggregate scores appear
- positive-recognition emphasis
- feedback anomaly and abuse detection
- Dasher dispute and correction workflow
- no protected-class questions
- no private contact information by default
- access-controlled manager notes
- retention limits
- separation of verified credentials from subjective observations
- transparency about how feedback is used

## Pilot success metrics

- merchant feedback completion rate
- pickup dwell time
- professional-recognition rate
- merchant complaint rate
- Dasher block rate
- order-handling incidents
- Dasher profile opt-in rate
- professional-card views
- career-interest engagement
- merchant satisfaction
- Dasher retention

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python seed.py
python -m pytest -v
python app.py
```

Open `http://127.0.0.1:8022`.

## Repository documents

- `docs/EXECUTIVE_PROPOSAL.md`
- `docs/PILOT_MCDONALDS.md`
- `docs/PRIVACY_AND_SAFEGUARDS.md`
- `docs/ARCHITECTURE.md`
- `docs/METRICS.md`
- `docs/PRODUCT_REQUIREMENTS.md`
- `docs/DoorDash_Professional_Network_Proposal.pdf`

## Status

**Independent prototype / partnership proposal.**

The objective is to demonstrate the product concept, establish measurable pilot hypotheses, and create a concrete artifact that DoorDash product, merchant, operations, trust, and workforce-development teams could evaluate.

## Trademark notice

DoorDash, Dasher, and McDonald's names and trademarks remain the property of their respective owners. Their use identifies the platform context and hypothetical case study; it does not indicate sponsorship or endorsement.

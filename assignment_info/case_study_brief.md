# FlexWork Marketplace Case Study Brief

## Business Context

**Company**: FlexWork
**Industry**: Professional Services Marketplace
**Model**: Two-sided platform connecting contractors with clients for project-based work

### Core Unit

A **project** represents a single contractor working a single engagement for a single client.

- **Posted projects**: Clients post project requirements on the platform
- **Completed projects**: Revenue is generated when a qualified contractor is matched and completes the work

### Key Metric

**Net revenue per project** measures the profitability of selling one "unit" of service.

---

## Problem Statement

FlexWork has observed significant degradation in net revenue per project comparing:
- **Q3 2025**: July-August 2025
- **Q3 2024**: July-August 2024

The leadership team needs to understand:
1. What is driving this degradation?
2. Which business segments are most affected?
3. What actions should be taken to recover profitability?

---

## Analysis Questions

**Dataset**: Monthly transaction-level net revenue data by client dimensions (January 2024 - September 2025)

### 1. Quantify the Degradation

**What has been the degradation in net revenue per project in Q3 2025 (through August) relative to Q3 2024?**

**Which business segments have experienced the most degradation?**

- Analyze by business segment, vertical, client lifecycle, and transaction type
- Identify highest-impact segments for prioritization

### 2. Root Cause Analysis

**What are the root causes of the degradation based on the various components of net revenue?**

Break down the drivers:
- Operational issues (overbooking, billing failures)
- Pricing pressure (rate declines, discounting)
- Business mix shifts (segment, cohort changes)
- Other factors

### 3. Strategic Action Plan

**Given the root causes from #2, what is your action plan to improve net revenue per project?**

**What are the levers you would deploy from a GTM perspective as well as a product perspective?**

**What is your project plan to address the issues?**

- Prioritize initiatives by impact and feasibility
- Define specific GTM (go-to-market) and Product levers
- Create a 90-day execution plan with milestones
- Quantify expected outcomes with uncertainty modeling

---

## Appendix A: Unit Economics Framework

### What Are Unit Economics?

Unit economics measure the profitability of selling one "unit" of service.

#### Key Differences from Traditional Profitability Metrics

| Traditional Metrics | Unit Economics |
|-------------------|----------------|
| Include all costs (fixed + variable) | Only variable costs |
| Net income, free cash flow | Per-unit profitability |
| Fixed costs: Product & Engineering, G&A, overhead | Variable costs: payment processing, insurance, ops support |

#### Why Unit Economics Matter

- **Breakeven Analysis**: Determines output levels needed to cover fixed costs
- **Scalability**: Stronger unit economics = lower scale required for profitability
- **Sustainability**: Demonstrates intrinsic profitability before fixed cost coverage
- **Volume Impact**: Greater volume covers fixed costs more efficiently

### Units of Measurement

1. **"One item sold"** → Project (unit of work a Contractor provides to a Client)
2. **"One customer acquired"** → Two-sided marketplace customers:
   - Clients (businesses posting projects)
   - Contractors (professionals delivering services)

---

## Appendix B: Data Dictionary

### Core Dimensions

| Field | Description |
|-------|-------------|
| **month_pst** | Month of payment transaction |
| **business_segment** | Relevant business segment (7 segments) |
| **vertical** | Business segments mapped to: Professional Services, Technical Services |
| **transaction_type** | Payment transaction type (see types below) |
| **overbook_project_group_flag** | Binary flag (1=overbooked project category) |
| **msa_parent** | Parent company under master services agreement |
| **msa_lob** | Line of business within MSA parent company |
| **new_existing_client** | Client lifecycle age (F90 vs F90+) |
| **gig_position** | Type of positions contractors work on platform |
| **project_hour_duration** | Average project duration in hours |
| **project_counts_payment** | Total projects resulting in financial transaction |

### Transaction Types

- **Normal**: Regular transactions after project completion
- **Dispute**: Claims for additional/reduced payment after project completion
- **Conversion Fee**: Fees when contractors are directly hired by clients
- **Incentive**: Customer support-related payouts to contractors (one-sided)
- **Tip**: Tip payouts to contractors (pass-through costs, FlexWork covers W2 taxes)
- **Unknown**: Uncategorized transactions

### Financial Metrics

| Field | Description |
|-------|-------------|
| **client_total** | Money received from client (hours billed × bill rate) |
| **client_service_fee** | Service fee collected from client |
| **client_booking_fee** | Booking fee collected from client |
| **service_and_booking_fees** | Sum of service + booking fees |
| **vendor_allowances** | MSA contract rebates/discounts |
| **total_instant_pay_fees** | Fees for expedited contractor payouts |
| **client_total_credit_memos** | Rebates/discounts owed to client |
| **contractor_total** | Money paid to contractor (hours worked × wage rate) |
| **contractor_w2_taxes** | W2 taxes for W2-classified projects |
| **contractor_total_tns_coach** | Trust & safety + coach costs |
| **gmv** | Gross Merchandise Value (see formula) |
| **contra_revenue** | See formula below |
| **net_revenue** | See formula below |

### Client Lifecycle

- **F90 Client**: Within first 90 days on platform
- **F90+ Client**: 90+ days on platform

### Overbooking Logic

FlexWork sometimes assigns more contractors than requested as a safeguard against no-shows. If more contractors show up than needed, FlexWork pays the extra contractors directly—the client is not charged for overbooked positions.

---

## Appendix C: Net Revenue Methodology

### GMV (Gross Merchandise Value)

**Formula**:
```
GMV = (Client Total) + (Client Service Fees) + (Client Booking Fees)
      - (Vendor Allowances) - (Client Credit Memos)
```

**Key Notes**:
- Client total excludes tip payouts
- Vendor allowances applied to Enterprise Corp A, B, C, D (MSA clients)
- Credit memos exclude certain MSA clients per Finance team request

### Contra Revenue

**Formula**:
```
Contra Revenue = (Contractor Total) + (Contractor W2 Taxes)
                 - (Contractor T&S and Coach payments)
```

**Key Notes**:
- W2 taxes based on state where project occurred
- T&S (Trust & Safety) costs are deducted from contra revenue

### Net Revenue

**Formula**:
```
Net Revenue = (GMV) + (Instant Pay Fees) - (Contra Revenue)
```

**Key Notes**:
- Instant pay fees incorporated per Finance team request
- This is the key metric for unit economics analysis

---

## Formula Reference

### Net Revenue Per Project
```
Net Revenue Per Project = Net Revenue ÷ project_counts_payment
```

### Key Financial Components

**Client Revenue Components**:
```
client_total = hours billed × client bill rate
service_and_booking_fees = client_service_fee + client_booking_fee
```

**Contractor Cost Components**:
```
contractor_total = hours worked × contractor wage rate
```

---

## Analysis Guidelines

1. **Start with Data Quality**: Validate metrics, check for anomalies, understand transaction types
2. **Establish Baseline**: Q3 2024 performance as comparison point
3. **Decompose Drivers**: Break down the -$4.51/project degradation into components
4. **Segment Analysis**: Identify which client segments, verticals, cohorts are most affected
5. **Action Planning**: Develop specific, actionable recommendations with quantified impact

---

*This case study uses synthetic data for portfolio demonstration purposes. All scenarios are fictional.*

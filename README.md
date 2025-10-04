# FlexWork Marketplace: Unit Economics Analysis

> **Portfolio Case Study** | Data Analysis & Strategy

A comprehensive analysis of marketplace unit economics degradation and strategic action planning to recover profitability.

---

## 📊 Executive Summary

**Company**: FlexWork - A professional services marketplace platform
**Problem**: 13.2% degradation in net revenue per project from Q3 2024 to Q3 2025
**Impact**: From $34.15/project → $29.63/project
**Objective**: Identify root causes and develop a 90-day action plan to recover profitability

### Key Findings

1. **Operational Inefficiencies** drove 65% of degradation
   - Overbooking rate surge: 16.5% → 23.9%
   - Zero GMV rate increase: 16.6% → 23.9%

2. **Pricing Pressure** contributed 25% of degradation
   - Average bill rate declined $14.58/project (-7.7%)
   - Aggressive discounting to win/retain clients

3. **Business Mix Shifts** accounted for 10% of degradation
   - Growth in lower-margin Technical Services segment
   - Decline in high-margin Professional Services

### Strategic Recommendation

**Focused 90-Day Plan**: Target top 3 root causes for maximum impact
- **Operational fixes** (Product-led): Reduce overbooking and billing failures
- **Pricing recovery** (GTM-led): Strategic rate increases and discount governance
- **Expected outcome**: $34.80/project (+17.5% improvement, +$7.9M annualized)

---

## 🎯 Project Structure

```
portfolio_marketplace_case_study/
├── data/
│   ├── raw/                              # Synthetic transaction data
│   └── processed/                         # Cleaned & aggregated datasets
├── notebooks/
│   ├── 01_data_quality_analysis.ipynb     # EDA & data validation
│   ├── 02_metrics_validation.ipynb        # Unit economics calculations
│   ├── 03_root_cause_analysis.ipynb       # Driver decomposition
│   └── 04_action_plan.ipynb               # Strategic recommendations & Monte Carlo
├── src/
│   └── metrics.py                         # Reusable metric calculations
├── outputs/
│   └── figures/                           # Visualizations
└── assignment_info/
    └── case_study_brief.md                # Original problem statement
```

---

## 🔍 Analysis Methodology

### 1. Data Quality Assessment
- **Dataset**: 387K synthetic transactions (Jan 2024 - Sep 2025)
- **Dimensions**: Business segment, client type, contractor classification, transaction type
- **Metrics**: GMV, Net Revenue, Contra Revenue per transaction

### 2. Metric Validation
- Validated unit economics formulas against business logic
- Identified data quality issues (zero GMV transactions, overbooking anomalies)
- Established baseline metrics for Q3 2024 vs Q3 2025

### 3. Root Cause Analysis
- **Driver Decomposition**: Waterfall analysis of revenue degradation
- **Segment Analysis**: Identified highest-impact business segments
- **Cohort Analysis**: Client lifecycle and retention patterns

### 4. Action Planning
- **Monte Carlo Simulation**: 10,000 scenarios modeling uncertainty
- **Sensitivity Analysis**: Tornado charts showing variable impact ranges
- **Project Plan**: 90-day phased execution with milestones and owners

---

## 📈 Key Insights & Visualizations

### Root Cause Breakdown
| Driver | Impact | % of Total |
|--------|--------|------------|
| Overbooking Rate Surge | -$1.50/project | 33% |
| Zero GMV Rate Increase | -$1.60/project | 35% |
| Pricing Decline | -$1.10/project | 24% |
| Mix Shifts | -$0.31/project | 7% |
| **Total Degradation** | **-$4.51/project** | **100%** |

### 90-Day Recovery Projection

**Conservative Targets** (Monte Carlo P50):
- **Day 30**: $30.50/project (+$0.87)
- **Day 60**: $32.80/project (+$3.17 cumulative)
- **Day 90**: $34.80/project (+$5.17 cumulative) ✓ **Beats Q3 2024**

**Financial Impact**:
- 90-day cumulative revenue gain: **$1.15M**
- Annualized run-rate improvement: **$7.9M/year**
- Probability of success: **50-60%** chance of hitting $35+/project

---

## 🛠️ Technical Stack

**Languages & Libraries**:
- Python 3.9+
- Pandas, NumPy (data manipulation)
- Matplotlib, Seaborn (visualization)
- Jupyter Notebook (analysis environment)

**Techniques**:
- Monte Carlo simulation (risk modeling)
- Driver decomposition (variance analysis)
- Cohort analysis (customer segmentation)
- Sensitivity analysis (tornado charts)

---

## 🚀 Getting Started

### Prerequisites
```bash
python 3.9+
```

### Setup
```bash
# Clone repository
git clone https://github.com/lokiak/portfolio_marketplace_case_study.git
cd portfolio_marketplace_case_study

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Generate synthetic data (optional - data already included)
python generate_synthetic_data.py

# Launch Jupyter Notebook
jupyter notebook
```

**Quick Start (venv already included)**:
```bash
cd portfolio_marketplace_case_study
source venv/bin/activate  # Activate the included virtual environment
jupyter notebook          # Start analyzing!
```

### Running the Analysis
1. Start with `01_data_quality_analysis.ipynb` for data exploration
2. Progress through notebooks sequentially (01 → 04)
3. Each notebook is self-contained with clear markdown explanations

---

## 📝 Key Deliverables

### 1. Root Cause Analysis Report
- Comprehensive driver decomposition
- Segment-level performance breakdowns
- Cohort retention analysis

### 2. Strategic Action Plan
- 90-day phased execution plan
- Product & GTM levers with ownership
- Monte Carlo risk modeling
- ROI projections and success metrics

### 3. Executive Visualizations
- Waterfall charts (revenue degradation)
- Tornado charts (sensitivity analysis)
- Timeline projections (recovery trajectory)
- Probability distributions (outcome ranges)

---

## 💼 Skills Demonstrated

- **Data Analysis**: Large-scale transaction analysis, metric validation, anomaly detection
- **Business Strategy**: Unit economics, pricing strategy, operational optimization
- **Statistical Modeling**: Monte Carlo simulation, sensitivity analysis, probabilistic forecasting
- **Communication**: Executive summaries, visual storytelling, actionable recommendations
- **Tools**: Python, Pandas, Jupyter, Git, Data visualization libraries

---

## 📚 Context & Methodology

### Unit Economics Framework

**Core Metric**: Net Revenue per Project
```
Net Revenue = GMV + Instant Pay Fees - Contra Revenue

Where:
  GMV = Client Total + Service Fees + Booking Fees - Allowances - Credits
  Contra Revenue = Contractor Pay + W2 Taxes - T&S Costs
```

**Why This Matters**:
- Measures profitability of selling one "unit" of service
- Excludes fixed costs (product, engineering, G&A)
- Determines breakeven volume and scalability
- Stronger unit economics = lower scale needed for profitability

### Analysis Approach
1. **Establish Baseline**: Q3 2024 performance ($34.15/project)
2. **Quantify Degradation**: Q3 2025 decline ($29.63/project, -13.2%)
3. **Decompose Drivers**: Operational, pricing, mix, and cohort effects
4. **Model Recovery**: Monte Carlo simulation with 90-day phased plan
5. **Define Actions**: Specific product & GTM levers with ownership

---

## 🔗 Connect

**Author**: Loki
**GitHub**: [@lokiak](https://github.com/lokiak)
**Portfolio**: [View more projects →](https://github.com/lokiak)

---

## ⚠️ Disclaimer

This is a **portfolio case study** using **synthetic data**. All company names, data, and scenarios are fictional and created for demonstration purposes. The analysis methodology and insights are real and applicable to marketplace businesses.

---

## 📄 License

This project is open source and available under the MIT License.

---

*Last updated: October 2025*

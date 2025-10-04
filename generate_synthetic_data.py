"""
Synthetic Data Generator for FlexWork Portfolio Case Study

Generates realistic transaction-level data mimicking a marketplace platform
with similar statistical properties to the original analysis, but completely fictional.

Author: Portfolio anonymization script
Date: 2025-10-03
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

def generate_synthetic_data():
    """
    Generate synthetic transaction data for FlexWork marketplace.

    Mimics the patterns from the original analysis:
    - ~21 months of data (Jan 2024 - Sep 2025)
    - Degradation in metrics from 2024 to 2025
    - Overbooking and zero GMV issues increasing
    - Various business segments with different margins
    """

    print("Generating synthetic FlexWork marketplace data...")
    print("="*80)

    # Date range: Jan 2024 to Sep 2025 (21 months)
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 9, 30)
    months = pd.date_range(start=start_date, end=end_date, freq='MS')

    # Business segments (mapped from original)
    segments = {
        'Consulting': {'weight': 0.25, 'margin_base': 42, 'degradation': -0.8},
        'Engineering': {'weight': 0.20, 'margin_base': 38, 'degradation': -1.2},
        'Design': {'weight': 0.15, 'margin_base': 45, 'degradation': -0.6},
        'Marketing': {'weight': 0.12, 'margin_base': 40, 'degradation': -0.9},
        'Data Analytics': {'weight': 0.10, 'margin_base': 48, 'degradation': -0.5},
        'Project Management': {'weight': 0.10, 'margin_base': 43, 'degradation': -0.7},
        'Other Services': {'weight': 0.08, 'margin_base': 35, 'degradation': -1.0},
    }

    # Verticals (roll-up)
    vertical_mapping = {
        'Consulting': 'Professional Services',
        'Engineering': 'Technical Services',
        'Design': 'Professional Services',
        'Marketing': 'Professional Services',
        'Data Analytics': 'Technical Services',
        'Project Management': 'Professional Services',
        'Other Services': 'Technical Services',
    }

    # Transaction types
    transaction_types = ['Normal', 'Dispute', 'Tip', 'Incentive', 'Conversion Fee', 'Unknown']

    # Gig positions
    gig_positions = [
        'Senior Consultant', 'Software Engineer', 'Graphic Designer',
        'Marketing Specialist', 'Data Analyst', 'Project Coordinator',
        'Account Manager', 'Business Analyst', 'UX Designer'
    ]

    # MSA clients (enterprise accounts)
    msa_clients = ['Enterprise Corp A', 'Enterprise Corp B', 'Enterprise Corp C', 'Enterprise Corp D']

    all_data = []

    for month in months:
        month_str = month.strftime('%Y-%m')
        month_num = (month.year - 2024) * 12 + month.month

        # Base transaction volume with growth
        base_volume = 12000 + month_num * 500  # Growing from 12K to 22K/month

        # Add seasonality
        if month.month in [6, 7, 8]:  # Summer peak
            base_volume = int(base_volume * 1.15)
        elif month.month in [11, 12]:  # Holiday season
            base_volume = int(base_volume * 1.10)

        # Degradation factors (2025 has more problems)
        is_2025 = month.year == 2025
        overbook_rate_base = 0.165 if not is_2025 else 0.239
        zero_gmv_rate_base = 0.166 if not is_2025 else 0.239

        # Generate transactions for this month
        for segment, props in segments.items():
            n_transactions = int(base_volume * props['weight'])

            for i in range(n_transactions):
                # Basic attributes
                vertical = vertical_mapping[segment]
                transaction_type = np.random.choice(
                    transaction_types,
                    p=[0.75, 0.08, 0.10, 0.04, 0.02, 0.01]
                )

                # Client attributes
                is_msa = np.random.random() < 0.15
                if is_msa:
                    msa_parent = np.random.choice(msa_clients)
                    msa_lob = f"{msa_parent} - {np.random.choice(['Division A', 'Division B'])}"
                else:
                    msa_parent = None
                    msa_lob = None

                # Client lifecycle (F90 = first 90 days)
                is_new_client = np.random.random() < (0.08 if is_2025 else 0.06)
                new_existing = 'F90' if is_new_client else 'F90+'

                # Overbooking flag (increases in 2025)
                overbook_noise = np.random.normal(0, 0.02)
                is_overbooked = np.random.random() < (overbook_rate_base + overbook_noise)
                overbook_flag = 1 if is_overbooked else 0

                # Project details
                gig_position = np.random.choice(gig_positions)
                project_hours = np.random.triangular(4, 8, 12)

                # Financial calculations
                # Base rates decline over time (pricing pressure)
                bill_rate_base = np.random.uniform(45, 85)
                pay_rate_base = bill_rate_base * np.random.uniform(0.65, 0.75)

                # Apply degradation if 2025
                if is_2025:
                    bill_rate_base *= np.random.uniform(0.92, 0.98)  # 2-8% decline

                # Client total payment
                client_total = bill_rate_base * project_hours

                # Service and booking fees
                service_fee_rate = np.random.uniform(0.08, 0.15)
                booking_fee_rate = np.random.uniform(0.02, 0.05)
                client_service_fee = client_total * service_fee_rate
                client_booking_fee = client_total * booking_fee_rate

                # Vendor allowances (for MSA only)
                vendor_allowances = 0
                if is_msa:
                    vendor_allowances = (client_total + client_service_fee + client_booking_fee) * np.random.uniform(0.05, 0.12)

                # Credit memos (refunds/discounts)
                has_credit_memo = np.random.random() < 0.05
                credit_memos = client_total * np.random.uniform(0.05, 0.20) if has_credit_memo else 0

                # Contractor payment
                contractor_total = pay_rate_base * project_hours

                # W2 taxes (assume 70% are W2)
                is_w2 = np.random.random() < 0.70
                contractor_w2_taxes = contractor_total * 0.0765 if is_w2 else 0  # FICA

                # Trust & safety costs
                contractor_tns_coach = contractor_total * np.random.uniform(0.01, 0.03)

                # Instant pay fees (contractors can get paid instantly for a fee)
                uses_instant_pay = np.random.random() < 0.25
                instant_pay_fees = contractor_total * 0.02 if uses_instant_pay else 0

                # Zero GMV logic (increases in 2025)
                zero_gmv_noise = np.random.normal(0, 0.02)
                force_zero_gmv = np.random.random() < (zero_gmv_rate_base + zero_gmv_noise)

                if force_zero_gmv or transaction_type == 'Tip':
                    # No client billing
                    client_total = 0
                    client_service_fee = 0
                    client_booking_fee = 0

                # Overbooking logic (FlexWork pays contractor, no client charge)
                if is_overbooked:
                    client_total = 0
                    client_service_fee = 0
                    client_booking_fee = 0

                # Calculate derived metrics
                gmv = (client_total + client_service_fee + client_booking_fee -
                       vendor_allowances - credit_memos)

                contra_revenue = (contractor_total - contractor_tns_coach + contractor_w2_taxes)

                net_revenue = gmv + instant_pay_fees - contra_revenue

                # Project count (usually 1, but could be batch)
                project_count = 1

                # Create transaction record
                record = {
                    'month_pst': month_str,
                    'business_segment': segment,
                    'vertical': vertical,
                    'transaction_type': transaction_type,
                    'overbook_project_group_flag': overbook_flag,
                    'msa_parent': msa_parent,
                    'msa_lob': msa_lob,
                    'new_existing_client': new_existing,
                    'gig_position': gig_position,
                    'project_hour_duration': round(project_hours, 2),
                    'project_counts_payment': project_count,

                    # Financial fields
                    'client_total': round(client_total, 2),
                    'client_service_fee': round(client_service_fee, 2),
                    'client_booking_fee': round(client_booking_fee, 2),
                    'service_and_booking_fees': round(client_service_fee + client_booking_fee, 2),
                    'vendor_allowances': round(vendor_allowances, 2),
                    'total_instant_pay_fees': round(instant_pay_fees, 2),
                    'client_total_credit_memos': round(credit_memos, 2),
                    'client_credit_memos_excl_enterprise_ab': round(credit_memos * 0.8, 2),  # Exclude some MSA

                    'contractor_total': round(contractor_total, 2),
                    'contractor_w2_taxes': round(contractor_w2_taxes, 2),
                    'contractor_total_tns_coach': round(contractor_tns_coach, 2),

                    # Calculated metrics
                    'gmv': round(gmv, 2),
                    'contra_revenue': round(contra_revenue, 2),
                    'contra_revenue_excl_tns_coach': round(contra_revenue - contractor_tns_coach, 2),
                    'net_revenue': round(net_revenue, 2),
                }

                all_data.append(record)

    # Convert to DataFrame
    df = pd.DataFrame(all_data)

    print(f"\n✓ Generated {len(df):,} synthetic transactions")
    print(f"  • Date range: {df['month_pst'].min()} to {df['month_pst'].max()}")
    print(f"  • Business segments: {df['business_segment'].nunique()}")
    print(f"  • Total GMV: ${df['gmv'].sum()/1_000_000:.1f}M")
    print(f"  • Total Net Revenue: ${df['net_revenue'].sum()/1_000_000:.1f}M")
    print(f"  • Avg net revenue per project: ${df['net_revenue'].sum() / df['project_counts_payment'].sum():.2f}")

    return df


def save_synthetic_data(df, output_path='data/raw/flexwork_transactions.csv'):
    """Save synthetic data to CSV."""
    df.to_csv(output_path, index=False)
    print(f"\n✓ Saved synthetic data to: {output_path}")
    print(f"  File size: {os.path.getsize(output_path) / 1024 / 1024:.2f} MB")


if __name__ == '__main__':
    import os

    # Generate data
    df = generate_synthetic_data()

    # Save to CSV
    save_synthetic_data(df)

    print("\n" + "="*80)
    print("Synthetic data generation complete!")
    print("="*80)

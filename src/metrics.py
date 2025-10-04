"""
Metric calculation functions for FlexWork unit economics analysis.

All formulas follow definitions from the assessment PDF Appendix C.
"""

import pandas as pd


def gmv(row):
    """
    Calculate Gross Merchandise Value (GMV) for a transaction.

    GMV = Client Total + Client Service Fee + Client Booking Fee
          - Vendor Allowances - Credit Memos (excl Enterprise Corp A/Enterprise Corp C)

    Args:
        row: pandas Series with required fields

    Returns:
        float: GMV value
    """
    return (
        row['client_total'] +
        row['client_service_fee'] +
        row['client_booking_fee'] -
        row['vendor_allowances'] -
        row['client_credit_memos_excl_compass_sodexo']
    )


def contra_revenue(row):
    """
    Calculate Contra Revenue for a transaction.

    Contra Revenue = Contractor Total - Contractor TNS/Coach + Contractor W2 Taxes

    Args:
        row: pandas Series with required fields

    Returns:
        float: Contra revenue value
    """
    return (
        row['contractor_total'] -
        row['contractor_total_tns_coach'] +
        row['contractor_w2_taxes']
    )


def net_revenue(row):
    """
    Calculate Net Revenue for a transaction.

    Net Revenue = GMV + Instant Pay Fees - Contra Revenue

    Args:
        row: pandas Series with required fields

    Returns:
        float: Net revenue value
    """
    return gmv(row) + row['total_instant_pay_fees'] - contra_revenue(row)


def calculate_metrics(df):
    """
    Add GMV, Contra Revenue, and Net Revenue columns to dataframe.

    Args:
        df: pandas DataFrame with raw transaction data

    Returns:
        pandas DataFrame with added metric columns
    """
    df = df.copy()
    df['gmv_calc'] = df.apply(gmv, axis=1)
    df['contra_revenue_calc'] = df.apply(contra_revenue, axis=1)
    df['net_revenue_calc'] = df.apply(net_revenue, axis=1)
    return df


def net_rev_per_shift(df):
    """
    Calculate aggregate Net Revenue per Project for a dataframe.

    Args:
        df: pandas DataFrame with net_revenue and project_counts_payment columns

    Returns:
        float: Net revenue per project
    """
    total_revenue = df['net_revenue'].sum()
    total_shifts = df['project_counts_payment'].sum()

    if total_shifts == 0:
        return 0

    return total_revenue / total_shifts


def gmv_per_shift(df):
    """
    Calculate aggregate GMV per Project for a dataframe.

    Args:
        df: pandas DataFrame with gmv and project_counts_payment columns

    Returns:
        float: GMV per project
    """
    total_gmv = df['gmv'].sum()
    total_shifts = df['project_counts_payment'].sum()

    if total_shifts == 0:
        return 0

    return total_gmv / total_shifts


def contra_per_shift(df):
    """
    Calculate aggregate Contra Revenue per Project for a dataframe.

    Args:
        df: pandas DataFrame with contra_revenue and project_counts_payment columns

    Returns:
        float: Contra revenue per project
    """
    total_contra = df['contra_revenue'].sum()
    total_shifts = df['project_counts_payment'].sum()

    if total_shifts == 0:
        return 0

    return total_contra / total_shifts


def instant_pay_per_shift(df):
    """
    Calculate aggregate Instant Pay Fees per Project for a dataframe.

    Args:
        df: pandas DataFrame with total_instant_pay_fees and project_counts_payment columns

    Returns:
        float: Instant pay fees per project
    """
    total_instant_pay = df['total_instant_pay_fees'].sum()
    total_shifts = df['project_counts_payment'].sum()

    if total_shifts == 0:
        return 0

    return total_instant_pay / total_shifts


def filter_shift_transactions(df):
    """
    Filter dataframe to include only core project transactions (Normal and Dispute).

    Excludes:
    - Tips: Pass-through payments (client_total excludes tips by design)
    - Incentives: One-sided payouts to contractors (no client charge)
    - Conversion Fees: Hiring fees (not project work)
    - Unknown: Uncategorized transactions

    Use this filter for per-project unit economics analysis to measure
    actual project profitability.

    Args:
        df: pandas DataFrame with transaction_type column

    Returns:
        pandas DataFrame filtered to Normal and Dispute transactions
    """
    return df[df['transaction_type'].isin(['Normal', 'Dispute'])].copy()

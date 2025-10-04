"""
Notebook Sanitization Script for FlexWork Portfolio Case Study

Copies and sanitizes Jupyter notebooks from the original Instawork case study,
replacing all company-specific references with generic FlexWork branding.

Author: Portfolio anonymization script
Date: 2025-10-03
"""

import json
import re
import os
import shutil

# Source and destination
SOURCE_NOTEBOOKS = "/Users/loki/Downloads/instawork_case/notebooks"
DEST_NOTEBOOKS = "/Users/loki/Downloads/portfolio_marketplace_case_study/notebooks"

# Comprehensive replacement mappings
REPLACEMENTS = {
    # Company names
    r'\bInstawork\b': 'FlexWork',
    r'\binstawork\b': 'flexwork',
    r'\bINSTAWORK\b': 'FLEXWORK',

    # Worker terminology
    r'\bpro\b(?!ject|cess|duct|gram|vide|file|blem|xy)': 'contractor',  # Avoid replacing in "project", "process", etc.
    r'\bPro\b(?!ject|cess|duct|gram|vide|file|blem)': 'Contractor',
    r'\bpros\b': 'contractors',
    r'\bPros\b': 'Contractors',
    r'\bpro\'s\b': 'contractor\'s',
    r'\bPro\'s\b': 'Contractor\'s',

    # Business terminology
    r'\bpartner\b': 'client',
    r'\bPartner\b': 'Client',
    r'\bpartners\b': 'clients',
    r'\bPartners\b': 'Clients',
    r'\bpartner\'s\b': 'client\'s',
    r'\bPartner\'s\b': 'Client\'s',

    # Work unit terminology
    r'\bshift\b': 'project',
    r'\bShift\b': 'Project',
    r'\bshifts\b': 'projects',
    r'\bShifts\b': 'Projects',

    # Business segments
    r'\bHospitality\b': 'Professional Services',
    r'\bhospitality\b': 'professional services',
    r'\bLight Industrial\b': 'Technical Services',
    r'\blight industrial\b': 'technical services',

    # Specific segments
    r'\bRestaurant\b': 'Consulting',
    r'\bWarehouse\b': 'Engineering',
    r'\bEvents\b': 'Design',
    r'\bRetail\b': 'Marketing',
    r'\bManufacturing\b': 'Data Analytics',
    r'\bCatering\b': 'Project Management',

    # MSA companies
    r'\bCompass\b': 'Enterprise Corp A',
    r'\bAramark\b': 'Enterprise Corp B',
    r'\bSodexo\b': 'Enterprise Corp C',
    r'\bWorldpac\b': 'Enterprise Corp D',

    # Column names in code
    r'partner_total': 'client_total',
    r'Partner_total': 'Client_total',
    r'partner_service_fee': 'client_service_fee',
    r'partner_booking_fee': 'client_booking_fee',
    r'partner_credit_memos': 'client_credit_memos',
    r'partner_credit_memos_excl_compass_sodexo': 'client_credit_memos_excl_enterprise_ab',
    r'vendor_allowances': 'vendor_allowances',  # Keep this

    r'pro_total': 'contractor_total',
    r'Pro_total': 'Contractor_total',
    r'pro_w2_taxes': 'contractor_w2_taxes',
    r'pro_total_tns_coach': 'contractor_total_tns_coach',

    r'shift_counts_payment': 'project_counts_payment',
    r'Shift_counts_payment': 'Project_counts_payment',
    r'shift_hour_duration': 'project_hour_duration',
    r'overbook_shift_group_flag': 'overbook_project_group_flag',

    r'new_existing_partner': 'new_existing_client',
    r'New_existing_partner': 'New_existing_client',

    # File paths
    r'instawork_case': 'portfolio_marketplace_case_study',
    r'instawork_transactions': 'flexwork_transactions',

    # URLs and references (remove any specific company links)
    r'https://instawork\.com': 'https://example-marketplace.com',
}


def sanitize_text(text):
    """Apply all replacements to a text string."""
    for pattern, replacement in REPLACEMENTS.items():
        text = re.sub(pattern, replacement, text)
    return text


def sanitize_notebook(source_path, dest_path):
    """
    Sanitize a single Jupyter notebook.

    Args:
        source_path: Path to source notebook
        dest_path: Path to save sanitized notebook
    """
    print(f"  Sanitizing: {os.path.basename(source_path)}")

    with open(source_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # Track changes
    cells_removed = 0
    cells_modified = 0

    # Process each cell
    sanitized_cells = []
    for cell in notebook['cells']:
        # Skip cells marked for removal (you can add logic here)
        # For now, keep all cells but sanitize content

        # Sanitize cell source
        if 'source' in cell:
            original_source = ''.join(cell['source'])
            sanitized_source = sanitize_text(original_source)

            if original_source != sanitized_source:
                cells_modified += 1

            # Update cell source
            cell['source'] = sanitized_source.split('\n')
            # Ensure newlines are preserved
            cell['source'] = [line + '\n' for line in cell['source'][:-1]] + [cell['source'][-1]]

        # Sanitize cell outputs if they exist
        if 'outputs' in cell:
            for output in cell['outputs']:
                if 'text' in output:
                    original_text = ''.join(output['text'])
                    output['text'] = sanitize_text(original_text).split('\n')
                    output['text'] = [line + '\n' for line in output['text'][:-1]] + [output['text'][-1]]

                if 'data' in output and 'text/plain' in output['data']:
                    original_data = ''.join(output['data']['text/plain'])
                    output['data']['text/plain'] = sanitize_text(original_data).split('\n')
                    output['data']['text/plain'] = [line + '\n' for line in output['data']['text/plain'][:-1]] + [output['data']['text/plain'][-1]]

        sanitized_cells.append(cell)

    notebook['cells'] = sanitized_cells

    # Save sanitized notebook
    with open(dest_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

    print(f"    ✓ Modified {cells_modified} cells")
    return cells_modified


def sanitize_python_file(source_path, dest_path):
    """Sanitize a Python source file."""
    print(f"  Sanitizing: {os.path.basename(source_path)}")

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    sanitized_content = sanitize_text(content)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(sanitized_content)

    print(f"    ✓ Sanitized Python file")


def sanitize_all_notebooks():
    """Sanitize all notebooks from the source directory."""
    print("="*80)
    print("SANITIZING NOTEBOOKS FOR FLEXWORK PORTFOLIO")
    print("="*80)
    print()

    # Notebooks to sanitize (skip notebook 01 as it's just data ingestion)
    notebooks_to_copy = [
        '02b_eda_quality_sql.ipynb',
        '03_metrics_validation.ipynb',
        '04_root_cause_analysis.ipynb',
        '05_action_plan.ipynb',
    ]

    total_modified = 0

    for notebook_name in notebooks_to_copy:
        source = os.path.join(SOURCE_NOTEBOOKS, notebook_name)

        # Rename notebooks for portfolio
        new_name = notebook_name.replace('02b_eda_quality_sql', '01_data_quality_analysis')
        new_name = new_name.replace('03_metrics', '02_metrics')
        new_name = new_name.replace('04_root', '03_root')
        new_name = new_name.replace('05_action', '04_action')

        dest = os.path.join(DEST_NOTEBOOKS, new_name)

        if os.path.exists(source):
            cells_modified = sanitize_notebook(source, dest)
            total_modified += cells_modified
        else:
            print(f"  ⚠️  Source not found: {notebook_name}")

    print()
    print(f"✓ Sanitized {len(notebooks_to_copy)} notebooks")
    print(f"✓ Modified {total_modified} cells total")
    print()

    # Also sanitize src/ Python files
    print("Sanitizing Python source files...")
    source_src = "/Users/loki/Downloads/instawork_case/src"
    dest_src = "/Users/loki/Downloads/portfolio_marketplace_case_study/src"

    if os.path.exists(os.path.join(source_src, 'metrics.py')):
        sanitize_python_file(
            os.path.join(source_src, 'metrics.py'),
            os.path.join(dest_src, 'metrics.py')
        )

    print()
    print("="*80)
    print("SANITIZATION COMPLETE!")
    print("="*80)


if __name__ == '__main__':
    sanitize_all_notebooks()

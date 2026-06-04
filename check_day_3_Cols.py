# check_day3_columns.py

import pandas as pd

files = [
    "02_nav_history_cleaned.csv",
    "03_aum_by_fund_house_cleaned.csv",
    "04_monthly_sip_inflows_cleaned.csv",
    "05_category_inflows_cleaned.csv",
    "06_industry_folio_count_cleaned.csv",
    "08_investor_transactions_cleaned.csv",
    "09_portfolio_holdings_cleaned.csv"
]

for file in files:
    print("\n" + "="*50)
    print(file)

    df = pd.read_csv(f"data/processed/{file}")

    print(df.columns.tolist())
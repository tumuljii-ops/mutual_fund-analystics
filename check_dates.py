import pandas as pd

files = [
    "03_aum_by_fund_house_cleaned.csv",
    "04_monthly_sip_inflows_cleaned.csv",
    "05_category_inflows_cleaned.csv",
    "06_industry_folio_count_cleaned.csv"
]

for file in files:
    df = pd.read_csv(f"data/processed/{file}")

    print("\n", file)
    print(df.head())
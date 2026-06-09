import pandas as pd

files = [
    "data/processed/02_nav_history_cleaned.csv",
    "data/processed/07_scheme_performance_cleaned.csv",
    "data/processed/08_investor_transactions_cleaned.csv",
    "data/processed/09_portfolio_holdings_cleaned.csv"
]

for file in files:

    df = pd.read_csv(file)

    print("\n")
    print("="*100)
    print(file)
    print("="*100)

    for col in df.columns:
        print(col)

    print("\nShape:", df.shape)
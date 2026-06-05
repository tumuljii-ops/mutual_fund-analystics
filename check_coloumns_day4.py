# check_day4_columns.py

import pandas as pd

files = [
    "02_nav_history_cleaned.csv",
    "07_scheme_performance_cleaned.csv",
    "10_benchmark_indices_cleaned.csv"
]

for f in files:
    df = pd.read_csv(f"data/processed/{f}")
    print("\n", f)
    print(df.columns.tolist())
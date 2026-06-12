import pandas as pd

perf = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

alpha_beta = perf[
    [
        "amfi_code",
        "scheme_name",
        "alpha",
        "beta"
    ]
]

alpha_beta.to_csv(
    "reports/alpha_beta.csv",
    index=False
)

print("alpha_beta.csv created")
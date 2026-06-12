import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create charts folder if not exists
os.makedirs("reports/charts", exist_ok=True)

# Load dataset
txn = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)
nav = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

pivot = nav.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

corr = pivot.pct_change().corr()

plt.figure(figsize=(10,8))

sns.heatmap(corr)

plt.savefig(
    "reports/charts/correlation_matrix.png",
    bbox_inches="tight"
)

plt.close()
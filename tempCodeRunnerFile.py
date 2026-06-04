import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("reports/charts", exist_ok=True)

txn = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

txn["gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Gender Split")

plt.savefig(
    "reports/charts/gender_split.png",
    bbox_inches="tight"
)

plt.close()
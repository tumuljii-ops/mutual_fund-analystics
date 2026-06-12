import pandas as pd
import os

DATA_FOLDER = "data/raw"

files = sorted(os.listdir(DATA_FOLDER))

print("=" * 80)
print("DATA INGESTION REPORT")
print("=" * 80)

for file in files:

    if file.endswith(".csv"):

        file_path = os.path.join(DATA_FOLDER, file)

        print(f"\nFILE: {file}")

        df = pd.read_csv(file_path)

        print(f"Shape: {df.shape}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\n" + "-" * 80)
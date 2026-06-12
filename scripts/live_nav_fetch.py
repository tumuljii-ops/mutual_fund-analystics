import requests
import pandas as pd

schemes = {
    119551: "sbi_bluechip",
    120503: "icici_bluechip",
    118632: "nippon_largecap",
    119092: "axis_bluechip",
    120841: "kotak_bluechip"
}

for amfi_code, file_name in schemes.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        print("\n" + "="*60)
        print("Scheme:", data["meta"]["scheme_name"])

        nav_df = pd.DataFrame(data["data"])

        output_path = f"data/raw/{file_name}_nav.csv"

        nav_df.to_csv(output_path, index=False)

        print("Saved:", output_path)

    else:
        print(f"Failed for {amfi_code}")
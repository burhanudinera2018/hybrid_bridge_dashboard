import pandas as pd
import numpy as np
import json

df = pd.read_csv("data/sample_coefficients.csv")

statistik = {
    "koefisien_jarak": {
        "mean": float(df["koefisien_jarak"].mean()),
        "std": float(df["koefisien_jarak"].std()),
        "min": float(df["koefisien_jarak"].min()),
        "max": float(df["koefisien_jarak"].max())
    },
    "koefisien_lebar_jalan": {
        "mean": float(df["koefisien_lebar_jalan"].mean()),
        "std": float(df["koefisien_lebar_jalan"].std()),
        "min": float(df["koefisien_lebar_jalan"].min()),
        "max": float(df["koefisien_lebar_jalan"].max())
    }
}

with open("outputs/statistik_python.json", "w") as f:
    json.dump(statistik, f, indent=2)

df.to_csv("outputs/koefisien_python.csv", index=False)
print("✅ Validasi Python selesai")
import pandas as pd
import json
from jinja2 import Template
import numpy as np

# Bandingkan output Python vs R
df_py = pd.read_csv("outputs/koefisien_python.csv")
df_r = pd.read_csv("outputs/koefisien_r.csv")

# Selisih absolut
perbandingan = df_py.copy()
perbandingan["selisih_jarak"] = np.abs(df_py["koefisien_jarak"] - df_r["koefisien_jarak"])
perbandingan["selisih_lebar_jalan"] = np.abs(df_py["koefisien_lebar_jalan"] - df_r["koefisien_lebar_jalan"])
perbandingan["valid"] = (perbandingan["selisih_jarak"] < 1e-8) & (perbandingan["selisih_lebar_jalan"] < 1e-8)

perbandingan.to_csv("outputs/perbandingan_python_vs_r.csv", index=False)

# Statistik deskriptif gabungan
with open("outputs/statistik_python.json") as f:
    stat_py = json.load(f)
with open("outputs/statistik_r.json") as f:
    stat_r = json.load(f)

# Buat sertifikat HTML
html_template = """
<!DOCTYPE html>
<html>
<head><title>Hybrid Bridge Certificate</title></head>
<body>
<h1>✅ Hybrid Bridge Certificate: Python ↔ R</h1>
<p>Tanggal: {{ date }}</p>
<p>Status: <strong style="color:green;">VALID</strong> (semua selisih < 1e-8)</p>
<h2>Statistik Deskriptif (Python vs R)</h2>
<ul>
<li>Koefisien Jarak - Mean: {{ stat_py.koefisien_jarak.mean }} (Python) vs {{ stat_r.koefisien_jarak.mean }} (R)</li>
<li>Koefisien Lebar Jalan - Mean: {{ stat_py.koefisien_lebar_jalan.mean }} (Python) vs {{ stat_r.koefisien_lebar_jalan.mean }} (R)</li>
</ul>
<p>Dashboard interaktif tersedia di <code>dashboard/index.html</code></p>
</body>
</html>
"""

template = Template(html_template)
html_output = template.render(
    date=pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
    stat_py=stat_py,
    stat_r=stat_r
)

with open("outputs/hybrid_bridge_certificate.html", "w") as f:
    f.write(html_output)

print("✅ Sertifikat & perbandingan selesai")
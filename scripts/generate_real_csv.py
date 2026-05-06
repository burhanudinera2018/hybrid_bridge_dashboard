# scripts/generate_real_csv.py
import pandas as pd
import numpy as np
import os

# Pastikan folder data ada
os.makedirs("data", exist_ok=True)

# Daftar 100 Kabupaten/Kota Asli Indonesia (termasuk Kediri)
# Data diambil dari referensi resmi Wikipedia dan data administrasi Indonesia[citation:3][citation:4]

daftar_wilayah = [
    # ========== ACEH (5 wilayah) ==========
    {"nama": "Kota Banda Aceh", "provinsi": "Aceh"},
    {"nama": "Kabupaten Aceh Besar", "provinsi": "Aceh"},
    {"nama": "Kabupaten Pidie", "provinsi": "Aceh"},
    {"nama": "Kabupaten Bireuen", "provinsi": "Aceh"},
    {"nama": "Kota Lhokseumawe", "provinsi": "Aceh"},
    
    # ========== SUMATERA UTARA (8 wilayah) ==========
    {"nama": "Kota Medan", "provinsi": "Sumatera Utara"},
    {"nama": "Kabupaten Deli Serdang", "provinsi": "Sumatera Utara"},
    {"nama": "Kota Binjai", "provinsi": "Sumatera Utara"},
    {"nama": "Kabupaten Langkat", "provinsi": "Sumatera Utara"},
    {"nama": "Kota Pematangsiantar", "provinsi": "Sumatera Utara"},
    {"nama": "Kabupaten Simalungun", "provinsi": "Sumatera Utara"},
    {"nama": "Kabupaten Karo", "provinsi": "Sumatera Utara"},
    {"nama": "Kota Tebing Tinggi", "provinsi": "Sumatera Utara"},
    
    # ========== SUMATERA BARAT (6 wilayah) ==========
    {"nama": "Kota Padang", "provinsi": "Sumatera Barat"},
    {"nama": "Kabupaten Padang Pariaman", "provinsi": "Sumatera Barat"},
    {"nama": "Kota Bukittinggi", "provinsi": "Sumatera Barat"},
    {"nama": "Kabupaten Agam", "provinsi": "Sumatera Barat"},
    {"nama": "Kota Payakumbuh", "provinsi": "Sumatera Barat"},
    {"nama": "Kabupaten Tanah Datar", "provinsi": "Sumatera Barat"},
    
    # ========== RIAU (5 wilayah) ==========
    {"nama": "Kota Pekanbaru", "provinsi": "Riau"},
    {"nama": "Kabupaten Kampar", "provinsi": "Riau"},
    {"nama": "Kota Dumai", "provinsi": "Riau"},
    {"nama": "Kabupaten Bengkalis", "provinsi": "Riau"},
    {"nama": "Kabupaten Siak", "provinsi": "Riau"},
    
    # ========== JAMBI (4 wilayah) ==========
    {"nama": "Kota Jambi", "provinsi": "Jambi"},
    {"nama": "Kabupaten Muaro Jambi", "provinsi": "Jambi"},
    {"nama": "Kabupaten Batanghari", "provinsi": "Jambi"},
    {"nama": "Kota Sungai Penuh", "provinsi": "Jambi"},
    
    # ========== SUMATERA SELATAN (5 wilayah) ==========
    {"nama": "Kota Palembang", "provinsi": "Sumatera Selatan"},
    {"nama": "Kabupaten Banyuasin", "provinsi": "Sumatera Selatan"},
    {"nama": "Kota Prabumulih", "provinsi": "Sumatera Selatan"},
    {"nama": "Kabupaten Ogan Komering Ilir", "provinsi": "Sumatera Selatan"},
    {"nama": "Kota Lubuklinggau", "provinsi": "Sumatera Selatan"},
    
    # ========== LAMPUNG (5 wilayah) ==========
    {"nama": "Kota Bandar Lampung", "provinsi": "Lampung"},
    {"nama": "Kabupaten Lampung Selatan", "provinsi": "Lampung"},
    {"nama": "Kota Metro", "provinsi": "Lampung"},
    {"nama": "Kabupaten Lampung Tengah", "provinsi": "Lampung"},
    {"nama": "Kabupaten Pesawaran", "provinsi": "Lampung"},
    
    # ========== KEPULAUAN RIAU & BANGKA BELITUNG (5 wilayah) ==========
    {"nama": "Kota Batam", "provinsi": "Kepulauan Riau"},
    {"nama": "Kabupaten Bintan", "provinsi": "Kepulauan Riau"},
    {"nama": "Kota Tanjungpinang", "provinsi": "Kepulauan Riau"},
    {"nama": "Kota Pangkal Pinang", "provinsi": "Kepulauan Bangka Belitung"},
    {"nama": "Kabupaten Bangka", "provinsi": "Kepulauan Bangka Belitung"},
    
    # ========== BANTEN (5 wilayah) ==========
    {"nama": "Kota Tangerang", "provinsi": "Banten"},
    {"nama": "Kabupaten Tangerang", "provinsi": "Banten"},
    {"nama": "Kota Cilegon", "provinsi": "Banten"},
    {"nama": "Kabupaten Serang", "provinsi": "Banten"},
    {"nama": "Kota Tangerang Selatan", "provinsi": "Banten"},
    
    # ========== DKI JAKARTA (5 wilayah administrasi) ==========
    {"nama": "Kota Administrasi Jakarta Pusat", "provinsi": "DKI Jakarta"},
    {"nama": "Kota Administrasi Jakarta Barat", "provinsi": "DKI Jakarta"},
    {"nama": "Kota Administrasi Jakarta Selatan", "provinsi": "DKI Jakarta"},
    {"nama": "Kota Administrasi Jakarta Timur", "provinsi": "DKI Jakarta"},
    {"nama": "Kota Administrasi Jakarta Utara", "provinsi": "DKI Jakarta"},
    
    # ========== JAWA BARAT (10 wilayah) ==========
    {"nama": "Kota Bandung", "provinsi": "Jawa Barat"},
    {"nama": "Kabupaten Bandung", "provinsi": "Jawa Barat"},
    {"nama": "Kota Bekasi", "provinsi": "Jawa Barat"},
    {"nama": "Kabupaten Bekasi", "provinsi": "Jawa Barat"},
    {"nama": "Kota Bogor", "provinsi": "Jawa Barat"},
    {"nama": "Kabupaten Bogor", "provinsi": "Jawa Barat"},
    {"nama": "Kota Depok", "provinsi": "Jawa Barat"},
    {"nama": "Kabupaten Cianjur", "provinsi": "Jawa Barat"},
    {"nama": "Kabupaten Sukabumi", "provinsi": "Jawa Barat"},
    {"nama": "Kota Sukabumi", "provinsi": "Jawa Barat"},
    
    # ========== JAWA TENGAH (10 wilayah) ==========
    {"nama": "Kota Semarang", "provinsi": "Jawa Tengah"},
    {"nama": "Kabupaten Semarang", "provinsi": "Jawa Tengah"},
    {"nama": "Kota Surakarta", "provinsi": "Jawa Tengah"},
    {"nama": "Kabupaten Sukoharjo", "provinsi": "Jawa Tengah"},
    {"nama": "Kota Magelang", "provinsi": "Jawa Tengah"},
    {"nama": "Kabupaten Magelang", "provinsi": "Jawa Tengah"},
    {"nama": "Kota Pekalongan", "provinsi": "Jawa Tengah"},
    {"nama": "Kabupaten Pekalongan", "provinsi": "Jawa Tengah"},
    {"nama": "Kota Tegal", "provinsi": "Jawa Tengah"},
    {"nama": "Kabupaten Tegal", "provinsi": "Jawa Tengah"},
    
    # ========== JAWA TIMUR (12 wilayah) ==========
    # TERMASUK KOTA KEDIRI dan KABUPATEN KEDIRI
    {"nama": "Kota Surabaya", "provinsi": "Jawa Timur"},
    {"nama": "Kabupaten Sidoarjo", "provinsi": "Jawa Timur"},
    {"nama": "Kota Malang", "provinsi": "Jawa Timur"},
    {"nama": "Kabupaten Malang", "provinsi": "Jawa Timur"},
    {"nama": "Kota Kediri", "provinsi": "Jawa Timur"},      # ✅ Kota tempat Anda tinggal!
    {"nama": "Kabupaten Kediri", "provinsi": "Jawa Timur"}, # ✅ Kabupaten Kediri
    {"nama": "Kota Blitar", "provinsi": "Jawa Timur"},
    {"nama": "Kabupaten Blitar", "provinsi": "Jawa Timur"},
    {"nama": "Kota Madiun", "provinsi": "Jawa Timur"},
    {"nama": "Kabupaten Madiun", "provinsi": "Jawa Timur"},
    {"nama": "Kabupaten Jember", "provinsi": "Jawa Timur"},
    {"nama": "Kabupaten Banyuwangi", "provinsi": "Jawa Timur"},
    
    # ========== D.I. YOGYAKARTA (4 wilayah) ==========
    {"nama": "Kota Yogyakarta", "provinsi": "DI Yogyakarta"},
    {"nama": "Kabupaten Sleman", "provinsi": "DI Yogyakarta"},
    {"nama": "Kabupaten Bantul", "provinsi": "DI Yogyakarta"},
    {"nama": "Kabupaten Gunungkidul", "provinsi": "DI Yogyakarta"},
    
    # ========== BALI (6 wilayah) ==========
    {"nama": "Kota Denpasar", "provinsi": "Bali"},
    {"nama": "Kabupaten Badung", "provinsi": "Bali"},
    {"nama": "Kabupaten Gianyar", "provinsi": "Bali"},
    {"nama": "Kabupaten Tabanan", "provinsi": "Bali"},
    {"nama": "Kabupaten Buleleng", "provinsi": "Bali"},
    {"nama": "Kabupaten Karangasem", "provinsi": "Bali"},
    
    # ========== NUSA TENGGARA BARAT & TIMUR (5 wilayah) ==========
    {"nama": "Kota Mataram", "provinsi": "Nusa Tenggara Barat"},
    {"nama": "Kabupaten Lombok Barat", "provinsi": "Nusa Tenggara Barat"},
    {"nama": "Kota Kupang", "provinsi": "Nusa Tenggara Timur"},
    {"nama": "Kabupaten Kupang", "provinsi": "Nusa Tenggara Timur"},
    {"nama": "Kabupaten Flores Timur", "provinsi": "Nusa Tenggara Timur"},
    
    # ========== KALIMANTAN (6 wilayah) ==========
    {"nama": "Kota Pontianak", "provinsi": "Kalimantan Barat"},
    {"nama": "Kabupaten Kubu Raya", "provinsi": "Kalimantan Barat"},
    {"nama": "Kota Banjarmasin", "provinsi": "Kalimantan Selatan"},
    {"nama": "Kota Balikpapan", "provinsi": "Kalimantan Timur"},
    {"nama": "Kota Samarinda", "provinsi": "Kalimantan Timur"},
    {"nama": "Kabupaten Kutai Kartanegara", "provinsi": "Kalimantan Timur"},
    
    # ========== SULAWESI (5 wilayah) ==========
    {"nama": "Kota Makassar", "provinsi": "Sulawesi Selatan"},
    {"nama": "Kabupaten Gowa", "provinsi": "Sulawesi Selatan"},
    {"nama": "Kota Manado", "provinsi": "Sulawesi Utara"},
    {"nama": "Kota Palu", "provinsi": "Sulawesi Tengah"},
    {"nama": "Kota Kendari", "provinsi": "Sulawesi Tenggara"},
]

print(f"📋 Total wilayah: {len(daftar_wilayah)} kabupaten/kota")

# ============================================================
# GENERATE DATA KOEFISIEN (REALISTIS)
# ============================================================
np.random.seed(42)  # Supaya hasil konsisten setiap kali dijalankan

n = len(daftar_wilayah)

# Data koefisien dengan variasi realistis
# Koefisien jarak: angka lebih tinggi = jarak ke pusat ekonomi sangat berpengaruh
koef_jarak = np.round(np.random.uniform(0.1, 2.8, n), 4)

# Koefisien lebar jalan: angka lebih tinggi = kondisi jalan sangat berpengaruh
koef_lebar = np.round(np.random.uniform(0.3, 3.2, n), 4)

# Tentukan dominasi berdasarkan perbandingan koefisien
dominasi = []
for i in range(n):
    if koef_jarak[i] > koef_lebar[i] * 1.2:  # Jarak 20% lebih besar
        dominasi.append("jarak")
    elif koef_lebar[i] > koef_jarak[i] * 1.2:  # Lebar jalan 20% lebih besar
        dominasi.append("lebar_jalan")
    else:
        dominasi.append("seimbang")

# Buat DataFrame
data = []
for i, wilayah in enumerate(daftar_wilayah):
    data.append({
        "nama_kabupaten": wilayah["nama"],
        "provinsi": wilayah["provinsi"],
        "koefisien_jarak": koef_jarak[i],
        "koefisien_lebar_jalan": koef_lebar[i],
        "dominasi": dominasi[i]
    })

df = pd.DataFrame(data)

# Tambahkan kolom kode wilayah (opsional, untuk referensi)
df.insert(0, "kode_wilayah", [f"IDN.{i+1:03d}" for i in range(n)])

# Simpan ke CSV
df.to_csv("data/sample_coefficients.csv", index=False)

# ============================================================
# TAMPILKAN STATISTIK DAN CONTOH DATA
# ============================================================
print("\n" + "="*60)
print("📊 STATISTIK DATA KOEFISIEN")
print("="*60)
print(f"Koefisien Jarak     -> Mean: {df['koefisien_jarak'].mean():.4f}, Std: {df['koefisien_jarak'].std():.4f}")
print(f"Koefisien Lebar Jalan -> Mean: {df['koefisien_lebar_jalan'].mean():.4f}, Std: {df['koefisien_lebar_jalan'].std():.4f}")
print(f"Distribusi Dominasi:")
print(f"  - Jarak      : {(df['dominasi'] == 'jarak').sum()} wilayah")
print(f"  - Lebar Jalan: {(df['dominasi'] == 'lebar_jalan').sum()} wilayah")
print(f"  - Seimbang   : {(df['dominasi'] == 'seimbang').sum()} wilayah")

print("\n" + "="*60)
print("📍 CONTOH DATA (5 WILAYAH PERTAMA)")
print("="*60)
print(df.head().to_string(index=False))

# ============================================================
# TAMPILKAN KHUSUS DATA KEDIRI
# ============================================================
print("\n" + "="*60)
print("🏠 DATA KHUSUS WILAYAH KEDIRI (Tempat Tinggal Anda)")
print("="*60)
kediri_data = df[(df['nama_kabupaten'] == 'Kota Kediri') | (df['nama_kabupaten'] == 'Kabupaten Kediri')]
if not kediri_data.empty:
    for _, row in kediri_data.iterrows():
        print(f"\n📍 {row['nama_kabupaten']}, {row['provinsi']}")
        print(f"   Koefisien Jarak      : {row['koefisien_jarak']}")
        print(f"   Koefisien Lebar Jalan: {row['koefisien_lebar_jalan']}")
        print(f"   Dominasi             : {row['dominasi'].upper()}")
        
        # Interpretasi sederhana untuk pembelajaran
        if row['dominasi'] == 'jarak':
            print(f"   💡 Interpretasi: Wilayah ini perlu prioritas PEMENDEKAN JARAK ke pusat ekonomi.")
        elif row['dominasi'] == 'lebar_jalan':
            print(f"   💡 Interpretasi: Wilayah ini perlu prioritas PELEBARAN/PEMBANGUNAN JALAN.")
        else:
            print(f"   💡 Interpretasi: Wilayah ini perlu peningkatan JARAK dan JALAN secara SEIMBANG.")
else:
    print("⚠️ Data Kediri tidak ditemukan, periksa daftar wilayah.")

print("\n" + "="*60)
print("✅ File berhasil disimpan di: data/sample_coefficients.csv")
print("="*60)
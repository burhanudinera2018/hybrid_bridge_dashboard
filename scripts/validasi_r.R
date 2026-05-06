# scripts/validasi_r.R
library(sf)
library(dplyr)
library(readr)
library(jsonlite)

# Baca CSV
df <- read_csv("data/sample_coefficients.csv", show_col_types = FALSE)

# Hitung statistik
statistik <- list(
  koefisien_jarak = list(
    mean = mean(df$koefisien_jarak, na.rm = TRUE),
    sd = sd(df$koefisien_jarak, na.rm = TRUE),
    min = min(df$koefisien_jarak, na.rm = TRUE),
    max = max(df$koefisien_jarak, na.rm = TRUE)
  ),
  koefisien_lebar_jalan = list(
    mean = mean(df$koefisien_lebar_jalan, na.rm = TRUE),
    sd = sd(df$koefisien_lebar_jalan, na.rm = TRUE),
    min = min(df$koefisien_lebar_jalan, na.rm = TRUE),
    max = max(df$koefisien_lebar_jalan, na.rm = TRUE)
  )
)

# Pastikan folder outputs ada
if (!dir.exists("outputs")) {
  dir.create("outputs")
}

# Simpan sebagai JSON
write_json(statistik, "outputs/statistik_r.json", auto_unbox = TRUE)

# Simpan CSV
write_csv(df, "outputs/koefisien_r.csv")

cat("✅ Validasi R selesai\n")
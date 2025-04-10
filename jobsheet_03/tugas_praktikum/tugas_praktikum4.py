# 4. Diketahui data berat bada mahasiswa informatika polines kelas IK-2E adalah sebagai berikut.
# Berat Badan(kg)	Frekuensi
#    41 – 45	        2
#    46 – 50	        3
#    50 – 55	        6
#    56 – 60	        4
#    61 – 65	        5
#    66 – 70	        2
# Hitunglah standart deviasi dari data berat badan mahasiswa informatika tersebut.

import numpy as np

# Data kelas berat badan dan frekuensi
kelas = [(41, 45), (46, 50), (50, 55), (56, 60), (61, 65), (66, 70)]
frekuensi = [2, 3, 6, 4, 5, 2]

# Hitung titik tengah untuk setiap kelas
titik_tengah = [(batas_bawah + batas_atas) /
                2 for batas_bawah, batas_atas in kelas]

# Buat data mentah berdasarkan titik tengah dan frekuensinya
data_mentah = []
for berat, frek in zip(titik_tengah, frekuensi):
    data_mentah.extend([berat] * frek)

# Hitung standar deviasi dengan NumPy, menggunakan ddof=1 untuk sampel
standar_deviasi = np.std(data_mentah, ddof=1)
print("Standar Deviasi Sampel (menggunakan NumPy, ddof=1):", standar_deviasi)

# Hitung standar deviasi dengan NumPy, menggunakan ddof=0 untuk populasi
standar_deviasi = np.std(data_mentah, ddof=0)
print("Standar Deviasi Populasi (menggunakan NumPy, ddof=0):", standar_deviasi)

# --------------------------------------------
# 📘 Konsep Utama:

# 1. import numpy as np
#    🔹 Library Importing: Mengimpor pustaka NumPy yang digunakan untuk perhitungan numerik,
#      termasuk mean dan standar deviasi.

# 2. kelas = [(41, 45), (46, 50), ...]
#    🔹 Interval Kelas: Menyimpan rentang kelas berat badan dalam bentuk tuple (batas bawah, batas atas).

# 3. frekuensi = [2, 3, 6, 4, 5, 2]
#    🔹 Frekuensi: Menyimpan jumlah mahasiswa dalam tiap interval berat badan.

# 4. titik_tengah = [(batas_bawah + batas_atas) / 2 for ...]
#    🔹 Titik Tengah (Midpoint): Titik tengah tiap kelas digunakan sebagai representasi nilai dari kelas tersebut.
#      Dihitung dengan rumus: (batas bawah + batas atas) / 2

# 5. data_mentah.extend([berat] * frek)
#    🔹 Data Mentah dari Frekuensi: Mengonversi data berfrekuensi menjadi daftar nilai yang bisa dianalisis
#      dengan menggandakan titik tengah sebanyak frekuensinya.

# 6. np.std(data_mentah, ddof=1)
#    🔹 Standar Deviasi Sampel: Menghitung standar deviasi dengan `ddof=1` untuk mengasumsikan data adalah sampel.
#      Rumus: √(Σ(xi - x̄)² / (n - 1))

# 7. np.std(data_mentah, ddof=0)
#    🔹 Standar Deviasi Populasi: Menghitung standar deviasi dengan `ddof=0` untuk asumsi bahwa data mencakup seluruh populasi.
#      Rumus: √(Σ(xi - μ)² / n)

# 8. print(...)
#    🔹 Output Display: Menampilkan hasil perhitungan standar deviasi ke terminal.

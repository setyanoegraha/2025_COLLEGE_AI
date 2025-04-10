# Tugas Praktikum
# 3. Pada sebuah kelas memiliki nilai hasil ujian yaitu:
# 50, 54, 62, 50, 52, 59, 61, 63, 65, 10, 53, 63, 65, 50, 59, 62, 50, 51, 57, 60, 63, 65, 65, 53, 99
# Berdasarkan data hasil ujian tersebut, tentukan:
# a. Urutkan data dari yang terkecil sampai data yang terbesar
# b. Identifikasi nilai first quartile (Q1) dan third quartile (Q3), dan IQR
# c. Tentukan nilai upper bound dan lower bound
# d. Tentukan nilai ujian yang menjadi outlier berdasarkan data hasil ujian diatas

import numpy as np

# Data Ujian
data = [50, 54, 62, 50, 52, 59, 61, 63, 65, 10, 53, 63,
        65, 50, 59, 62, 50, 51, 57, 60, 63, 65, 65, 53, 99]
print(f"Data Ujian Tidak Terurut: {data}\n")

# a. Urutkan data dari yang terkecil sampai yang terbesar
sorted_data = sorted(data)
print(f"Data Ujian Terurut (Kecil ke Besar): {sorted_data}\n")

# b. Identifikasi nilai first quartile (Q1) dan third quartile (Q3), dan IQR
Q1 = np.percentile(sorted_data, 25)
Q3 = np.percentile(sorted_data, 75)
IQR = Q3 - Q1
print(f"Nilai First Quartile (Q1): {Q1}")
print(f"Nilai Third Quartile (Q3): {Q3}")
print(f"Nilai IQR: {IQR}\n")

# c. Tentukan nilai upper bound dan lower bound
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(f"Nilai Lower Bound: {lower_bound}")
print(f"Nilai Upper Bound: {upper_bound}\n")

# d. Tentukan nilai ujian yang menjadi outlier berdasarkan hasil ujian di atas
outliers = []
for nilai_ujian in data:
    if nilai_ujian < lower_bound or nilai_ujian > upper_bound:
        outliers.append(nilai_ujian)
print(f"Nilai Ujian yang Outlier: {outliers}")

# --------------------------------------------
# 📘 Konsep Utama:

# 1. import numpy as np
#    🔹 Library Importing: Mengimpor pustaka NumPy yang digunakan untuk perhitungan statistik numerik seperti percentil dan IQR.

# 2. data = [...]
#    🔹 Data List: Menyimpan seluruh nilai ujian dalam bentuk list Python.

# 3. sorted_data = sorted(data)
#    🔹 Data Sorting: Mengurutkan data dari yang terkecil ke yang terbesar untuk keperluan analisis statistik.

# 4. np.percentile(sorted_data, 25) & np.percentile(sorted_data, 75)
#    🔹 Percentile Calculation:
#       - Q1 (25th percentile): Nilai di bawah 25% data.
#       - Q3 (75th percentile): Nilai di bawah 75% data.
#       - Berguna untuk mengukur sebaran data.

# 5. IQR = Q3 - Q1
#    🔹 Interquartile Range (IQR): Selisih antara Q3 dan Q1. Digunakan untuk mendeteksi outlier.

# 6. lower_bound = Q1 - 1.5 * IQR & upper_bound = Q3 + 1.5 * IQR
#    🔹 Outlier Boundaries:
#       - Lower Bound: Nilai terkecil yang masih dianggap normal.
#       - Upper Bound: Nilai terbesar yang masih dianggap normal.

# 7. for nilai_ujian in data:
#        if nilai_ujian < lower_bound or nilai_ujian > upper_bound:
#            outliers.append(nilai_ujian)
#    🔹 Outlier Detection: Mengecek setiap nilai apakah lebih kecil dari lower bound atau lebih besar dari upper bound.
#      Jika ya, maka dianggap sebagai *outlier* dan dimasukkan ke list `outliers`.

# 8. print(...)
#    🔹 Output Display: Menampilkan hasil dari setiap langkah proses analisis ke layar.

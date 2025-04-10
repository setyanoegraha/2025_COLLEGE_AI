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

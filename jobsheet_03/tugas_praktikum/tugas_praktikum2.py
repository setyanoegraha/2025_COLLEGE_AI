# Tugas Praktikum
# 2. Diketahui sebuah deret data 9, 10, 11, 6, 8, 7, 7, 5, 4, 5.
# Tentukan persentil ke-25 dan persentil ke-75!

import numpy as np

data = [9, 10, 11, 6, 8, 7, 7, 5, 4, 5]

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

print(f"Data: {data}")
print(f"Persentil ke-25 (Q1): {Q1}")
print(f"Persentil ke-75 (Q3): {Q3}")

# --------------------------------------------
# 📘 Konsep Utama:

# 1. from scipy import stats & import numpy as np
#    🔹 Library Importing: Mengimpor pustaka SciPy dan NumPy untuk analisis statistik dan numerik.

# 2. data = [...]
#    🔹 List: Menyimpan data numerik dalam list Python.

# 3. np.percentile(data, 25) dan np.percentile(data, 75)
#    🔹 Percentile Calculation: Fungsi `np.percentile` menghitung nilai pada persentil tertentu.
#      - Persentil ke-25 (Q1): 25% dari data berada di bawah nilai ini.
#      - Persentil ke-75 (Q3): 75% dari data berada di bawah nilai ini.

# 4. print(...)
#    🔹 Output Display: Menampilkan hasil perhitungan persentil ke terminal.

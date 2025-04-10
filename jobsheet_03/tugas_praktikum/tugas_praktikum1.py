# Tugas Praktikum
# 1. Pelemparan dadu sebanyak 25 kali.
# Angka yang keluar datanya adalah: 1 2 3 4 5 5 6 2 3 4 5 6 6 4 3 2 1 4 3 5 6 6 5 4 5
# Modus dari data di atas adalah ...

from scipy import stats

dadu = [1, 2, 3, 4, 5, 5, 6, 2, 3, 4, 5, 6,
        6, 4, 3, 2, 1, 4, 3, 5, 6, 6, 5, 4, 5]
x = stats.mode(dadu, keepdims=True)
print(dadu)
print(f"Modus dari data di atas adalah {x.mode[0]}")

# --------------------------------------------
# 📘 Konsep Utama:

# 1. from scipy import stats
#    🔹 Library Importing: Mengimpor modul statistik dari pustaka SciPy untuk analisis data seperti modus, mean, dst.

# 2. dadu = [...]
#    🔹 List (Array): Menyimpan sekumpulan data (hasil pelemparan dadu sebanyak 25 kali) dalam bentuk list Python.

# 3. stats.mode(dadu, keepdims=True)
#    🔹 Statistical Function: Menghitung modus (nilai yang paling sering muncul) dari data.
#    🔹 keepdims=True: Menjaga agar hasil tetap dalam bentuk array berdimensi sesuai format terbaru SciPy.

# 4. print(dadu)
#    🔹 Output Display: Menampilkan seluruh data list ke terminal.

# 5. print(f"... {x.mode[0]}")
#    🔹 Formatted String (f-string): Menyisipkan nilai variabel langsung ke dalam string.
#    🔹 x.mode[0]: Mengakses nilai modus dari array hasil fungsi stats.mode.

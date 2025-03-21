import numpy as np

# Membuat matriks di python
A = np.array([[80, 30, 25],
              [50, 20, 10]])
B = np.array([[30, 60, 15],
              [10, 30, 30]])
hasil = A + B
print("Membuat Matriks di python")
print(f"Hasil:\n{hasil}\n")

# Melakukan operasi dot product
A = np.array([10, 20, 15])
B = np.array([16, 67, 35])

hasil = np.dot(A, B)
print("Melakukan Operasi dot product")
print(f"Hasil:\n{hasil}\n")

# Melakukan operasi cross product
A = np.array([10, 20, 15])
B = np.array([16, 67, 35])

hasil = np.cross(A, B)
print("Melakukan operasi cross product")
print(f"Hasil:\n{hasil}\n")

import numpy as np

# Mendefinisakn Matriks
A = np.array([[3, 1], [2, 0]])
B = np.array([[2, 1], [1, -1]])
C = np.array([[-1, 1, 2], [2, 0, -1]])

# Melakukan Perkalian
A_B = np.dot(A, B)
B_C = np.dot(B, C)

# Hasil Perkalian
print(f"Hasil A.B:\n{A_B}")
print(f"Hasil B.C:\n{B_C}\n")

import numpy as np

# Definisi vektor A dan B
A = np.array([5, 3, 7])
B = np.array([12, -3, 1])

# Menghitung panjang (magnitudo) vektor
magnitude_A = np.linalg.norm(A)
magnitude_B = np.linalg.norm(B)

# Menghitung perkalian titik (dot product)
dot_product = np.dot(A, B)

# Menghitung perkalian silang (cross product)
cross_product = np.cross(A, B)

# Menampilkan hasil
print("Panjang Vektor A:", round(magnitude_A, 2))
print("Panjang Vektor B:", round(magnitude_B, 2))
print("A . B (Dot Product):", dot_product)
print("A x B (Cross Product):", cross_product)

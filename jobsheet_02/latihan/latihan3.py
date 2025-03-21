import math

# Trigonometri
angle = math.radians(30)  # Konversi 30 derajat ke radian
print(f"sin(30): {math.sin(angle)}")
print(f"cos(30): {math.cos(angle)}")
print(f"tan(30): {math.tan(angle)}\n")

# Logaritma
num = 100
print(f"log({num}): {math.log(num)}")
print(f"log10({num}): {math.log10(num)}\n")

# Konversi Sudut
radian_value = math.pi / 4
print(f"{radian_value} radian dalam derajat: {math.degrees(radian_value)}\n")

# Jarak antara dua titik
point1 = (3, 4)
point2 = (6, 8)
print(f"Jarak antara {point1} dan {point2}: {math.dist(point1, point2)}\n")

# Faktorial
n = 5
print(f"Faktorial dari {n}: {math.factorial(n)}\n")

# Modulo floating point
a, b = 7.5, 2.3
print(f"{a} mod {b}: {math.fmod(a, b)}\n")

# Cek NaN (Not a Number)
value = float('nan')
print(f"Apakah {value} NaN? {math.isnan(value)}\n")

# Fungsi Gamma
x = 5
print(f"Gamma({x}): {math.gamma(x)}\n")

# Permutasi
n, k = 5, 3
print(f"Permutasi P({n}, {k}): {math.perm(n, k)}")

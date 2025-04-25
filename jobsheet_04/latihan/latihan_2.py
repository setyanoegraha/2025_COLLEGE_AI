import pandas as pd

# A. Memuat Series dari sebuah List Python
print("\n=== A. Memuat Series dari sebuah List Python ===")
li = [1, 7, 2]
se = pd.Series(li)

print(se)

# B. Mengakses Elemen pada Series
print("\n=== B. Mengakses Elemen pada Series ===")
li = [1, 7, 2]
se = pd.Series(li)

print(se[0])

# C. Memberi Label pada Series
print("\n=== C. Memberi Label pada Series ===")
li = [1, 7, 2]
se = pd.Series(li, index=['x', 'y', 'z'])

print(se['x'])

# D. Membuat Series dari Dictionary
print("\n=== D. Membuat Series dari Dictionary ===")
calories = {'day1': 420, 'day2': 380, 'day3': 390}
se = pd.Series(calories)

print(se)

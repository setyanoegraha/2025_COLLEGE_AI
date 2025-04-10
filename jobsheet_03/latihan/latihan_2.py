# 2. Spread
import numpy as np

# a. Mendapatkan Nilai Range
data = [2, 3, 7, 8, 9, 12, 15, 20, 50, 42]

minimum = np.min(data)
maximum = np.max(data)
x = maximum - minimum

print(f"Nilai minimum dari data {data} adalah {minimum}")
print(f"Nilai maksimum dari data {data} adalah {maximum}")
print(f"Nilai range dari data {data} adalah {x}\n")


# b. Mendapatkan Nilai Percentile
data = [90, 80, 70, 65, 110, 80, 83, 67, 94]

x = np.percentile(data, 90)

print(f"Nilai percentile ke-90 dari data {data} adalah {x}\n")


# c. Mendapatkan Nilai Quartile dan Interquartile Range
data = [3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10]

Q1 = np.median(data[:int(len(data)/2)])
Q3 = np.median(data[int(len(data)/2):])
IQR = Q3 - Q1

print(f"Quartile 1 dari data {data} adalah {Q1}")
print(f"Quartile 3 dari data {data} adalah {Q3}")
print(f"Interquartile range dari data {data} adalah {IQR}\n")


# d. Mendapatkan Nilai Variance dan Standart Deviation
data = [86, 87, 88, 86, 87, 85, 86]
mean = np.mean(data)
var = np.var(data)
std = np.std(data)

print(f"Nilai rata-rata dari data {data} adalah {mean:.2f}")
print(f"Nilai variance dari data {data} adalah {var:.2f}")
print(f"Nilai standart deviation dari data {data} adalah {std:.2f}\n")

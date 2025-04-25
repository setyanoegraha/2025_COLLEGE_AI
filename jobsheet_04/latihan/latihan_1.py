import pandas as pd

file_path = r'D:\Kuliah\Semester2\Artificial_Intelligence\semua_kode\jobsheet_04\latihan\data_csv.csv'
df = pd.read_csv(file_path)
print(df.to_string())

print(df)

print(pd.options.display.max_rows)

pd.options.display.max_rows = 9999
df = pd.read_csv(file_path)
print(df)

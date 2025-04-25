import pandas as pd

# A. Membuat DataFrame
print("\nA. Membuat DataFrame:")

df = pd.DataFrame(data={"Nama": ["Ali", "Joko", "Adi"],
                        "Umur": [12, 13, 15],
                        "Kelas": [6, 7, 8]})

print(df.columns)

df.columns.values[0] = "Nama Singkat"
print(df)

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)

# B. Mengakses Elemen pada DataFrame
print("\nB. Mengakses Elemen pada DataFrame:")
print(df.iloc[0:2, [0, 1]])
print(df.iloc[0:2, 0:2])
print(df.iloc[:, 0:2])
print(df.loc[0:2, :'calories'])
print(df.loc[0:2, ['calories', 'duration']])
print(df['calories'])
print(df['calories'][0])
print(df[['calories']])
print(df[['calories']].loc[[0, 1]])

# C. Memberi Nama pada Index
print("\nC. Memberi Nama pada Index:")
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(df)

print(df)

# D. Melihat DataFrame
print("\nD. Melihat DataFrame:")
file_path_csv = r'D:\Kuliah\Semester2\Artificial_Intelligence\semua_kode\jobsheet_04\latihan\data_csv.csv'
df = pd.read_csv(file_path_csv)
print(df)
print(df.head())
print(df.tail())
print(df.head(10))
print(df.shape)
print(df.dtypes)

# E. Membaca Informasi pada DataFrame
print("\nE. Membaca Informasi pada DataFrame:")
print(df.info())
print(df.describe())
print(df['Calories'].mean(), df["Calories"].median(), df["Calories"].mode()[0])
print(df.corr())

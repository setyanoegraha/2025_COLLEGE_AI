import pandas as pd

# A. Membaca file CSV
print("\nMembaca CSV file: ")
file_path_csv = r'D:\Kuliah\Semester2\Artificial_Intelligence\semua_kode\jobsheet_04\latihan\data_csv.csv'
df = pd.read_csv(file_path_csv)
print(df.to_string())
print(df)

print(pd.options.display.max_rows)

pd.options.display.max_rows = 9999
df = pd.read_csv(file_path_csv)
print(df)

# B. Membaca file JSON
print("\nMembaca JSON file: ")
file_path_json = r'D:\Kuliah\Semester2\Artificial_Intelligence\semua_kode\jobsheet_04\latihan\data_json.json'
df = pd.read_json(file_path_json)
print(df.to_string())

# C. Menggunakan Parameter pada Pandas Read
print("\nMembaca CSV file dengan parameter:")
df = pd.read_csv(file_path_csv, sep=';', header=0)
print(df)

# D. Membaca Custom Data
data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282
    }
}

print("\nMembaca Custom data:")
df = pd.DataFrame(data)
print(df)

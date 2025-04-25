import pandas as pd

# 1. Load dataset “Top Score English Premier League (EPL) musim 2020/2021” dan ubah menjadi dataframe
dataset_path = r'D:\Kuliah\Semester2\Artificial_Intelligence\semua_kode\jobsheet_04\tugas_praktikum\epl-goalScorer(20-21).csv'
df = pd.read_csv(dataset_path)
print(df)

# 2. Ambil 5 data pertama dari dataset
print("5 Data Pertama:")
print(df.head())

# 3. Tampilkan jumlah baris dan jumlah kolom dari dataset
print("\nJumlah Baris dan Kolom:")
print(f"Baris: {df.shape[0]}, Kolom: {df.shape[1]}")

# 4. Tampilkan tipe data dari masing-masing kolom dataset
print("\nTipe Data Kolom:")
print(df.dtypes)

# 5. Tampilkan jumlah goal yang dicetak setiap pemain yang terdapat di dataset
print("\nJumlah Goal Setiap Pemain:")
print(df[['player_name', 'goals']])

# 6. Tampilkan dataframe yang hanya terdiri dari nama pemain, goal, posisi, nama klub pemain, dan jumlah kartu kuning
print("\nDataframe dengan Kolom Tertentu:")
selected_columns = df[['player_name', 'goals',
                       'position', 'team_title', 'yellow_cards']]
print(selected_columns)

# 7. Tampilkan semua pemain dari klub “Liverpool”
print("\nPemain dari Klub Liverpool:")
liverpool_players = df[df['team_title'] == 'Liverpool']
print(liverpool_players)

# 8. Tampilkan semua pemain dari klub “Arsenal”
print("\nPemain dari Klub Arsenal:")
arsenal_players = df[df['team_title'] == 'Arsenal']
print(arsenal_players)

# 9. Tampilkan 10 pemain yang memiliki jumlah kartu kuning paling banyak di EPL musim 2020/2021
print("\n10 Pemain dengan Kartu Kuning Terbanyak:")
top_yellow_cards = df.nlargest(10, 'yellow_cards')
print(top_yellow_cards[['player_name', 'yellow_cards']])

# 10. Tampilkan 10 pemain yang memiliki jumlah kartu merah paling banyak di EPL musim 2020/2021
print("\n10 Pemain dengan Kartu Merah Terbanyak:")
top_red_cards = df.nlargest(10, 'red_cards')
print(top_red_cards[['player_name', 'red_cards']])

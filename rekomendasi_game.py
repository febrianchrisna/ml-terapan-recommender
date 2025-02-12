# -*- coding: utf-8 -*-
"""rekomendasi_game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kqh868CfGly9BYOXb0PSGUYAsrVzR6Wi

# Data Loading
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Import library yang akan di butuhkan"""

game = pd.read_csv('/content/Metacritic_games_of_all_time.csv')
game

"""Load dataset yang akan di gunakan ke dalam variabel game

# Exploratory Data Analysis
"""

game.info()

"""Deskripsi Variabel:
- unamed:	ID unik untuk setiap game (numerik)
- title:	Judul game (kategorikal)
- release:	Tanggal rilis game (kategorikal)
- platform:	Platform tempat game dirilis (kategorikal)
- critic_score:	Skor dari kritikus (numerik)
- user_score:	Skor dari pengguna (kategorikal)
- developer:	Pengembang game (kategorikal)
- genre(s):	Genre atau jenis game (kategorikal)
- rating:	Rating konten game (kategorikal)
"""

game = game.rename(columns={'Unnamed: 0': 'game_id'})

"""Dilakukan penamaan untuk kolom unnamed menjadi game_id"""

print('Jumlah judul game: ', len(game.title.unique()))

"""Jumlah data judul/title game pada dataset ini ada 9909

## Univariate Analyisis
"""

plt.figure(figsize=(10, 6))
sns.countplot(x='platform', data=game)
plt.title('Distribution of Platform')
plt.xlabel('Platform')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

"""Insight:
- PC memiliki jumlah game terbanyak, menunjukkan popularitas yang sangat tinggi.
- Xbox One dan Nintendo Switch memiliki jumlah game yang signifikan, mencerminkan basis pengguna yang besar dan permintaan tinggi.
- PlayStation 4 dan PlayStation 3 masih memiliki banyak game, meskipun PlayStation 5 sudah diluncurkan.
- Xbox 360 menunjukkan penurunan jumlah game dibandingkan Xbox One.
- Platform yang lebih tua seperti PlayStation 2, 3DS, dan Wii U menunjukkan jumlah game yang lebih sedikit, mencerminkan penurunan popularitas.
- Xbox Series X dan PlayStation 5 memiliki jumlah game terbatas, kemungkinan karena keduanya baru dirilis.
- PlayStation Vita dan Stadia memiliki jumlah game yang sangat sedikit, menunjukkan kurangnya dukungan atau ketidakpopuleran.

"""

plt.figure(figsize=(10, 6))
sns.countplot(x='rating', data=game)
plt.title('Distribution of Content Rating')
plt.xlabel('Content Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

"""Insight:

- Rating T (Teen) mendominasi, dengan lebih dari 4.000 game, menunjukkan bahwa sebagian besar game ditujukan untuk audiens remaja.
- Rating M (Mature) juga signifikan, dengan lebih dari 2.000 game, mencerminkan banyaknya game untuk audiens dewasa.
- Rating E (Everyone) dan E10+ (10 tahun ke atas) memiliki jumlah game yang lebih sedikit, menunjukkan bahwa game untuk segala usia masih ada, namun kurang banyak.
- Rating KA (Kids to Adults), RP (Rating Pending), dan AO (Adults Only) sangat jarang, mencerminkan kategori game yang lebih niche atau masih menunggu penilaian.
"""

genre_counts = game['genre(s)'].str.split(',').explode().value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.title('Top 10 Game Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

"""Insight:

- Genre General mendominasi dengan lebih dari 5.000 entri, menunjukkan bahwa banyak game memiliki genre yang lebih umum.
- Genre Action juga sangat dominan, dengan lebih dari 3.000 game, mencerminkan popularitas besar game aksi di kalangan pemain.
- Shooter dan Action Adventure masing-masing memiliki jumlah game yang signifikan, menunjukkan bahwa game dengan aksi cepat dan cerita petualangan sangat digemari.
- Arcade dan Role-Playing memiliki jumlah game yang lebih rendah, tetapi masih cukup relevan, menunjukkan keberagaman jenis game yang disukai pemain.
- Adventure, First-Person, Sci-Fi, dan Strategy menunjukkan jumlah yang lebih sedikit, tetapi masih masuk dalam genre populer meskipun kurang mendominasi dibandingkan genre lainnya.
- Dalam dataset ini, sebagian besar game memiliki lebih dari satu genre, yang menjelaskan mengapa genre General mendominasi dengan jumlah game terbanyak

"""

genre_counts = game['developer'].str.split(',').explode().value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.title('Top 10 Game Developer')
plt.xlabel('Genre')
plt.ylabel('Developer')
plt.xticks(rotation=45)
plt.show()

"""Insight:
- Ubisoft mendominasi dengan jumlah game terbanyak, lebih dari 600 game. Ini menunjukkan bahwa Ubisoft adalah salah satu pengembang terbesar dan paling produktif dalam industri game.
- Electronic Arts (EA) dan Activision mengikuti dengan jumlah game yang signifikan, yang mencerminkan peran besar mereka dalam merilis game-game populer di berbagai platform.
- SCEI (Sony Computer Entertainment America) juga menunjukkan kontribusi besar dalam industri game, mencerminkan popularitas konsol PlayStation dan game eksklusif yang mereka kembangkan.
- Pengembang seperti Sega, Capcom, dan Square Enix juga menunjukkan jumlah game yang cukup banyak, yang menandakan kekuatan mereka dalam menciptakan franchise ikonik, seperti Sega dengan Sonic, Capcom dengan Street Fighter, dan Square Enix dengan Final Fantasy.
- Microsoft Game Studios, Nintendo, dan Konami memiliki jumlah game yang lebih sedikit dibandingkan pengembang lainnya, tetapi tetap penting, dengan kontribusi besar terhadap game eksklusif di platform mereka masing-masing, seperti Halo (Microsoft) dan Super Mario (Nintendo).

"""

plt.figure(figsize=(8, 6))
sns.histplot(game['critic_score'].dropna(), kde=True)
plt.title('Distribution of critic scores')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.show()

"""Insight:

- Distribusi Skor: Skor kritik cenderung terkonsentrasi di kisaran 60 hingga 85, dengan puncak frekuensi tertinggi sekitar 80. Ini menunjukkan bahwa sebagian besar game mendapatkan skor yang cukup baik, tetapi tidak banyak yang mendapatkan skor mendekati 100, yang biasanya menunjukkan game dengan kualitas sangat tinggi.
- Skor Tinggi dan Skor Rendah: Skor di bawah 40 memiliki frekuensi yang jauh lebih rendah, menunjukkan bahwa sangat sedikit game yang mendapatkan penilaian sangat buruk dari para kritikus. Sebaliknya, game dengan skor sangat tinggi (di atas 90) juga jarang ditemui.
- Skor Bias Terhadap Positif: Kurva distribusi menunjukkan sedikit bias ke arah skor positif, dengan konsentrasi besar pada skor sekitar 70 hingga 85, yang mungkin menunjukkan bahwa sebagian besar game diterima dengan baik oleh kritikus, namun tidak banyak yang mencapai status luar biasa.
- Skor Konsisten: Banyak game mendapatkan skor yang relatif seragam, berada dalam rentang yang tidak terlalu ekstrem, menandakan bahwa banyak game yang berfungsi dengan baik tetapi tidak terlalu menonjol dalam hal kualitas luar biasa atau kekurangan signifikan.


"""

max_rating = game['critic_score'].max()
mean_rating = game['critic_score'].mean()
min_rating = game['critic_score'].min()

print(f"Max Rating: {max_rating}")
print(f"Mean Rating: {mean_rating}")
print(f"Min Rating: {min_rating}")

plt.figure(figsize=(8, 6))
sns.histplot(game['user_score'].dropna(), kde=True)
plt.title('Distribution of User Scores')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.show()

"""Insight:

- Skor 'TBD' (To Be Determined) memiliki frekuensi tertinggi, dengan lebih dari 790 entri. Hal ini menunjukkan bahwa banyak game tidak memiliki skor yang diberikan oleh pengguna atau belum diberi penilaian oleh mereka, yang bisa disebabkan oleh pengaturan platform atau ketidakhadiran ulasan pengguna pada beberapa game.
- Skor Pengguna di Rentang 7.0-7.9 mendominasi, dengan skor 7.7, 7.6, 7.8, dan 7.5 memiliki jumlah yang signifikan (lebih dari 500 entri untuk setiap skor). Ini mencerminkan bahwa sebagian besar game mendapatkan penilaian yang cukup baik dari pengguna, namun tidak banyak yang mendapatkan penilaian luar biasa (di atas 9).
- Distribusi yang Cenderung Positif, meskipun ada variasi, distribusi menunjukkan dominasi di kisaran skor yang lebih tinggi, menunjukkan bahwa mayoritas game diterima dengan cukup baik oleh pengguna. Tidak banyak game yang mendapat skor sangat rendah atau sangat tinggi.
- Skor yang lebih rendah, seperti 6.0 ke bawah, jarang muncul dalam dataset, yang menunjukkan bahwa sangat sedikit game yang mendapat penilaian buruk oleh pengguna.
"""

print('User Score: ', game.user_score.unique())

"""Terdapat tbd dan nilai kosong pada user_score ini"""

top_10_uscore = game['user_score'].value_counts().nlargest(10)
top_10_uscore

"""Dapat dilihat bahwa tbd(To Be Determined) menduduki data dengan jumlah paling banyak pada user_score, yang menunjukkan bahwa skor pengguna belum ditentukan

# Data Preparation

## Kesalahan Tipe Data
"""

game.info()

"""Terdapat kesalahan pada tipe data di kolom user_score. Meskipun nilai skor seharusnya berupa angka numerik, kolom user_score saat ini bertipe object (string), yang berpotensi menyulitkan dalam analisis dan perhitungan lebih lanjut. Selain itu, pada kolom user_score, terdapat nilai "tbd" (To Be Determined), yang menunjukkan bahwa skor pengguna belum ditentukan. Agar data lebih konsisten dan siap untuk analisis, "tbd" akan diganti dengan nilai 0."""

game['user_score'] = pd.to_numeric(game['user_score'], errors='coerce')

print(game['user_score'].dtype)

"""## Missing Value"""

game.isna().sum()

"""Karena dataset ini memiliki jumlah sampel yang besar (14.666 entri), missing value dapat diatasi dengan menghapus baris yang mengandung nilai yang hilang tanpa mempengaruhi kualitas analisis secara signifikan. Menghapus baris dengan missing value di kolom-kolom tersebut adalah solusi yang tepat karena penghapusan ini tidak akan mengurangi banyak data dan dataset tetap akan representatif untuk analisis selanjutnya."""

nan_critic_score = game[game['critic_score'].isna()]
nan_critic_score

game.dropna(subset=['critic_score', 'user_score'], inplace=True)

rating = game[game['rating'].isna()]
rating

game.dropna(subset=['rating'], inplace=True)

game.shape

game.isna().sum()

"""Data sudah bersih dari Missing Value

## Duplikasi Data
"""

game['title'].value_counts()

"""Terlihat bahwa terdapat duplikasi data pada kolom title (judul game). Beberapa game muncul lebih dari satu kali, seperti Resident Evil: Revelations yang tercatat 7 kali, Final Fantasy X / X-2 HD Remaster yang tercatat 6 kali, dan lainnya. Hal ini bisa mempengaruhi kualitas rekomendasi yang dihasilkan, karena sistem rekomendasi bisa memberi bobot yang berlebihan pada game yang terduplikasi. Untuk mengatasi masalah ini,  dilakukan drop duplikasi pada kolom title untuk memastikan bahwa setiap game hanya tercatat sekali dalam dataset. Dengan menghapus duplikasi ini, dataset akan lebih konsisten dan relevan, sehingga hasil rekomendasi akan lebih akurat"""

game_filtered = game[game['title'] == "Resident Evil: Revelations"]
game_filtered

game = game[~game['title'].duplicated(keep='first')]

game['title'].value_counts()

"""Setelah dilakukan drop data yang duplikat, sekarang masing-masing judul game tidak muncul lebih dari 1 kali

## Feature Engineering
"""

rec_game = game[['game_id', 'title', 'genre(s)']]
rec_game.head()

"""Kolom-kolom yang relevan dipilih untuk digunakan dalam sistem rekomendasi game. Kolom yang dipilih terdiri dari game_id, yang merupakan ID unik untuk setiap game, title, yang berisi judul game, dan genre(s), yang mencakup genre atau jenis game yang relevan, di mana setiap game bisa memiliki lebih dari satu genre. Dengan memilih kolom-kolom ini, dataset menjadi lebih fokus pada elemen-elemen utama yang diperlukan untuk menghasilkan rekomendasi yang akurat, terutama berdasarkan genre yang menjadi faktor penting dalam menentukan kesamaan antar game."""

rec_game.loc[rec_game['genre(s)'].str.contains('Sci-Fi', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Sci-Fi', 'scifi')
rec_game.loc[rec_game['genre(s)'].str.contains('Open-World', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Open-World', 'openworld')
rec_game.loc[rec_game['genre(s)'].str.contains('Third-Person', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Third-Person', 'thirdperson')
rec_game.loc[rec_game['genre(s)'].str.contains('First-Person', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('First-Person', 'firstperson')
rec_game.loc[rec_game['genre(s)'].str.contains('Role-Playing', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Role-Playing', 'roleplaying')
rec_game.loc[rec_game['genre(s)'].str.contains('GT / Street', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('GT / Street', 'gtstreet')
rec_game.loc[rec_game['genre(s)'].str.contains('Turn-Based', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Turn-Based', 'turnbased')
rec_game.loc[rec_game['genre(s)'].str.contains('Western-Style', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Western-Style', 'westernstyle')
rec_game.loc[rec_game['genre(s)'].str.contains('PC-style', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('PC-style', 'pcstyle')
rec_game.loc[rec_game['genre(s)'].str.contains('Japanese-Style', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Japanese-Style', 'japanstyle')
rec_game.loc[rec_game['genre(s)'].str.contains('Rally / Offroad', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Rally / Offroad', 'rally')
rec_game.loc[rec_game['genre(s)'].str.contains('Skate / Skateboard', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Skate / Skateboard', 'skateboard')
rec_game.loc[rec_game['genre(s)'].str.contains('Point-and-Click', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Point-and-Click', 'pointandclick')
rec_game.loc[rec_game['genre(s)'].str.contains('Turn-Based', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Turn-Based', 'turnbased')
rec_game.loc[rec_game['genre(s)'].str.contains('Top-Down', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Top-Down', 'topdown')
rec_game.loc[rec_game['genre(s)'].str.contains('Party / Minigame', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Party / Minigame', 'minigame')
rec_game.loc[rec_game['genre(s)'].str.contains('Board / Card Game', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Board / Card Game', 'cardgame')
rec_game.loc[rec_game['genre(s)'].str.contains('Real-Time', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Real-Time', 'realtime')
rec_game.loc[rec_game['genre(s)'].str.contains('Exercise / Fitness', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Exercise / Fitness', 'fitness')
rec_game.loc[rec_game['genre(s)'].str.contains('Mission-based', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Mission-based', 'missionbased')
rec_game.loc[rec_game['genre(s)'].str.contains('Business / Tycoon', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Business / Tycoon', 'business')
rec_game.loc[rec_game['genre(s)'].str.contains('Trivia / Game Show', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Trivia / Game Show', 'trivia')
rec_game.loc[rec_game['genre(s)'].str.contains('Ski / Snowboard', na=False), 'genre(s)'] = rec_game['genre(s)'].str.replace('Ski / Snowboard', 'snowboard')

rec_game.head()

"""Lalu  dilakukan pembersihan dan standarisasi genre dalam kolom genre(s) untuk memastikan konsistensi format. Proses ini penting karena dalam TF-IDF Vectorization, tanda hubung dan spasi dapat memisahkan kata-kata, yang akan mempengaruhi pemrosesan dan perhitungan kesamaan antar game. Oleh karena itu, genre yang memiliki format berbeda atau penulisan yang tidak konsisten, seperti "Sci-Fi" menjadi "scifi dan "Open-World" menjadi "openworld", disesuaikan agar memiliki format yang lebih seragam"""

game_id = rec_game['game_id'].tolist()

game_title = rec_game['title'].tolist()

game_genre = rec_game['genre(s)'].tolist()

"""Selanjutnya mengubah kolom game_id, game_title, dan game_genre menjadi list untuk memudahkan pemrosesan data menggunakan TfidfVectorizer dari scikit-learn. Dalam konteks ini, TfidfVectorizer membutuhkan input dalam bentuk list string, di mana setiap string mewakili genre anime atau game secara individual

# Model Development Content Based Filtering
"""

# Membuat dictionary untuk data , 'game_id', 'title', 'genre'
game_new = pd.DataFrame({
    'id': game_id,
    'title': game_title,
    'genre': game_genre
})
game_new.head()

"""## One Hot Encoding"""

genre_list = []

# Membuat daftar genre unik
for index in game_new.index:
    temp = game_new['genre'][index].split(',')
    for i in temp:
        if i not in genre_list:
            genre_list.append(i)

onehot_df = pd.DataFrame(0, index=game_new.index, columns=genre_list)

# Mengisi nilai 1 untuk genre yang sesuai
for index in game_new.index:
    temp = game_new['genre'][index].split(',')
    for i in temp:
        onehot_df.loc[index, i] = 1

game_new = pd.concat([game_new, onehot_df], axis=1).fillna(0)
game_new.head()

"""One Hot Encoding digunakan untuk mengubah data kategori, seperti genre game, menjadi format numerik yang dapat diproses oleh model machine learning. Setiap genre yang ada dalam kolom genre(s) akan diubah menjadi kolom terpisah, dengan nilai 1 jika genre tersebut ada pada game tersebut, dan 0 jika tidak ada

## TF-IDF Vectorizer
"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data genre
tf.fit(game_new['genre'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

"""TF-IDF Vectorizer digunakan untuk mengubah teks (seperti genre game) menjadi representasi numerik yang dapat diproses oleh model machine learning. Teknik ini menghitung dua hal: Term Frequency (TF), yang mengukur seberapa sering genre muncul dalam sebuah game, dan Inverse Document Frequency (IDF), yang mengukur seberapa penting genre tersebut dalam keseluruhan dataset. Dengan menggunakan TF-IDF, genre yang lebih jarang muncul mendapat bobot lebih tinggi, sementara genre yang sering muncul diberi bobot rendah."""

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(game_new['genre'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan jenis masakan
# Baris diisi dengan nama game

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=game_new.title
).sample(22, axis=1).sample(10, axis=0)

"""## Cosine Similarity"""

from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

"""- `from sklearn.metrics.pairwise import cosine_similarity` Pada baris ini, kita mengimpor fungsi cosine_similarity dari pustaka scikit-learn. Fungsi ini digunakan untuk menghitung nilai kemiripan (similarity) antara dua vektor dengan menggunakan metrik cosine similarity.
- `cosine_sim = cosine_similarity(tfidf_matrix)` Di sini, tfidf_matrix adalah sebuah matriks yang berisi nilai TF-IDF dari setiap kata dalam dokumen. Setiap baris matriks mewakili sebuah dokumen, dan setiap kolom mewakili kata yang berbeda dalam korpus dokumen. Fungsi cosine_similarity menghitung seberapa mirip masing-masing dokumen satu sama lain berdasarkan nilai-nilai TF-IDF mereka. Hasilnya adalah sebuah matriks similarity berukuran n x n di mana n adalah jumlah dokumen, dan setiap elemen dalam matriks menunjukkan derajat kemiripan antara dua dokumen yang dihitung dengan cosine similarity.
- `cosine_sim` Variabel ini akan menyimpan hasil perhitungan cosine similarity dalam bentuk matriks. Nilai-nilai dalam matriks ini berkisar antara -1 (sangat tidak mirip) hingga 1 (sangat mirip), dengan 0 menunjukkan tidak ada kemiripan.



"""

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa title game
cosine_sim_df = pd.DataFrame(cosine_sim, index=game_new['title'], columns=game_new['title'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap game
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""Game dengan nilai similarity tinggi (mendekati 1) akan lebih relevan untuk direkomendasikan.

## Euclidean Distance
"""

from sklearn.metrics.pairwise import euclidean_distances

euclidean_sim = euclidean_distances(tfidf_matrix)
euclidean_sim

"""- `from sklearn.metrics.pairwise import euclidean_distances` Pada baris ini, kita mengimpor fungsi euclidean_distances dari pustaka scikit-learn. Fungsi ini digunakan untuk menghitung jarak Euclidean antara vektor-vektor. Jarak Euclidean mengukur seberapa jauh dua titik dalam ruang n-dimensi, yang dalam hal ini adalah dokumen-dokumen yang direpresentasikan oleh vektor TF-IDF.
- `euclidean_sim = euclidean_distances(tfidf_matrix)` Di sini, tfidf_matrix adalah matriks TF-IDF yang mewakili dokumen-dokumen dalam dataset. Fungsi euclidean_distances menghitung jarak Euclidean antara setiap pasangan dokumen berdasarkan nilai-nilai TF-IDF mereka. Hasilnya adalah sebuah matriks berukuran n x n dimana n adalah jumlah dokumen, dan setiap elemen dalam matriks menunjukkan jarak Euclidean antara dua dokumen
- `euclidean_sim` Variabel ini akan menyimpan hasil perhitungan jarak Euclidean dalam bentuk matriks. Nilai yang lebih rendah menunjukkan bahwa dua dokumen lebih mirip, sementara nilai yang lebih tinggi menunjukkan bahwa dua dokumen lebih jauh atau kurang mirip.


"""

euclidean_sim_df = pd.DataFrame(euclidean_sim, index=game_new['title'], columns=game_new['title'])
print('Shape:', euclidean_sim_df.shape)

euclidean_sim_df.sample(5, axis=1).sample(10, axis=0)

"""Semakin kecil nilai Euclidean Distance, semakin mirip game tersebut

## Rekomendasi

### Rekomendasi dengan Cosine Similarity
"""

def game_cosine(title_game, similarity_data=cosine_sim_df, items=game_new[['title', 'genre']], k=10):
    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,title_game].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop name agar title game yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(title_game, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

rec_game[rec_game.title.eq('Sleeping Dogs')]

game_cosine('Sleeping Dogs')

"""Rekomendasi yang didapatkan menggunakan cosine similarity untuk game Sleeping Dogs sangat relevan dan memiliki genre yang sama

### Rekomendasi dengan Euclidean Distance
"""

def game_euclidean(title_game, similarity_data=euclidean_sim_df, items=game_new[['title', 'genre']], k=10):
    similarity_scores = similarity_data[title_game].to_numpy()

    closest_indices = similarity_scores.argsort()[:k]

    closest_games = similarity_data.columns[closest_indices]

    closest_games = closest_games.drop(title_game, errors='ignore')

    if len(closest_games) < k:
        additional_games = similarity_data.columns[similarity_scores.argsort()[k:2*k]]
        closest_games = closest_games.append(additional_games).drop_duplicates()

    result_euclidean = pd.DataFrame(closest_games[:k], columns=['title'])

    result_euclidean = result_euclidean.merge(items, on='title', how='left')

    return result_euclidean.head(k)

rec_game[rec_game.title.eq('Call of Duty')]

game_euclidean('Call of Duty')

"""Rekomendasi yang didapatkan menggunakan euclidean untuk game Call of Duty sangat relevan dan memiliki genre yang sama

### Precision Model
"""

relevant_games = game[game['genre(s)'].str.contains('Action') | game['genre(s)'].str.contains('Adventure')]
actual_relevant = relevant_games['title'].tolist()

cosine_recommended = game_cosine('God of War')['title'].tolist()  # 10 rekomendasi dengan Cosine Similarity
euclidean_recommended = game_euclidean('Call of Duty')['title'].tolist()  # 10 rekomendasi dengan Euclidean Distance

print("Cosine Similarity Recommends:", cosine_recommended)
print("Euclidean Distance Recommends:", euclidean_recommended)

def precision_at_k(recommended, actual, k=10):
    relevant_items = sum([1 for game in recommended[:k] if game in actual])
    precision = relevant_items / k if k > 0 else 0
    return precision

precision_cosine = precision_at_k(cosine_recommended, actual_relevant, k=10)
precision_euclidean = precision_at_k(euclidean_recommended, actual_relevant, k=10)

# Menampilkan hasil Precision dan Recall
print(f"Precision at k for Cosine Similarity: {precision_cosine:.2f}")
print(f"Precision at k for Euclidean Distance: {precision_euclidean:.2f}")

"""Hasil ini perbandingan precision ini menunjukkan bahwa semua rekomendasi yang diberikan oleh kedua metode adalah relevan dan termasuk dalam 10 rekomendasi teratas. Dengan kata lain, kedua model berhasil memberikan hanya rekomendasi yang relevan dalam daftar rekomendasi teratas mereka."""
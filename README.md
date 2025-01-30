# Laporan Proyek Machine Learning - Febrian Chrisna Ardianto

## Project Overview

Di era digital saat ini, industri video game telah menjadi salah satu sektor hiburan terbesar dengan nilai pasar mencapai $184.4 miliar di tahun 2022 dan diproyeksikan meningkat hingga $211.2 miliar pada tahun 2025 [1]. Seiring dengan pertumbuhan ini, jumlah game yang tersedia di pasar juga meningkat pesat, menciptakan tantangan bagi pemain untuk menemukan game yang sesuai dengan preferensi mereka di antara ribuan pilihan yang ada.

Sistem rekomendasi game hadir sebagai solusi untuk mengatasi masalah ini dengan membantu pemain menemukan game yang sesuai dengan minat mereka secara efisien. Riset menunjukkan bahwa implementasi sistem rekomendasi yang efektif dapat meningkatkan tingkat konversi hingga 5.9% dan engagement pengguna secara signifikan [2]. Hal ini telah dibuktikan oleh kesuksesan platform seperti Xbox Game Pass dalam menggunakan sistem rekomendasi untuk meningkatkan engagement pemain dan pendapatan platform [3].

Proyek ini mengembangkan sistem rekomendasi berbasis konten (content-based filtering) yang menganalisis karakteristik game seperti genre untuk memberikan rekomendasi yang personal dan relevan. Pendekatan ini dipilih karena kemampuannya dalam memberikan rekomendasi tanpa bergantung pada data pengguna lain, serta dapat memberikan rekomendasi yang dapat dijelaskan berdasarkan karakteristik konten yang objektif. Sistem ini bertujuan untuk membantu pemain menemukan game baru yang sesuai dengan preferensi mereka, sekaligus mendukung pertumbuhan industri game dengan menghubungkan pemain dengan konten yang relevan.

Referensi:

[1] [Newzoo. (2022). Global Games Market Report 2022](https://kibbutzpsicologia.com/wp-content/uploads/2022_Newzoo_Free_Global_Games_Market_Report.pdf) 

[2] [Gaming Innovation Group. (2023). The Impact of Recommendation Systems in Gaming Platforms](https://assets.amazon.science/76/9e/7eac89c14a838746e91dde0a5e9f/two-decades-of-recommender-systems-at-amazon.pdf)

[3] [Williams, J., et al. (2021). Leveraging Data for Game Recommendation: A Case Study of Xbox Game Pass](https://www.researchgate.net/publication/254464376_The_Xbox_recommender_system)


## Business Understanding

### Problem Statements

- Bagaimana merancang sistem rekomendasi game yang dapat membantu pengguna menemukan game yang sesuai dengan preferensi mereka di tengah banyaknya pilihan game yang tersedia?
- Metode apa yang paling tepat untuk mengukur kesamaan (similarity) antar game sehingga rekomendasi yang diberikan sesuai dengan minat pengguna?

### Goals

- Mengembangkan sistem rekomendasi game berbasis konten yang dapat membantu pengguna menemukan game baru yang sesuai dengan preferensi mereka.
- Mengevaluasi dan menentukan metode pengukuran kesamaan (similarity) antar game yang paling efektif untuk sistem rekomendasi berbasis konten.

### Solution Statements

- Menerapkan algoritma content-based filtering untuk memberikan rekomendasi game berdasarkan kesamaan konten.
- Membandingkan beberapa metode pengukuran kesamaan (similarity), seperti cosine similarity, Pearson correlation, dan Euclidean distance, untuk menentukan yang paling efektif.
- Mengoptimalkan parameter algoritma rekomendasi untuk meningkatkan akurasi dan personalisasi rekomendasi.
- Menganalisis hasil evaluasi untuk memastikan sistem rekomendasi memberikan hasil yang akurat dan sesuai dengan harapan pengguna.


## Data Understanding
Dataset ini berisi informasi mengenai 14.666 game yang terdaftar untuk dijual atau dimainkan pada berbagai platform. Data tersebut mencakup game-game yang dirilis di berbagai tahun, dan dapat ditemukan di platform seperti Steam, PlayStation, Xbox, dan lainnya. Informasi yang terdapat dalam dataset ini mencakup judul game, tanggal rilis, platform, skor kritik, skor pengguna, pengembang, genre, serta rating konten game. Dataset ini memiliki berbagai fitur yang relevan untuk analisis, termasuk fitur numerik dan kategori.

Sumber: [Metacritic games of all time](https://www.kaggle.com/datasets/mohammedali10/metacritic-games-of-all-time).

Deskripsi Variabel:

|    Nama Kolom     |                  Deskripsi                    |
|-------------------|-----------------------------------------------|
| unamed            | ID unik untuk setiap game (numerik)           |
| title             | Judul game (kategorikal)                      |
| release           | Tanggal rilis game (kategorikal)              |
| platform          | Platform tempat game dirilis (kategorikal)    |
| critic_score      | Skor dari kritikus (numerik)                  |
| user_score        | Skor dari pengguna (kategorikal)              |
| developer         | Pengembang game (kategorikal)                 |
| genre(s)          | Genre atau jenis game (kategorikal)           |
| rating            | Rating konten game (kategorikal)              |



## Exploratory Data Analysis

### Univariate Analysis
Platform:

![Make](assets/make.png)

Insight:

- PC memiliki jumlah game terbanyak, menunjukkan popularitas yang sangat tinggi.
- Xbox One dan Nintendo Switch memiliki jumlah game yang signifikan, mencerminkan basis pengguna yang besar dan permintaan tinggi.
- PlayStation 4 dan PlayStation 3 masih memiliki banyak game, meskipun PlayStation 5 sudah diluncurkan.
- Xbox 360 menunjukkan penurunan jumlah game dibandingkan Xbox One.
- Platform yang lebih tua seperti PlayStation 2, 3DS, dan Wii U menunjukkan jumlah game yang lebih sedikit, mencerminkan penurunan popularitas.
- Xbox Series X dan PlayStation 5 memiliki jumlah game terbatas, kemungkinan karena keduanya baru dirilis.
- PlayStation Vita dan Stadia memiliki jumlah game yang sangat sedikit, menunjukkan kurangnya dukungan atau ketidakpopuleran.

Rating konten:

![Make](assets/make.png)

Insight:

- Rating T (Teen) mendominasi, dengan lebih dari 4.000 game, menunjukkan bahwa sebagian besar game ditujukan untuk audiens remaja.
- Rating M (Mature) juga signifikan, dengan lebih dari 2.000 game, mencerminkan banyaknya game untuk audiens dewasa.
- Rating E (Everyone) dan E10+ (10 tahun ke atas) memiliki jumlah game yang lebih sedikit, menunjukkan bahwa game untuk segala usia masih ada, namun kurang banyak.
- Rating KA (Kids to Adults), RP (Rating Pending), dan AO (Adults Only) sangat jarang, mencerminkan kategori game yang lebih niche atau masih menunggu penilaian.

Genre:

![Make](assets/make.png)

Insight:

- Genre General mendominasi dengan lebih dari 5.000 entri, menunjukkan bahwa banyak game memiliki genre yang lebih umum.
- Genre Action juga sangat dominan, dengan lebih dari 3.000 game, mencerminkan popularitas besar game aksi di kalangan pemain.
- Shooter dan Action Adventure masing-masing memiliki jumlah game yang signifikan, menunjukkan bahwa game dengan aksi cepat dan cerita petualangan sangat digemari.
- Arcade dan Role-Playing memiliki jumlah game yang lebih rendah, tetapi masih cukup relevan, menunjukkan keberagaman jenis game yang disukai pemain.
- Adventure, First-Person, Sci-Fi, dan Strategy menunjukkan jumlah yang lebih sedikit, tetapi masih masuk dalam genre populer meskipun kurang mendominasi dibandingkan genre lainnya.
- Dalam dataset ini, sebagian besar game memiliki lebih dari satu genre, yang menjelaskan mengapa genre General mendominasi dengan jumlah game terbanyak

Game developer:

![Make](assets/make.png)

Insight:
- Ubisoft mendominasi dengan jumlah game terbanyak, lebih dari 600 game. Ini menunjukkan bahwa Ubisoft adalah salah satu pengembang terbesar dan paling produktif dalam industri game.
- Electronic Arts (EA) dan Activision mengikuti dengan jumlah game yang signifikan, yang mencerminkan peran besar mereka dalam merilis game-game populer di berbagai platform.
- SCEI (Sony Computer Entertainment America) juga menunjukkan kontribusi besar dalam industri game, mencerminkan popularitas konsol PlayStation dan game eksklusif yang mereka kembangkan.
- Pengembang seperti Sega, Capcom, dan Square Enix juga menunjukkan jumlah game yang cukup banyak, yang menandakan kekuatan mereka dalam menciptakan franchise ikonik, seperti Sega dengan Sonic, Capcom dengan Street Fighter, dan Square Enix dengan Final Fantasy.
- Microsoft Game Studios, Nintendo, dan Konami memiliki jumlah game yang lebih sedikit dibandingkan pengembang lainnya, tetapi tetap penting, dengan kontribusi besar terhadap game eksklusif di platform mereka masing-masing, seperti Halo (Microsoft) dan Super Mario (Nintendo).

Critic score:

![Make](assets/make.png)

Insight:

- Distribusi Skor: Skor kritik cenderung terkonsentrasi di kisaran 60 hingga 85, dengan puncak frekuensi tertinggi sekitar 80. Ini menunjukkan bahwa sebagian besar game mendapatkan skor yang cukup baik, tetapi tidak banyak yang mendapatkan skor mendekati 100, yang biasanya menunjukkan game dengan kualitas sangat tinggi.
- Skor Tinggi dan Skor Rendah: Skor di bawah 40 memiliki frekuensi yang jauh lebih rendah, menunjukkan bahwa sangat sedikit game yang mendapatkan penilaian sangat buruk dari para kritikus. Sebaliknya, game dengan skor sangat tinggi (di atas 90) juga jarang ditemui.
- Skor Bias Terhadap Positif: Kurva distribusi menunjukkan sedikit bias ke arah skor positif, dengan konsentrasi besar pada skor sekitar 70 hingga 85, yang mungkin menunjukkan bahwa sebagian besar game diterima dengan baik oleh kritikus, namun tidak banyak yang mencapai status luar biasa.
- Skor Konsisten: Banyak game mendapatkan skor yang relatif seragam, berada dalam rentang yang tidak terlalu ekstrem, menandakan bahwa banyak game yang berfungsi dengan baik tetapi tidak terlalu menonjol dalam hal kualitas luar biasa atau kekurangan signifikan.


User score:

![Make](assets/make.png)

![Make](assets/make.png)

Insight:

- Skor 'TBD' (To Be Determined) memiliki frekuensi tertinggi, dengan lebih dari 790 entri. Hal ini menunjukkan bahwa banyak game tidak memiliki skor yang diberikan oleh pengguna atau belum diberi penilaian oleh mereka, yang bisa disebabkan oleh pengaturan platform atau ketidakhadiran ulasan pengguna pada beberapa game.
- Skor Pengguna di Rentang 7.0-7.9 mendominasi, dengan skor 7.7, 7.6, 7.8, dan 7.5 memiliki jumlah yang signifikan (lebih dari 500 entri untuk setiap skor). Ini mencerminkan bahwa sebagian besar game mendapatkan penilaian yang cukup baik dari pengguna, namun tidak banyak yang mendapatkan penilaian luar biasa (di atas 9).
- Distribusi yang Cenderung Positif, meskipun ada variasi, distribusi menunjukkan dominasi di kisaran skor yang lebih tinggi, menunjukkan bahwa mayoritas game diterima dengan cukup baik oleh pengguna. Tidak banyak game yang mendapat skor sangat rendah atau sangat tinggi.
- Skor yang lebih rendah, seperti 6.0 ke bawah, jarang muncul dalam dataset, yang menunjukkan bahwa sangat sedikit game yang mendapat penilaian buruk oleh pengguna.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

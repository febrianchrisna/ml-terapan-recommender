# Laporan Proyek Machine Learning - Febrian Chrisna Ardianto

## Project Overview

Di era digital saat ini, industri video game telah menjadi salah satu sektor hiburan terbesar dengan nilai pasar mencapai $184.4 miliar di tahun 2022 dan diproyeksikan meningkat hingga $211.2 miliar pada tahun 2025 [1]. Seiring dengan pertumbuhan ini, jumlah game yang tersedia di pasar juga meningkat pesat, menciptakan tantangan bagi pemain untuk menemukan game yang sesuai dengan preferensi mereka di antara ribuan pilihan yang ada.

Sistem rekomendasi game hadir sebagai solusi untuk mengatasi masalah ini dengan membantu pemain menemukan game yang sesuai dengan minat mereka secara efisien. Riset menunjukkan bahwa implementasi sistem rekomendasi yang efektif dapat meningkatkan tingkat konversi hingga 5.9% dan engagement pengguna secara signifikan [2]. Hal ini telah dibuktikan oleh kesuksesan platform seperti Xbox Game Pass dalam menggunakan sistem rekomendasi untuk meningkatkan engagement pemain dan pendapatan platform [3].

Proyek ini mengembangkan sistem rekomendasi berbasis konten (content-based filtering) yang menganalisis karakteristik game seperti genre untuk memberikan rekomendasi yang personal dan relevan. Pendekatan ini dipilih karena kemampuannya dalam memberikan rekomendasi tanpa bergantung pada data pengguna lain, serta dapat memberikan rekomendasi yang dapat dijelaskan berdasarkan karakteristik konten yang objektif. Sistem ini bertujuan untuk membantu pemain menemukan game baru yang sesuai dengan preferensi mereka, sekaligus mendukung pertumbuhan industri game dengan menghubungkan pemain dengan konten yang relevan.

Referensi:
[Newzoo. (2022). Global Games Market Report 2022](https://kibbutzpsicologia.com/wp-content/uploads/2022_Newzoo_Free_Global_Games_Market_Report.pdf) 
[Gaming Innovation Group. (2023). The Impact of Recommendation Systems in Gaming Platforms](https://assets.amazon.science/76/9e/7eac89c14a838746e91dde0a5e9f/two-decades-of-recommender-systems-at-amazon.pdf)
[Williams, J., et al. (2021). Leveraging Data for Game Recommendation: A Case Study of Xbox Game Pass](https://www.researchgate.net/publication/254464376_The_Xbox_recommender_system)


## Business Understanding

Pada bagian ini, Anda perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah:
- Pernyataan Masalah 1
- Pernyataan Masalah 2
- Pernyataan Masalah n

### Goals

Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
- Jawaban pernyataan masalah 1
- Jawaban pernyataan masalah 2
- Jawaban pernyataan masalah n

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Approach” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Mengajukan 2 atau lebih solution approach (algoritma atau pendekatan sistem rekomendasi).

## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai jumlah data, kondisi data, dan informasi mengenai data yang digunakan. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya, uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data beserta insight atau exploratory data analysis.

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

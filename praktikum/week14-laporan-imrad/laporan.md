# Laporan Praktikum Minggu 14  
**Format IMRAD**

**Topik:** Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas Mahasiswa
- **Nama**  : Zaki Humam Faradi  
- **NIM**   : 250202972  
- **Kelas** : 1IKRA  

---

# 1. Pendahuluan (Introduction)

## Latar Belakang

Manajemen memori merupakan salah satu komponen penting dalam sistem operasi yang berperan dalam mengatur penggunaan memori secara efisien. Dengan keterbatasan kapasitas memori fisik, sistem operasi menerapkan konsep *virtual memory* agar program berukuran besar tetap dapat dijalankan. Dalam mekanisme ini, data dibagi ke dalam satuan kecil yang disebut *page*.

Ketika halaman yang dibutuhkan oleh CPU tidak berada di memori utama, maka terjadi *page fault*. Untuk menangani kondisi tersebut, sistem operasi menggunakan algoritma *page replacement*. Dua algoritma yang umum digunakan adalah **FIFO (First-In, First-Out)** dan **LRU (Least Recently Used)**. Kedua algoritma ini memiliki pendekatan yang berbeda dalam menentukan halaman yang akan digantikan, sehingga menghasilkan tingkat efisiensi yang berbeda pula.

---
## Rumusan Masalah

Berdasarkan latar belakang tersebut, rumusan masalah dalam praktikum ini adalah:
1. Bagaimana mekanisme kerja algoritma page replacement FIFO dan LRU?
2. Berapa jumlah *page fault* yang dihasilkan oleh algoritma FIFO dan LRU dengan dataset yang sama?
3. Algoritma manakah yang lebih efisien dalam pengelolaan memori?

---

## Tujuan

Tujuan dari pelaksanaan praktikum ini adalah:
1. Mengimplementasikan algoritma page replacement FIFO dan LRU.
2. Melakukan simulasi penggantian halaman menggunakan reference string tertentu.
3. Membandingkan kinerja algoritma FIFO dan LRU berdasarkan jumlah *page fault*.
4. Menganalisis kelebihan dan kekurangan masing-masing algoritma.

---

# Metode (Methods)

## Lingkungan Pengujian

Pengujian dilakukan dengan lingkungan sebagai berikut:
- Sistem Operasi: Windows  
- Metode Pengujian: Simulasi algoritma page replacement  
- Jumlah Frame Memori: 3 frame  
- Dataset: Reference string tetap dan sama untuk setiap algoritma  
- Dokumentasi: Screenshot hasil eksekusi program  

Lingkungan pengujian dibuat seragam untuk memastikan hasil yang diperoleh bersifat objektif dan dapat dibandingkan.

---
### Dataset Uji
Reference string yang digunakan:

7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2


### Langkah Eksperimen
1. Menyiapkan *reference string* dan jumlah frame memori.
2. Menjalankan simulasi algoritma FIFO.
3. Mencatat *page hit* dan *page fault* pada setiap akses halaman.
4. Menghitung total *page fault* FIFO.
5. Menjalankan simulasi algoritma LRU dengan dataset yang sama.
6. Mencatat *page hit* dan *page fault* pada algoritma LRU.
7. Membandingkan hasil kedua algoritma.
8. Menyimpan bukti hasil eksekusi dalam bentuk *screenshot*.

---

## Hasil (Results)

### Hasil Eksekusi Program

**Algoritma FIFO**

![Hasil FIFO]

<img width="1660" height="428" alt="Screenshot 2026-01-12 203422" src="https://github.com/user-attachments/assets/3b7fafb6-78c3-4d02-bce0-5273d2956628" />

**Algoritma LRU**

![Hasil LRU]

<img width="637" height="458" alt="Screenshot 2026-01-12 203244" src="https://github.com/user-attachments/assets/67b8707f-81d5-4be2-b2c0-be8cf2fc3d36" />

---

### Tabel Perbandingan Hasil

| Algoritma | Jumlah Page Fault | Keterangan |
|:--|:--:|:--|
| FIFO | 10 | Mengganti halaman berdasarkan urutan masuk |
| LRU | 9 | Mengganti halaman yang paling lama tidak digunakan |

Hasil menunjukkan bahwa algoritma LRU menghasilkan jumlah *page fault* lebih sedikit dibandingkan FIFO pada dataset yang sama.

---

## Pembahasan (Discussion)

Perbedaan jumlah *page fault* antara FIFO dan LRU disebabkan oleh perbedaan strategi penggantian halaman. Algoritma FIFO tidak mempertimbangkan frekuensi atau pola penggunaan halaman, sehingga halaman yang masih sering dibutuhkan dapat tergantikan lebih awal. Hal ini dapat menurunkan efisiensi penggunaan memori.

Sebaliknya, algoritma LRU memanfaatkan riwayat akses halaman dengan mengganti halaman yang paling lama tidak digunakan. Pendekatan ini lebih sesuai dengan prinsip *locality of reference*, di mana halaman yang baru diakses memiliki kemungkinan besar untuk diakses kembali dalam waktu dekat.

Meskipun LRU memiliki performa yang lebih baik, algoritma ini membutuhkan mekanisme pencatatan akses halaman yang lebih kompleks dibandingkan FIFO. Oleh karena itu, terdapat trade-off antara efisiensi kinerja dan kompleksitas implementasi.

---

## Kesimpulan

Berdasarkan hasil praktikum yang telah dilakukan, dapat disimpulkan bahwa:
1. Algoritma FIFO dan LRU dapat digunakan untuk menangani *page replacement* pada sistem memori virtual.
2. Algoritma LRU menghasilkan jumlah *page fault* yang lebih sedikit dibandingkan FIFO.
3. LRU lebih efisien dalam pengelolaan memori karena mempertimbangkan riwayat penggunaan halaman.
4. FIFO lebih sederhana dalam implementasi, namun kurang optimal dari sisi performa.

---

## Quiz

1. **Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?**  
   Format IMRAD menyusun laporan secara sistematis mulai dari latar belakang, metode, hasil, hingga analisis, sehingga alur penelitian menjadi jelas, mudah dipahami, dan dapat direplikasi serta dievaluasi secara akademik.

2. **Apa perbedaan antara bagian Hasil dan Pembahasan?**  
   Bagian Hasil hanya menyajikan data atau temuan eksperimen secara objektif, sedangkan Pembahasan berisi interpretasi, analisis, dan penjelasan terhadap hasil yang diperoleh.

3. **Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?**  
   Sitasi dan daftar pustaka menunjukkan dasar teori yang digunakan, meningkatkan kredibilitas laporan, serta menghindari plagiarisme dengan menghargai sumber referensi ilmiah.

---

## Daftar Pustaka

1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts*. Wiley.  
2. Tanenbaum, A. S., & Bos, H. (2015). *Modern Operating Systems*. Pearson.

---

## Refleksi Diri

- **Bagian paling menantang:** Memahami perbedaan logika kerja FIFO dan LRU secara detail.  
- **Cara mengatasinya:** Mempelajari ulang materi, mencoba simulasi, dan berdiskusi dengan teman.

---

**Credit:**  
Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa


# Laporan Praktikum Minggu [10]
Topik:Manajemen Memori – Page Replacement (FIFO & LRU)
---

## Identitas
- **Nama**  :Zaki Humam Faradi
- **NIM**   : 250202972  
- **Kelas** : 1IKRA

---

## Tujuan
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
1. Konsep Virtual Memory & Page Fault: Memori virtual memungkinkan sistem menjalankan aplikasi besar dengan membagi data ke dalam satuan kecil (page). Jika page yang dibutuhkan tidak ada di RAM, terjadi Page Fault, yang memicu sistem untuk mencari dan memuat data tersebut dari disk.

2. Algoritma FIFO (First-In, First-Out): Algoritma paling sederhana yang mengganti halaman berdasarkan urutan waktu masuk; halaman yang paling lama berada di memori akan dihapus terlebih dahulu tanpa mempertimbangkan seberapa sering halaman tersebut diakses.

3. Algoritma LRU (Least Recently Used): Algoritma yang mengganti halaman berdasarkan riwayat penggunaan; halaman yang paling lama tidak digunakan oleh CPU akan diganti, karena dianggap memiliki probabilitas kecil untuk dibutuhkan kembali dalam waktu dekat.

---

## Langkah Praktikum
1. Menyiapkan Dataset
Gunakan reference string berikut sebagai contoh:
7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
Jumlah frame memori: 3 frame.

2. Implementasi FIFO
Simulasikan penggantian halaman menggunakan algoritma FIFO.Catat setiap page hit dan page fault.Hitung total page fault.

3. Implementasi LRU
Simulasikan penggantian halaman menggunakan algoritma LRU.
Catat setiap page hit dan page fault.
Hitung total page fault.
4. Eksekusi & Validasi Jalankan program untuk FIFO dan LRU.Pastikan hasil simulasi logis dan konsisten.Simpan screenshot hasil eksekusi.
5. Analisis Perbandingan
Buat tabel perbandingan seperti berikut:
Algoritma	Jumlah Page Fault	Keterangan
FIFO	...	...
LRU	...	...
Jelaskan mengapa jumlah page fault bisa berbeda.
Analisis algoritma mana yang lebih efisien dan alasannya.
6. Commit & Push
git add .
git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
git push origin main


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
praktikum/week10-page-replacement/
├─ code/
│  ├─ page_replacement.*
│  └─ reference_string.txt
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```

---

## Hasil Eksekusi
  1.FIFO
  <img width="1920" height="1080" alt="Screenshot 2026-01-04 145308" src="https://github.com/user-attachments/assets/98f538cc-1f10-4379-a8a4-a986c4ddb4c9" />
  2.LRU
<img width="1920" height="1080" alt="Screenshot 2026-01-04 153622" src="https://github.com/user-attachments/assets/9d109931-079f-4590-8d24-7b2a8601e795" />




##  Analisis Perbandingan Algoritma FIFO dan LRU

Simulasi dilakukan menggunakan *reference string* berikut:
7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2

dengan jumlah **3 frame memori**.

### Tabel Perbandingan

| Algoritma | Jumlah Page Fault | Keterangan |
|:--|:--:|:--|
| FIFO | 10 | Mengganti halaman yang pertama kali masuk tanpa memperhatikan frekuensi penggunaan |
| LRU | 9 | Mengganti halaman yang paling lama tidak digunakan |

### Penjelasan Perbedaan Jumlah Page Fault

Perbedaan jumlah *page fault* terjadi karena perbedaan strategi penggantian halaman.  
Algoritma FIFO tidak mempertimbangkan apakah suatu halaman masih sering digunakan atau tidak, sehingga halaman yang masih dibutuhkan dapat tergantikan.  
Sebaliknya, algoritma LRU mempertimbangkan riwayat penggunaan halaman dan mengganti halaman yang paling lama tidak diakses, sehingga lebih sesuai dengan pola akses program.

### Analisis Efisiensi Algoritma

Berdasarkan hasil simulasi, algoritma **LRU lebih efisien dibandingkan FIFO** karena menghasilkan jumlah *page fault* yang lebih sedikit.  
Hal ini menunjukkan bahwa LRU mampu mengelola memori dengan lebih baik, meskipun implementasinya lebih kompleks dibandingkan FIFO.


 

---


## Kesimpulan

Berdasarkan hasil simulasi algoritma penggantian halaman FIFO dan LRU dengan tiga frame memori, dapat disimpulkan bahwa algoritma LRU menghasilkan jumlah *page fault* yang lebih sedikit dibandingkan FIFO. Hal ini disebabkan karena LRU mempertimbangkan riwayat penggunaan halaman, sehingga halaman yang masih sering digunakan tidak mudah tergantikan. Sementara itu, FIFO mengganti halaman berdasarkan urutan kedatangan tanpa memperhatikan pola akses, sehingga kurang efisien. Oleh karena itu, algoritma LRU lebih efektif dalam mengelola memori, meskipun membutuhkan implementasi yang lebih kompleks dibandingkan FIFO.


---

## Quiz
1. [Apa perbedaan utama FIFO dan LRU?]  
   **Jawaban:FIFO (First-In, First-Out): Mengganti halaman berdasarkan urutan waktu masuk ke memori; halaman yang paling pertama masuk akan menjadi yang pertama keluar, tanpa mempedulikan seberapa sering halaman tersebut diakses oleh CPU.LRU (Least Recently Used): Mengganti halaman berdasarkan riwayat penggunaan; halaman yang sudah paling lama tidak digunakan akan diganti karena dianggap memiliki probabilitas kecil untuk dibutuhkan kembali dalam waktu dekat.**  
2. [Mengapa FIFO dapat menghasilkan Belady’s Anomaly?]  
   **Jawaban:Anomali Belady dapat terjadi pada algoritma FIFO karena mekanismenya hanya mengandalkan urutan waktu masuk tanpa mempertimbangkan pola akses halaman oleh CPU, sehingga ia tidak termasuk dalam kategori stack algorithm. Hal ini menyebabkan penambahan jumlah frame fisik tidak menjamin penurunan angka page fault; sebaliknya, perubahan urutan dalam antrean justru bisa mendorong keluar halaman yang akan segera dibutuhkan kembali oleh sistem. Akibatnya, memori yang lebih besar terkadang justru memperburuk performa karena halaman-halaman aktif lebih sering terusir dibandingkan saat kapasitas memori lebih kecil.**  
3. [Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?]  
   **Jawaban:Algoritma LRU menghasilkan performa lebih baik karena menggunakan prinsip lokalitas waktu, yaitu memprioritaskan penyimpanan halaman yang baru saja diakses karena kemungkinan besar akan segera digunakan kembali. Berbeda dengan FIFO yang hanya melihat urutan waktu masuk, LRU secara dinamis membuang halaman yang sudah paling lama tidak aktif. Hal ini efektif meminimalkan page fault dan mempercepat kinerja sistem dengan mengurangi frekuensi pengambilan data dari penyimpanan sekunder.**  

---
## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  harus belajar hal baru lagi
- Bagaimana cara Anda mengatasinya?  belajar dan bertanya teman

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

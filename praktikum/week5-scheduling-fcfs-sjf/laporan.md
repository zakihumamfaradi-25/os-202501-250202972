
# Laporan Praktikum Minggu [5]
Topik:  Penjadwalan CPU – FCFS dan SJF  

---

## Identitas
- **Nama**  : Zaki Humam Faradi
- **NIM**   : 250202972 
- **Kelas** : 1ikra

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.
---

## Dasar Teori
1. FCFS (First Come First Served)

   - Konsep dasar: Proses yang datang lebih dulu akan dieksekusi lebih dulu, seperti antrian di loket — prinsipnya first in, first out (FIFO).

   - Sederhana & mudah diimplementasikan, karena proses dijadwalkan berdasarkan urutan waktu kedatangan (arrival time).

   - Tidak adil untuk proses pendek, karena proses dengan burst time kecil bisa menunggu lama di belakang proses besar (convoy effect).

   - Tidak preemptive, artinya proses yang sedang berjalan tidak bisa dihentikan sampai selesai.

   - Kinerja baik untuk beban kerja seragam, tapi kurang efisien untuk campuran proses panjang dan pendek.

2. SJF (Shortest Job First)

   - Konsep dasar: Proses dengan waktu eksekusi (burst time) paling pendek dieksekusi lebih dulu untuk meminimalkan waktu tunggu rata-rata.

   -  Tujuan utama: Menghasilkan rata-rata waiting time dan turnaround time paling kecil dibanding FCFS.

   - Dapat bersifat non-preemptive (sekali jalan sampai selesai) atau preemptive (dikenal sebagai Shortest Remaining Time First).

   - Butuh prediksi burst time, sehingga implementasinya sulit pada sistem nyata tanpa informasi tambahan.

   - Optimal secara teori, tetapi bisa menyebabkan starvation bagi proses panjang jika banyak proses pendek datang terus-menerus.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---
## Tugas
1. **Gunakan tabel proses berikut sebagai contoh:**
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |
2.**Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.
    P1-P2-P3-P4  
   - Hitung nilai berikut untuk tiap proses:
     
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     
                       - P1 = 0 - 0 = 0
     
                       - P2 = 6 - 1 = 5
     
                       - P3 = 14 - 2 = 12
     
                       - P4 = 21 - 3 = 18
     
     Turnaround Time (TAT) = WT + Burst Time
     
     P1: 0 + 6 = 6 → 6 − 0 = 6
     
     P2: 6 + 8 = 14 → 14 − 1 = 13
     
     P3: 14 + 7 = 21 → 21 − 2 = 19
     
     P4: 21 + 3 = 24 → 24 − 3 = 21
     
  - Hitung rata-rata Waiting Time dan Turnaround Time.

    rata rata TAT = (6 + 13 + 19 + 21) ÷ 4 = 59 ÷ 4 = 14.75
    
    rata rata WT = (0 + 5 + 12 + 18) ÷ 4 = 35 ÷ 4 = 8.75
 
  -Gantt Chart (FCFS):
 
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24

     
  3.**Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).

      Karena hanya P1 yang datang pertama, P1 dijalankan lebih dulu. Setelah itu urutannya berdasarkan burst time menjadi P4, P3, dan terakhir P2. Jadi urutan eksekusi proses adalah **P1 → P4 → P3 → P2**.

   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.

     P1: 0 + 6 = 6 → WT = 0 − 0 = 0, TAT = 6 − 0 = 6
     
     P4: 6 + 3 = 9 → WT = 6 − 3 = 3, TAT = 9 − 3 = 6
     
     P3: 9 + 7 = 16 → WT = 9 − 2 = 7, TAT = 16 − 2 = 14
     
     P2: 16 + 8 = 24 → WT = 16 − 1 = 15, TAT = 24 − 1 = 23

Rata-rata WT = (0 + 3 + 7 + 15) ÷ 4 = 25 ÷ 4 = 6.25

Rata-rata TAT = (6 + 6 + 14 + 23) ÷ 4 = 49 ÷ 4 = 12.25

   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | 8,75 | 14,75| Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | 6,25 | 12,25 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

 ---

     


## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

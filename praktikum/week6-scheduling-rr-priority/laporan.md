
# Laporan Praktikum Minggu [X]
Topik: Algoritma RR dan Priority
---

## Identitas
- **Nama**  : Zaki Humam Faradi 
- **NIM**   : 250202972
- **Kelas** : 1ikra

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.
3. Membandingkan performa algoritma RR dan Priority.
4. Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori
Penjadwalan CPU adalah mekanisme dalam sistem operasi yang bertugas menentukan urutan eksekusi proses yang berada dalam antrian siap (ready queue). Tujuannya adalah untuk memaksimalkan penggunaan CPU, meminimalkan waktu tunggu, serta meningkatkan efisiensi dan kinerja sistem secara keseluruhan. Salah satu algoritma penjadwalan yang paling umum digunakan adalah Round Robin (RR). Algoritma ini bersifat preemptive dan menggunakan time quantum atau jatah waktu yang sama untuk setiap proses. Proses akan dieksekusi secara bergiliran; jika waktu yang dialokasikan habis sebelum proses selesai, maka CPU akan menghentikan sementara proses tersebut dan memberikannya kembali giliran setelah semua proses lain mendapatkan jatahnya.

Round Robin memiliki karakteristik yang adil karena setiap proses memperoleh kesempatan eksekusi yang sama, sehingga cocok untuk sistem time-sharing atau sistem interaktif. Namun, ukuran quantum harus ditentukan dengan hati-hati. Quantum yang terlalu kecil dapat menyebabkan terlalu banyak context switching, sehingga meningkatkan overhead sistem, sedangkan quantum yang terlalu besar akan membuat algoritma ini berperilaku seperti First Come First Serve (FCFS).

Sementara itu, Priority Scheduling adalah algoritma penjadwalan yang memilih proses berdasarkan tingkat prioritas. Proses dengan prioritas tertinggi akan dieksekusi terlebih dahulu, baik dengan cara preemptive (menghentikan proses lain yang sedang berjalan) maupun non-preemptive (menunggu proses selesai terlebih dahulu). Algoritma ini efisien dalam menangani proses penting atau kritis, terutama dalam sistem real-time.

Namun, kelemahan utama Priority Scheduling adalah kemungkinan terjadinya starvation, yaitu kondisi di mana proses dengan prioritas rendah tidak pernah mendapat giliran eksekusi karena selalu kalah oleh proses dengan prioritas tinggi. Untuk mengatasinya, dapat digunakan teknik aging, yaitu menaikkan prioritas proses yang telah menunggu terlalu lama. Secara umum, Round Robin lebih menekankan pada keadilan waktu eksekusi, sedangkan Priority Scheduling berfokus pada pentingnya urutan eksekusi berdasarkan tingkat kepentingan proses.

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).
      prioritas angka kecil = prioritas tinggi
Urutan eksekusi: P1 (0–5), P2 (5–8), P4 (8–14), P3 (14–22)
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
     ada di tugas
     
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```
---



---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<img width="1920" height="1080" alt="Screenshot 2025-11-11 182831" src="https://github.com/user-attachments/assets/30e05b0d-46db-4ecb-91da-c75705aed999" />
<img width="1920" height="1080" alt="Screenshot 2025-11-11 182815" src="https://github.com/user-attachments/assets/43791ec8-bbd0-4dce-bf07-d392f0d48743" />


---



## Kesimpulan
Kesimpulan Praktikum Penjadwalan CPU

Dari hasil praktikum dengan dua algoritma penjadwalan yaitu Round Robin dan Priority Scheduling, diperoleh bahwa masing-masing algoritma memiliki karakteristik dan performa yang berbeda. Pada percobaan ini, algoritma Priority Scheduling menghasilkan rata-rata Turnaround Time sebesar 10,75 dan rata-rata Waiting Time sebesar 5,25, sedangkan algoritma Round Robin menghasilkan rata-rata Turnaround Time sebesar 14,00 dan rata-rata Waiting Time sebesar 8,50.

Hasil tersebut menunjukkan bahwa algoritma Priority Scheduling lebih efisien dalam menyelesaikan proses dibandingkan dengan Round Robin karena waktu tunggu dan waktu penyelesaiannya lebih singkat. Namun, algoritma Round Robin lebih adil dalam pembagian waktu CPU karena setiap proses mendapat giliran secara bergantian.

Dengan demikian, pemilihan algoritma penjadwalan harus disesuaikan dengan kebutuhan sistem. Jika keadilan antar proses lebih diutamakan, maka digunakan algoritma Round Robin. Sebaliknya, jika efisiensi dan prioritas pekerjaan lebih penting, maka digunakan algoritma Priority Scheduling.

---

## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* untuk algoritma RR dan Priority.
   Data proses:

| Proses | Burst Time (BT) | Arrival Time (AT) | Priority |
| :----: | :-------------: | :---------------: | :------: |
|   P1   |        5        |         0         |     2    |
|   P2   |        3        |         1         |     1    |
|   P3   |        8        |         2         |     4    |
|   P4   |        6        |         3         |     3    |

Time quantum untuk RR = 3

---

## 1. Round Robin (RR)

### Langkah simulasi:

**Urutan eksekusi RR** berdasarkan arrival time dan giliran:

* Waktu 0–3: P1 → sisa 5–3=2
* Waktu 3–6: P2 → sisa 3–3=0 (selesai)
* Waktu 6–9: P3 → sisa 8–3=5
* Waktu 9–12: P4 → sisa 6–3=3
* Waktu 12–14: P1 → sisa 2–2=0 (selesai)
* Waktu 14–17: P3 → sisa 5–3=2
* Waktu 17–20: P4 → sisa 3–3=0 (selesai)
* Waktu 20–22: P3 → sisa 2–2=0 (selesai)

### Hitung Completion Time (CT)

| Proses |  CT |
| :----: | :-: |
|   P1   |  14 |
|   P2   |  6  |
|   P3   |  22 |
|   P4   |  20 |

### Hitung Turnaround Time (TAT = CT - AT)

| Proses |  CT |  AT | TAT = CT - AT |
| :----: | :-: | :-: | :-----------: |
|   P1   |  14 |  0  |  14 - 0 = 14  |
|   P2   |  6  |  1  |   6 - 1 = 5   |
|   P3   |  22 |  2  |  22 - 2 = 20  |
|   P4   |  20 |  3  |  20 - 3 = 17  |

### Hitung Waiting Time (WT = TAT - BT)

| Proses | TAT |  BT | WT = TAT - BT |
| :----: | :-: | :-: | :-----------: |
|   P1   |  14 |  5  |   14 - 5 = 9  |
|   P2   |  5  |  3  |   5 - 3 = 2   |
|   P3   |  20 |  8  |  20 - 8 = 12  |
|   P4   |  17 |  6  |  17 - 6 = 11  |

### Rata-rata

* Average TAT = (14 + 5 + 20 + 17)/4 = 56/4 = 14
* Average WT = (9 + 2 + 12 + 11)/4 = 34/4 = 8.5

---

## 2. Priority Scheduling (Non-preemptive)

Aturan: prioritas angka kecil = prioritas tinggi
Urutan eksekusi: P1 (0–5), P2 (5–8), P4 (8–14), P3 (14–22)

### Hitung Completion Time (CT)

| Proses | Start |  BT | CT = Start + BT |
| :----: | :---: | :-: | :-------------: |
|   P1   |   0   |  5  |    0 + 5 = 5    |
|   P2   |   5   |  3  |    5 + 3 = 8    |
|   P4   |   8   |  6  |    8 + 6 = 14   |
|   P3   |   14  |  8  |   14 + 8 = 22   |

### Hitung Turnaround Time (TAT = CT - AT)

| Proses |  CT |  AT | TAT = CT - AT |
| :----: | :-: | :-: | :-----------: |
|   P1   |  5  |  0  |   5 - 0 = 5   |
|   P2   |  8  |  1  |   8 - 1 = 7   |
|   P4   |  14 |  3  |  14 - 3 = 11  |
|   P3   |  22 |  2  |  22 - 2 = 20  |

### Hitung Waiting Time (WT = TAT - BT)

| Proses | TAT |  BT | WT = TAT - BT |
| :----: | :-: | :-: | :-----------: |
|   P1   |  5  |  5  |   5 - 5 = 0   |
|   P2   |  7  |  3  |   7 - 3 = 4   |
|   P4   |  11 |  6  |   11 - 6 = 5  |
|   P3   |  20 |  8  |  20 - 8 = 12  |

### Rata-rata

* Average TAT = (5 + 7 + 11 + 20)/4 = 43/4 = 10.75
* Average WT = (0 + 4 + 5 + 12)/4 = 21/4 = 5.25

---

## Tabel Rangkuman
| Algoritma | Proses |  BT |  AT |  CT | TAT |  WT |
| :-------: | :----: | :-: | :-: | :-: | :-: | :-: |
|     RR    |   P1   |  5  |  0  |  14 |  14 |  9  |
|     RR    |   P2   |  3  |  1  |  6  |  5  |  2  |
|     RR    |   P3   |  8  |  2  |  22 |  20 |  12 |
|     RR    |   P4   |  6  |  3  |  20 |  17 |  11 |
|  Priority |   P1   |  5  |  0  |  5  |  5  |  0  |
|  Priority |   P2   |  3  |  1  |  8  |  7  |  4  |
|  Priority |   P4   |  6  |  3  |  14 |  11 |  5  |
|  Priority |   P3   |  8  |  2  |  22 |  20 |  12 |




Rata-rata:

* RR → TAT = 14, WT = 8.5
* Priority → TAT = 10.75, WT = 5.25



2. Sajikan hasil perhitungan dan Gantt Chart dalam `laporan.md`.
 hasil perhitungan di nomor 1
3. Bandingkan performa dan jelaskan pengaruh *time quantum* serta prioritas.
 Berdasarkan hasil perbandingan, algoritma Priority memiliki rata-rata turnaround time dan waiting time yang lebih kecil dibandingkan Round Robin, yaitu 10,75 dan 5,25, sedangkan Round Robin menghasilkan 14 dan 8,5. Hal ini menunjukkan bahwa Priority lebih efisien dalam menyelesaikan proses secara keseluruhan. Pengaruh time quantum pada Round Robin sangat besar karena jika quantum terlalu kecil, sistem akan sering melakukan pergantian proses sehingga waiting time meningkat, sedangkan jika terlalu besar, algoritma akan menyerupai FCFS dan membuat proses pendek menunggu lebih lama. Sementara itu, algoritma Priority menentukan urutan eksekusi berdasarkan tingkat prioritas, sehingga proses yang lebih penting atau memiliki prioritas tinggi diselesaikan lebih cepat. Namun, kelemahannya adalah kemungkinan terjadinya starvation pada proses dengan prioritas rendah. Secara keseluruhan, Priority lebih unggul dalam efisiensi waktu, sedangkan Round Robin lebih adil dan cocok untuk sistem interaktif yang membutuhkan respons cepat.
   
4. Simpan semua bukti (tabel, grafik, atau gambar) ke folder `screenshots/`.  

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?  
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?  
3. Mengapa algoritma Priority dapat menyebabkan *starvation*?  

jawab:

1. **Perbedaan utama** adalah **Round Robin** memberikan waktu eksekusi bergiliran secara adil untuk setiap proses, sedangkan **Priority Scheduling** mengeksekusi proses berdasarkan tingkat **prioritas**.  

2. **Time quantum** yang terlalu **kecil** membuat CPU sering berpindah proses sehingga efisiensi menurun, sedangkan **time quantum** yang terlalu **besar** membuat proses kecil harus menunggu lama.  

3. Algoritma **Priority** dapat menyebabkan **starvation** karena proses dengan prioritas rendah bisa tertunda terus jika selalu ada proses dengan prioritas lebih tinggi.

---
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  cukup sulit dalam pengerjaannya
- Bagaimana cara Anda mengatasinya?  tanya teman

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

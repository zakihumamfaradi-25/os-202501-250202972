
# Laporan Praktikum Minggu [9]
Topik: "Simulasi Algoritma Penjadwalan CPU"
---

## Identitas
- **Nama**  : Zaki Humam Faradi 
- **NIM**   :250202972
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.
4. Menjelaskan hasil simulasi secara tertulis.
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.


---

## Dasar Teori
1. Konsep Dasar Penjadwalan CPU: Merupakan mekanisme utama dalam sistem operasi multiprogramming untuk memaksimalkan utilitas CPU. Tujuannya adalah memastikan CPU selalu sibuk dengan cara beralih di antara berbagai proses yang berada dalam antrean (ready queue).
2. Kriteria Penjadwalan: Digunakan sebagai parameter untuk mengukur efisiensi algoritma. Kriteria utama meliputi Waiting Time (total waktu tunggu proses di ready queue), Turnaround Time (waktu total dari saat proses masuk hingga selesai), dan Response Time (waktu sejak permintaan masuk hingga respons pertama diberikan).
3. Gantt Chart sebagai Alat Simulasi: Dalam percobaan, Gantt Chart digunakan untuk memvisualisasikan urutan eksekusi proses secara kronologis. Diagram ini memudahkan penghitungan statistik performa algoritma seperti rata-rata waktu tunggu (Average Waiting Time).


---

## Langkah Praktikum
1. Menyiapkan Dataset Buat dataset proses minimal berisi data yang telah disajikan.
2. Implementasi Algoritma
Program harus: Menghitung waiting time dan turnaround time.
               Mendukung minimal 1 algoritma (FCFS atau SJF non-preemptive).
               Menampilkan hasil dalam tabel.
3. Eksekusi & Validasi : Jalankan program menggunakan dataset uji. Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.Simpan Hasil Screenshot.
4. Analisis :  Jelaskan alur program.
               Bandingkan hasil simulasi dengan perhitungan manual.
               Jelaskan kelebihan dan keterbatasan simulasi.
5. Commit & Push
git add .
git commit -m "Minggu 9 - Simulasi Scheduling CPU"
git push origin main


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
praktikum/week9-sim-scheduling/
├─ code/
│  ├─ scheduling_simulation.*
│  └─ dataset.csv
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<img width="1042" height="254" alt="Screenshot 2026-01-03 083229" src="https://github.com/user-attachments/assets/f789ac7e-141f-43e4-af47-a5f9ee58036d" />


---

## Analisis
# Simulasi Penjadwalan CPU Menggunakan Algoritma FCFS

## 1. Alur Program

Program simulasi penjadwalan CPU menggunakan algoritma **First Come First Served (FCFS)** bekerja dengan alur sebagai berikut:

1. Program dimulai dengan mendefinisikan dataset proses yang terdiri dari:
   - ID proses
   - Arrival Time (AT)
   - Burst Time (BT)

2. Variabel `current_time` diinisialisasi dengan nilai 0 sebagai penanda waktu CPU saat ini.

3. Proses dijalankan berdasarkan urutan kedatangan sesuai prinsip algoritma FCFS.

4. Untuk setiap proses, program melakukan:
   - Penentuan waktu mulai eksekusi (start time).
   - Perhitungan Waiting Time (WT) dengan rumus:
     ```
     WT = Start Time - Arrival Time
     ```
   - Perhitungan Completion Time dan Turnaround Time (TAT) dengan rumus:
     ```
     TAT = Completion Time - Arrival Time
     ```

5. Nilai Waiting Time dan Turnaround Time setiap proses ditampilkan dalam bentuk tabel.

6. Program selesai setelah seluruh proses dieksekusi.

---

## 2. Perbandingan Hasil Simulasi dengan Perhitungan Manual

Hasil simulasi dibandingkan dengan perhitungan manual yang telah dilakukan sebelumnya.

| Proses | WT Manual | WT Simulasi | TAT Manual | TAT Simulasi |
|------|----------|------------|-----------|-------------|
| P1 | 0 | 0 | 5 | 5 |
| P2 | 4 | 4 | 7 | 7 |
| P3 | 6 | 6 | 14 | 14 |
| P4 | 13 | 13 | 19 | 19 |

### Analisis
Hasil simulasi menunjukkan nilai Waiting Time dan Turnaround Time yang sama dengan perhitungan manual. Hal ini membuktikan bahwa implementasi algoritma FCFS pada program telah berjalan dengan benar dan sesuai dengan teori penjadwalan CPU.

---

## 3. Kelebihan dan Keterbatasan Simulasi

### Kelebihan
- Mengurangi risiko kesalahan perhitungan dibandingkan metode manual.
- Mempercepat proses analisis penjadwalan CPU.
- Dapat digunakan untuk menguji berbagai dataset proses.
- Menampilkan hasil secara terstruktur dalam bentuk tabel.

### Keterbatasan
- Simulasi hanya mendukung algoritma FCFS.
- Tidak mempertimbangkan prioritas proses.
- Tidak mendukung sistem preemptive.
- Tidak sepenuhnya merepresentasikan kondisi sistem operasi nyata, seperti waktu tunggu I/O.

---

## Kesimpulan

Simulasi penjadwalan CPU menggunakan algoritma FCFS menghasilkan perhitungan Waiting Time dan Turnaround Time yang akurat dan sesuai dengan perhitungan manual. Simulasi ini efektif untuk memahami konsep dasar penjadwalan proses, meskipun masih memiliki keterbatasan dalam kompleksitas algoritma yang didukung.

---

## Quiz
1. [Mengapa simulasi diperlukan untuk menguji algoritma scheduling?]  
   **Jawaban:Simulasi sangat penting untuk menguji algoritma penjadwalan karena memungkinkan pengembang untuk menganalisis perilaku algoritma secara aman tanpa risiko merusak sistem operasi yang sedang berjalan (live system). Melalui simulasi, variabel kompleks seperti waktu kedatangan dan durasi proses dapat dimanipulasi dengan mudah untuk mengamati fenomena seperti convoy effect atau starvation secara berulang dalam lingkungan yang terkontrol. Selain itu, simulasi jauh lebih efisien dari segi biaya dan waktu dibandingkan melakukan pengujian pada perangkat keras nyata, sehingga memudahkan perbandingan performa antar algoritma secara objektif sebelum diimplementasikan ke dalam kernel yang sesungguhnya.**  
2. [Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?]  
   **Jawaban:Perhitungan manual sangat berisiko terhadap kesalahan manusia (human error) dan menjadi tidak praktis karena membutuhkan waktu yang sangat lama untuk memproses ribuan data secara beruntun. Sebaliknya, simulasi komputer mampu mengolah dataset besar dalam hitungan milidetik dengan akurasi yang presisi, serta memudahkan pembaruan data secara otomatis tanpa harus mengulang perhitungan dari awal. Selain itu, simulasi memungkinkan pembuatan visualisasi statistik dan Gantt Chart yang rumit secara instan, sehingga memudahkan analisis performa algoritma yang sulit dicapai melalui cara manual.**  
3. [Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.]  
   **Jawaban:Algoritma yang paling mudah diimplementasikan adalah First-Come, First-Served (FCFS) karena logikanya hanya menggunakan prinsip antrean sederhana atau FIFO (First-In, First-Out). Dalam implementasi kodenya, pengembang tidak perlu membuat fungsi pengurutan ulang yang rumit seperti pada Shortest Job First (SJF) atau mengatur interupsi kuantum waktu seperti pada Round Robin, melainkan cukup mengeksekusi proses berdasarkan urutan kedatangannya saja. Algoritma ini juga memiliki beban sistem (overhead) yang sangat rendah karena tidak memerlukan prediksi waktu pengerjaan di masa depan, sehingga struktur datanya sangat ringkas dan mudah dipahami bagi pemula dalam pemrograman sistem operasi.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
  menggunkan bahasa pemograman python yang dimana belum sampai di materi di matkul algoritma pemograman  
- Bagaimana cara Anda mengatasinya?
  bertanya kepada teman dan meminta untuk mengajari

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

# Laporan Proyek Kelompok: Mini Simulasi Sistem Operasi

---

## 1. Pendahuluan

### 1.1 Latar Belakang

Sistem Operasi (OS) memiliki peran vital dalam mengelola sumber daya komputer, terutama dalam mengatur antrean proses pada CPU dan alokasi memori utama. Memahami algoritma internal OS seperti **First-Come First-Served (FCFS)** dan **First-In First-Out (FIFO)** seringkali sulit jika hanya melalui teori.

Proyek ini menghadirkan aplikasi simulasi berbasis terminal (**CLI**) yang mengimplementasikan kedua konsep tersebut. Simulasi ini menggunakan dataset nyata (file `.csv` dan `.txt`) untuk menghitung metrik kinerja secara otomatis, seperti *Waiting Time* pada penjadwalan CPU dan *Page Fault* pada manajemen memori. Dengan menggunakan **Docker**, proyek ini memastikan bahwa lingkungan eksekusi tetap konsisten bagi siapa pun yang menjalankannya.

### 1.2 Tujuan Proyek

1. Mengintegrasikan konsep **CPU Scheduling** dan **Memory Management** dalam satu aplikasi modular
2. Menerapkan pengolahan data dari file eksternal (CSV dan TXT) menggunakan bahasa pemrograman **Python**
3. Mengelola proyek secara kolaboratif menggunakan alur kerja **Git** dan pendokumentasian yang sistematis
4. Mengimplementasikan **Dockerization** untuk mempermudah distribusi dan eksekusi aplikasi di berbagai platform

---

## 2. Arsitektur Aplikasi

### 2.1 Desain Arsitektur Umum

Aplikasi ini dirancang dengan struktur modular untuk memisahkan antara antarmuka menu, logika algoritma, dan penyimpanan data.

#### Komponen Utama

- **`main.py`** - Berfungsi sebagai *entry point* (pengendali utama) yang menangani navigasi menu
- **`cpu_scheduling.py`** - Berisi fungsi `simulasi_fcfs` untuk menghitung urutan proses dan waktu tunggu
- **`page_replacement.py`** - Berisi fungsi `simulasi_fifo` untuk mensimulasikan pergantian halaman di RAM
- **`data/`** - Folder yang menyimpan dataset `processes.csv` dan `page.txt`

### 2.2 Deskripsi Modul

#### Modul CPU Scheduling (FCFS)

- Membaca file `processes.csv`
- Melakukan pengurutan berdasarkan *Arrival Time*
- Menghitung *Waiting Time* (WT) dan *Turnaround Time* (TAT)

#### Modul Memory Management (FIFO)

- Membaca referensi aplikasi dari `page.txt`
- Menerima input manual jumlah frame RAM dari pengguna
- Mensimulasikan antrean frame (jika penuh, data terlama dihapus)

### 2.3 Alur Data (Data Flow)

1. Pengguna memilih menu pada `main.py`
2. Modul terkait memuat data dari folder `data/`
3. Logika algoritma memproses data tersebut (pengurutan atau antrean)
4. Hasil kalkulasi ditampilkan kembali ke terminal dalam bentuk tabel ringkasan

---

## 3. Demo Menjalankan Aplikasi

Aplikasi telah dibungkus menggunakan Docker untuk memastikan kemudahan penggunaan.

### 3.1 Prosedur Eksekusi (Docker)

Langkah-langkah untuk menjalankan aplikasi via Docker:

```bash
# 1. Membangun Image dari Dockerfile
docker build -t week-15 .

# 2. Menjalankan Container secara Interaktif
docker run -it --rm week-15
```

### 3.2 Bukti Eksekusi

Tangkapan layar (*screenshot*) hasil eksekusi program, baik tampilan menu utama maupun hasil tabel perhitungan, telah kami lampirkan dalam folder `screenshots/` sebagai bukti validasi bahwa aplikasi berjalan sesuai spesifikasi.

---

## 4. Hasil Pengujian dan Analisis

### 4.1 Hasil Modul CPU Scheduling (FCFS)

Berdasarkan data `processes.csv` (eFootball, PUBG, ML, Spotify):

- **Total Waktu Eksekusi**: Tergantung pada akumulasi *Burst Time*
- **Analisis**: Proses dieksekusi secara sekuensial. Proses `Spotify` yang datang terakhir (Arrival 3) harus menunggu hingga `eFootball`, `PUBG`, dan `ML` selesai, mengakibatkan *Waiting Time* yang lebih tinggi dibandingkan proses pertama.

### 4.2 Hasil Modul Page Replacement (FIFO)

Berdasarkan data `page.txt` dan asumsi **3 Frame**:

- **Status Hit/Fault**: Terjadi *Fault* saat aplikasi baru (seperti YouTube) masuk ketika RAM sudah penuh oleh eFootball, PUBG, dan ML
- **Analisis**: Karena menggunakan FIFO, `eFootball` sebagai aplikasi yang masuk pertama kali akan "dibuang" (pop index 0) saat `Spotify` atau `YouTube` membutuhkan ruang di RAM

---

## 5. Pembagian Peran dan Kontribusi

| Nama Anggota | Peran | Kontribusi |
|--------------|-------|------------|
| **Zaki Humam Faradi** | Project Lead | Integrasi `main.py`, Dockerfile, dan repositori Git |
| **Andi Pratama** | Developer 1 | Pengembangan `cpu_scheduling.py` dan dataset CSV |
| **Rifki Hidayat** | Developer 2 | Pengembangan `page_replacement.py` dan dataset TXT |
| **Ismatul Khoeriyah** | Dokumentasi | Penyusunan `README.md` dan `laporan.md` |

---

## 6. Jawaban Quiz

### 1. Tantangan terbesar integrasi modul apa, dan bagaimana solusinya?

**Tantangan:**  
Menangani error `FileNotFoundError` saat file dataset dipanggil dari dalam container Docker karena struktur folder yang berbeda.

**Solusi:**  
Menggunakan *relative path* (`data/filename`) dan memastikan instruksi `COPY . .` di Dockerfile menyertakan folder `data`.

### 2. Mengapa Docker membantu proses demo dan penilaian proyek?

Docker memastikan asisten praktikum tidak perlu menginstal dependensi manual. Cukup dengan satu baris perintah, aplikasi berjalan dengan konfigurasi Python yang sama persis (versi 3.14-slim) seperti di laptop pengembang.

### 3. Jika dataset diperbesar 10x, modul mana yang paling terdampak performanya?

**Jawaban: Modul CPU Scheduling**

Hal ini dikarenakan adanya fungsi `proses.sort(key=lambda x: x["arrival"])`. Python menggunakan *Timsort* dengan kompleksitas O(n log n). Jika data bertambah 10x, proses pengurutan akan memakan waktu lebih banyak dibandingkan modul Memory (FIFO) yang hanya melakukan iterasi linear O(n) terhadap list aplikasi.

---

## 7. Kesimpulan

Proyek ini berhasil mensimulasikan fungsi manajemen proses dan memori secara akurat sesuai dengan algoritma FCFS dan FIFO. Penggunaan arsitektur modular dan Dockerization terbukti meningkatkan efisiensi pengembangan dan distribusi perangkat lunak.

---

## Lampiran

**Tautan Repositori:** [https://github.com/zakihumamfaradi-25/os-202501-250202972.git]

---

*Dokumen ini disusun sebagai bagian dari Laporan Tugas Praktikum Sistem Operasi*

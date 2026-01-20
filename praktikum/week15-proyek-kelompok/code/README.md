# Mini Simulasi Sistem Operasi

Aplikasi berbasis terminal (**CLI**) ini dibuat untuk mensimulasikan dua konsep utama pada **Sistem Operasi**, yaitu **CPU Scheduling** dan **Memory Management**. Program ditulis menggunakan bahasa **Python** dan digunakan sebagai **Tugas Praktikum Minggu 15**.

---

## Fitur Utama

### 1. Simulasi CPU Scheduling (FCFS)

* **Algoritma**: First Come First Served (FCFS)
* **Deskripsi**:
  Proses akan dieksekusi berdasarkan waktu kedatangan (*arrival time*). Proses yang datang lebih dulu akan diproses terlebih dahulu hingga selesai (non-preemptive).
* **Input**: File `processes.csv`
* **Output**:

  * Waiting Time setiap proses
  * Turnaround Time setiap proses
  * Rata-rata Waiting Time
  * Rata-rata Turnaround Time

### 2. Simulasi Memory Management (FIFO)

* **Algoritma**: First In First Out (FIFO)
* **Deskripsi**:
  Simulasi manajemen memori RAM. Jika memori penuh dan halaman baru masuk, maka halaman yang pertama kali masuk akan dikeluarkan terlebih dahulu.
* **Input**: File `page.txt`
* **Output**:

  * Status Hit / Fault
  * Isi frame RAM setiap referensi halaman
  * Total Page Fault

---

## Struktur Folder

```text
project/
├── main.py               # Program utama (menu aplikasi)
├── cpu_scheduling.py     # Modul simulasi FCFS
├── page_replacement.py   # Modul simulasi FIFO
├── README.md             # Dokumentasi proyek
└── data/
    ├── processes.csv     # Dataset CPU Scheduling
    └── page.txt          # Dataset Page Replacement
```

---

## Cara Menjalankan Program

### 1. Menjalankan Secara Manual (Python Lokal)

**Persyaratan**:

* Python 3.x sudah terinstal

**Langkah-langkah**:

1. Buka terminal / command prompt
2. Arahkan ke folder project
3. Jalankan perintah berikut:

```bash
python main.py
```

---

## Menu Program

Saat program dijalankan, akan muncul menu:

```
=== MINI SIMULASI SISTEM OPERASI ===
1. Simulasi CPU Scheduling (FCFS)
2. Simulasi Memory Management (FIFO)
3. Keluar
```

* Pilih **1** untuk simulasi CPU Scheduling
* Pilih **2** untuk simulasi Memory Management
* Pilih **3** untuk keluar dari program

---

## Konfigurasi Dataset

### 1. Dataset CPU Scheduling (`data/processes.csv`)

**Format**:

```
Process,ArrivalTime,BurstTime
```

**Contoh Isi**:

```
eFootball,0,5
PUBG,1,3
ML,2,8
Spotify,3,6
```

Keterangan:

* `Process` : Nama proses
* `ArrivalTime` : Waktu kedatangan proses
* `BurstTime` : Lama proses dieksekusi

---

### 2. Dataset Memory Management (`data/page.txt`)

**Format**:

* Nama halaman/aplikasi dipisahkan dengan koma

**Contoh Isi**:

```
eFootball,PUBG,ML,eFootball,Spotify,PUBG,YouTube,ML,eFootball
```

---

## Catatan

* Jumlah frame RAM dimasukkan secara manual saat program berjalan
* Pastikan nama file dan format data sudah sesuai
* Program akan menampilkan pesan error jika file tidak ditemukan

---

## Penutup

Program ini dibuat untuk membantu memahami konsep **CPU Scheduling FCFS** dan **Page Replacement FIFO** secara sederhana melalui simulasi berbasis terminal.

Semoga bermanfaat sebagai media pembelajaran Sistem Operasi 🙌

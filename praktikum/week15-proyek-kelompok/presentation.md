# PRESENTASI PROYEK KELOMPOK: MINI SIMULASI OS
**Topik:** CPU Scheduling (FCFS) & Memory Management (FIFO)

**Minggu:** 15

---

## Nama Anggota Kelompok 
- Zaki Humam Faradi (250202972)
- Andi Pratama (250202975)
- Rifki Hidayat (250202964)
- Ismatul Khoeriyah (250202912)

---
  
## 1. PENDAHULUAN

### Latar Belakang
- Konsep OS (CPU Scheduling & Memory Management) seringkali abstrak dan sulit dibayangkan.
- Kami membuat aplikasi **Mini Simulasi** dengan analogi sehari-hari agar lebih konkret.

### Studi Kasus
1. **Simulasi CPU Scheduling**, yang merepresentasikan algoritma *First-Come First-Served* (FCFS). 
   - Dalam simulasi ini, proses yang datang pertama kali akan dieksekusi hingga selesai sebelum sistem beralih ke proses berikutnya.
   - Menggunakan analogi aplikasi mobile (eFootball, PUBG, Mobile Legends, Spotify).

2. **Simulasi Page Replacement**, yang memodelkan algoritma FIFO (*First-In First-Out*). 
   - Simulasi ini menggambarkan manajemen memori RAM, di mana aplikasi yang paling lama dibuka akan ditutup secara otomatis oleh sistem ketika kapasitas memori (RAM) telah penuh dan pengguna membuka aplikasi baru.
   - Menggunakan data referensi aplikasi seperti eFootball, PUBG, ML, YouTube, dan Spotify.

---

## 2. ARSITEKTUR APLIKASI

### Tech Stack
- **Bahasa:** Python (Berbasis CLI/Terminal).
- **Environment:** Docker (Untuk konsistensi / *reproducible*).
- **Version Control:** Git (Branching per fitur).

### Desain Modular
Secara garis besar, arsitektur aplikasi terdiri dari tiga komponen utama:

1. **Controller Utama (`main.py`):** Bertindak sebagai pintu masuk (*entry point*) aplikasi yang menangani interaksi pengguna, menampilkan menu pilihan, dan memanggil fungsi dari modul yang relevan.

2. **Modul Logika (*Logic Modules*):** Berkas terpisah yang berisi implementasi algoritma sistem operasi:
   - `cpu_scheduling.py` untuk penjadwalan CPU
   - `page_replacement.py` untuk manajemen memori

3. **Manajemen Data (*Data Layer*):** Penyimpanan data input statis dalam bentuk berkas:
   - `data/processes.csv` - berisi data proses (Process, ArrivalTime, BurstTime)
   - `data/page.txt` - berisi sequence referensi aplikasi

---

## 3. DATASET

### Dataset CPU Scheduling (processes.csv)
```csv
Process,ArrivalTime,BurstTime
eFootball,0,5
PUBG,1,3
ML,2,8
Spotify,3,6
```

**Karakteristik:**
- 4 proses dengan variasi arrival time dan burst time
- Simulasi aplikasi mobile yang umum digunakan
- Total burst time: 22 unit waktu

### Dataset Page Replacement (page.txt)
```
eFootball,PUBG,ML,eFootball,Spotify,PUBG,YouTube,ML,eFootball
```

**Karakteristik:**
- 9 referensi halaman
- 5 aplikasi unik (eFootball, PUBG, ML, Spotify, YouTube)
- Mendemonstrasikan temporal locality (eFootball muncul 3x)

---

## 4. LIVE DEMO

### Skenario Demo

**Step 1: Jalankan Docker**
```bash
docker build -t week-15 .
docker run -it --rm week-15
```

**Step 2: Simulasi CPU Scheduling (FCFS)**
- Pilih menu: 1
- Input: Otomatis membaca `data/processes.csv`
- Amati: 
  - Urutan eksekusi proses
  - Waiting time setiap proses
  - Average waiting time

**Step 3: Simulasi Page Replacement (FIFO)**
- Pilih menu: 2
- Input jumlah frame RAM: **3**
- Input: Otomatis membaca `data/page.txt`
- Amati: 
  - Status HIT/FAULT setiap referensi
  - Frame state changes
  - Total page faults

---

## 5. HASIL & ANALISIS: CPU SCHEDULING (FCFS)

### Data Uji
Berdasarkan file `processes.csv`:
- eFootball: Arrival=0, Burst=5
- PUBG: Arrival=1, Burst=3
- ML: Arrival=2, Burst=8
- Spotify: Arrival=3, Burst=6

### Hasil Eksekusi
```
Proses    | Arrival | Burst | Waiting | Turnaround
----------|---------|-------|---------|------------
eFootball |    0    |   5   |    0    |     5
PUBG      |    1    |   3   |    4    |     7
ML        |    2    |   8   |    6    |    14
Spotify   |    3    |   6   |   13    |    19

Average Waiting Time: 5.75 unit waktu
Average Turnaround Time: 11.25 unit waktu
```

### Analisis
- **Convoy Effect terdeteksi**: Proses ML (burst=8) membuat Spotify harus menunggu lama (13 unit).
- Proses PUBG (burst kecil=3) harus menunggu 4 unit meskipun bisa diselesaikan dengan cepat.
- **Kesimpulan:** FCFS adil secara urutan kedatangan, tapi tidak efisien untuk *waiting time* jika ada proses besar di tengah antrian.
- **Trade-off:** Kesederhanaan implementasi vs optimasi performa.

---

## 6. HASIL & ANALISIS: MEMORY (FIFO)

### Data Uji
- Sequence: eFootball, PUBG, ML, eFootball, Spotify, PUBG, YouTube, ML, eFootball
- Kapasitas RAM: **3 Frame**

### Hasil Eksekusi
```
Page Reference | Frame State              | Status
---------------|--------------------------|--------
eFootball      | [eFootball]              | FAULT
PUBG           | [eFootball, PUBG]        | FAULT
ML             | [eFootball, PUBG, ML]    | FAULT
eFootball      | [eFootball, PUBG, ML]    | HIT
Spotify        | [PUBG, ML, Spotify]      | FAULT (evict eFootball)
PUBG           | [PUBG, ML, Spotify]      | HIT
YouTube        | [ML, Spotify, YouTube]   | FAULT (evict PUBG)
ML             | [ML, Spotify, YouTube]   | HIT
eFootball      | [Spotify, YouTube, eFootball] | FAULT (evict ML)

Total Page Faults: 6
Page Hits: 3
Hit Rate: 33.33%
```

### Analisis
- **FIFO murni berdasarkan waktu masuk**: Tidak mempertimbangkan frekuensi penggunaan.
- Aplikasi **eFootball** yang sering dipakai (muncul 3x) tetap dihapus saat RAM penuh karena ia "paling tua" di memori.
- Akibatnya, saat `eFootball` dibuka lagi, terjadi page fault (loading ulang).
- **Kesimpulan:** FIFO mudah diimplementasi, tapi kurang optimal untuk pola penggunaan aplikasi yang repetitif.
- **Rekomendasi:** Algoritma LRU (Least Recently Used) akan lebih baik untuk workload dengan temporal locality.

---

## 7. IMPLEMENTASI KODE INTI

### CPU Scheduling (cpu_scheduling.py)
```python
def simulasi_fcfs(nama_file):
    proses = []
    
    # Load CSV
    with open(nama_file, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            proses.append({
                "nama": row["Process"],
                "arrival": int(row["ArrivalTime"]),
                "burst": int(row["BurstTime"])
            })
    
    # Sort by arrival time (FCFS core)
    proses.sort(key=lambda x: x["arrival"])
    
    # Calculate metrics
    waktu = 0
    for p in proses:
        if waktu < p["arrival"]:
            waktu = p["arrival"]
        
        waiting_time = waktu - p["arrival"]
        waktu += p["burst"]
```

### Page Replacement (page_replacement.py)
```python
def simulasi_fifo(nama_file, jumlah_frame):
    # Load page references
    with open(nama_file, "r") as file:
        pages = [p.strip() for p in file.read().split(",")]
    
    frame = []
    page_fault = 0
    
    for page in pages:
        if page in frame:
            status = "Hit"
        else:
            page_fault += 1
            
            if len(frame) < jumlah_frame:
                frame.append(page)
            else:
                frame.pop(0)  # FIFO eviction
                frame.append(page)
```

---

## 8. TIM & KONTRIBUSI

Proyek dikerjakan menggunakan Git Flow dengan pembagian peran:

| Nama Anggota | Peran Utama | Deskripsi Kontribusi |
|--------------|-------------|----------------------|
| **Zaki Humam Faradi** | *Project Lead & Integrator* | • Merancang struktur awal proyek dan `main.py`<br>• Mengelola repositori Git (merge PR, resolve conflict)<br>• Membuat konfigurasi `Dockerfile` agar aplikasi berjalan di container<br>• Melakukan pengujian fungsional seluruh modul<br>• Mengumpulkan *screenshot* bukti demo |
| **Andi Pratama** | *Developer (Modul Scheduling)* | • Mengimplementasikan algoritma FCFS pada `cpu_scheduling.py`<br>• Menyusun logika *sorting* data berdasarkan waktu kedatangan<br>• Membuat dataset `processes.csv`<br>• Testing CPU module |
| **Rifki Hidayat** | *Developer (Modul Memory)* | • Mengimplementasikan algoritma FIFO pada `page_replacement.py`<br>• Membuat visualisasi tabel isi RAM<br>• Menyusun dataset `page.txt` dan skenario uji *page fault*<br>• Testing Memory module |
| **Ismatul Khoeriyah** | *Documentation & QA* | • Menyusun file `README.md` dan dokumentasi cara penggunaan<br>• Menyusun file dokumen akhir `laporan.md`<br>• Membuat slide presentasi<br>• Quality assurance testing |

### Statistik Kontribusi
- **Total Commits:** 45+
- **Branches:** 4 (main, feature/fcfs, feature/fifo, docs/readme)
- **Pull Requests:** 12
- **Collaboration Tools:** Git, GitHub

---

## 9. KESIMPULAN

### Key Takeaways
1. **FCFS (CPU):**
   - Kelebihan: Simple, no starvation, deterministik
   - Kekurangan: Convoy effect, poor average waiting time
   - Use case: Batch processing systems

2. **FIFO (Memory):**
   - Kelebihan: Implementasi mudah, low overhead
   - Kekurangan: Ignores usage patterns, Belady's Anomaly
   - Use case: Simple memory management tanpa hardware support

3. **Docker Containerization:**
   - Memastikan konsistensi environment
   - Eliminasi "works on my machine" problem
   - Memudahkan deployment dan testing

### Pembelajaran Tim
- Kolaborasi menggunakan Git branching strategy
- Importance of modular design
- Trade-offs dalam pemilihan algoritma OS
- Value of empirical testing vs theoretical analysis

---

## 10. DEMO & Q&A

**Repository GitHub:**  
https://github.com/zakihumamfaradi-25/os-202501-250202972.git

**Demo Commands:**
```bash
# Clone repository
git clone https://github.com/zakihumamfaradi-25/os-202501-250202972.git

# Build Docker image
docker build -t mini-os-simulasi .

# Run container
docker run -it --rm mini-os-simulasi
```

---

**Terima Kasih**  
*Ada Pertanyaan?*


# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)
---

## Identitas
- **Nama**  : Zaki Humam Faradi
- **NIM**   : 250202972
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan praktikum ini, mahasiswa diharapkan mampu:
1.  Menulis Dockerfile sederhana untuk membungkus aplikasi atau skrip uji.
2.  Membangun (build) image dan menjalankan container dari image tersebut.
3.  Menerapkan pembatasan sumber daya (Resource Limit) berupa CPU dan Memori pada container.
4.  Mengamati dan menganalisis perilaku container saat dijalankan dengan dan tanpa batasan resource.
5.  Memahami mekanisme sistem operasi dalam menangani proses yang melebihi batas alokasi memori (OOM Kill).

---

## Dasar Teori
### Docker & Containerization
Docker adalah platform untuk mengemas aplikasi beserta seluruh dependensinya (library, konfigurasi) ke dalam sebuah unit standar yang disebut **Container**. Berbeda dengan Virtual Machine (VM) yang meniru perangkat keras dan membutuhkan OS penuh, container berjalan di atas kernel OS host yang sama namun terisolasi satu sama lain. Hal ini membuat container jauh lebih ringan dan cepat.

### Resource Isolation & Cgroups
Cgroups memungkinkan sistem untuk membatasi, menghitung, dan mengisolasi penggunaan sumber daya (CPU, memori, disk I/O, network) dari sekumpulan proses. Dengan fitur ini, kita dapat memastikan bahwa satu container tidak menghabiskan seluruh sumber daya host yang dapat mengganggu kinerja container lain atau sistem utama.

### Memory Limit & OOM Killed
Ketika sebuah container dibatasi penggunaan memorinya (misalnya 256MB), kernel akan memantau konsumsi RAM container tersebut. Jika aplikasi di dalam container mencoba mengalokasikan memori melebihi batas yang ditentukan (Hard Limit) dan tidak ada ruang Swap yang tersedia, kernel Linux akan melakukan tindakan terminasi paksa yang disebut **OOM (Out Of Memory) Killer**. Proses akan dimatikan seketika untuk menjaga stabilitas sistem, biasanya ditandai dengan Exit Code 137.

### Dockerfile
Dockerfile adalah file teks berisi serangkaian instruksi yang dibaca oleh Docker untuk membangun sebuah image secara otomatis. Instruksi umum meliputi `FROM` (base image), `WORKDIR` (direktori kerja), `COPY` (menyalin file), dan `CMD` (perintah eksekusi).

---

## Langkah Praktikum
### A. Persiapan & Instalasi
1.  Mengunduh aplikasi **Docker Dekstop**.
    -  **Docker Dekstop** : https://www.docker.com/products/docker-desktop/ 
2.  Menginstall Docker Desktop pada PC atau Laptop.
3.  Membuka Aplikasi agar server docker berjalan
4.  Install Extension `Container Tools` agar bisa berjalan di `Visual Code Studio`
5.  Pastikan Docker terpasang dan berjalan dengan perintah:
   ```bash
      docker version
      docker ps
   ```

### B. Pembuatan Program Uji (`app.py`) dan Dockerfile
1. Membuat script Python dengan skenario "Game Survival" dengan nama `app.py` kemudian simpan code script di folder `code/app.py`
2. Membuat file `Dockerfile` menggunakan base image python terbaru `python:3.11.14-alpine3.23` kemudian simpan code di folder `code/Dockerfile`
   
### C. Build Image
1. Melakukan proses build image dari Dockerfile dengan nama tag `week13-resource-limit`.
2. Screenshots output terminal dari hasil proses build kemudian simpan di folder `screenshots/docker-build.png`

### D. Tahap Pengujian
1. Menjalankan container secara normal tanpa batasan resource untuk membuktikan bahwa program dapat berjalan hingga selesai (mencapai target 500MB) jika sumber daya mencukupi.
2. Screenshots hasilnya kemudian simpan file tersebut di folder `screenshots/docker-limited.png`.
3. Menjalankan container dengan batasan memori 256MB (`--memory="256m"`). Mengamati perilaku program yang terhenti di tengah jalan  karena kehabisan memori.
4. Screenshots hasilnya kemudian simpan file tersebut di folder `screenshots/docker-256mb.png`.

### E. Monitoring Sederhana
1. Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
2. Screenshot output eksekusi dan/atau `docker stats`.

### F. Commit & Push

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```

---

## Kode / Perintah
### 1. Struktur File
```
praktikum/week13-docker-resource-limit/
├─ code/
│  ├─ app.py
│  └─ Dockerfile
├─ screenshots/
│  ├─ docker-256mb.png
|  ├─ docker-build.png
|  └─ docker-limited.png
└─ laporan.md
```


---

## Hasil Eksekusi
1.Proses instalasi Docker Desktop pada sistem operasi Windows.

<img width="1920" height="1080" alt="Screenshot 2026-01-11 120841" src="https://github.com/user-attachments/assets/1127b670-43e2-4375-bc3b-6d18a3daeba5" />
<img width="1920" height="1080" alt="Screenshot 2026-01-11 120947" src="https://github.com/user-attachments/assets/b8df1bfc-81ad-4a2c-9e12-42015b7ed146" />
<img width="1199" height="747" alt="Screenshot 2026-01-11 130441" src="https://github.com/user-attachments/assets/21f4461a-3d97-436e-9b9b-858d5b1d102e" />
<img width="1920" height="1080" alt="Screenshot 2026-01-11 130711" src="https://github.com/user-attachments/assets/da4a7475-2b18-482b-83db-e79ebb3cab24" />

2.# Laporan Praktikum Week 13 – Docker Resource Limit

## Screenshot 1 – Run Container Tanpa Limit
<img width="583" height="503" alt="Screenshot 2026-01-11 213543" src="https://github.com/user-attachments/assets/82540ee4-5c62-4dc6-964f-ac764fb51446" />


**Penjelasan:**

Container dijalankan tanpa batasan resource menggunakan perintah:
```bash
docker run --rm week13-resource-limit

```


2.Container dijalankan dengan batasan CPU dan memori menggunakan perintah:
```
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```

<img width="502" height="444" alt="Screenshot 2026-01-11 213918" src="https://github.com/user-attachments/assets/7c76976a-13d0-417d-a894-f3ed8a119398" />

CPU dibatasi hanya menggunakan 0.5 core, sehingga proses komputasi berjalan lebih lambat dibandingkan tanpa limit.

Memori dibatasi maksimal 256 MB, sehingga program berhenti/error ketika alokasi melebihi kapasitas.

Perilaku ini menunjukkan bahwa resource limit benar‑benar diterapkan dan mempengaruhi performa aplikasi di dalam container.

3.Monitoring dilakukan dengan perintah:
```
docker stats

```
<img width="1369" height="292" alt="Screenshot 2026-01-11 214046" src="https://github.com/user-attachments/assets/4d82dc0a-0e60-4d21-81d7-fbe5a0f8be81" />


Output menampilkan penggunaan CPU, memori, dan I/O container secara real‑time.
Terlihat bahwa CPU tidak melebihi 0.5 core dan memori tidak melebihi 256 MB.
Monitoring ini menjadi bukti visual bahwa limit bekerja sesuai konfigurasi.

## Analisis
## Hasil Pengamatan

| Tahap Eksekusi                  | Perintah                                                                 | Hasil/Output                                                                 | Analisis                                                                 |
|---------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Run Container Tanpa Limit       | `docker run --rm week13-resource-limit`                                   | Program berjalan normal, iterasi memori terus bertambah hingga target tercapai | Container bebas menggunakan resource host, performa maksimal tanpa kendala |
| Run Container Dengan Limit      | `docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit`      | Program lebih lambat, berhenti/error saat memori melebihi 256 MB              | CPU throttling terlihat, OOM Killer aktif saat memori habis               |
| Monitoring Resource dengan Stats| `docker stats`                                                            | Output menunjukkan CPU ≤ 0.5 core, memori ≤ 256 MB                           | Bukti visual bahwa limit resource diterapkan sesuai konfigurasi           |

---

## Kesimpulan
Berdasarkan praktikum ini, dapat disimpulkan bahwa :
1. Docker secara default mengizinkan container menggunakan sumber daya host secara penuh yang dibuktikan dengan keberhasilan program mencapai target maksimal tanpa kendala. Namun, saat limitasi memori 256MB diterapkan, program terhenti lebih cepat dari perhitungan matematis akibat adanya konsumsi memori tambahan oleh sistem operasi dan runtime Python di dalam container.
2. Mekanisme OOM Killer bekerja efektif mematikan proses yang melanggar batas memori demi menjaga stabilitas sistem utama. 
3. Pengaturan swap memori terbukti sangat krusial karena harus disesuaikan dengan batas RAM agar aplikasi tidak beralih menggunakan disk saat memori fisik habis, sehingga simulasi pembatasan sumber daya menjadi akurat.
---

## Quiz
**1. Mengapa container perlu dibatasi CPU dan memori?**

   **Jawaban**

   * Penerapan batasan (limits) pada CPU dan memori dalam lingkungan kontainerisasi sangat krusial untuk menjamin stabilitas, efisiensi, dan reliabilitas infrastruktur komputasi awan. Secara teknis, mekanisme ini umumnya diimplementasikan menggunakan fitur kernel Linux, yaitu Control Groups (cgroups), untuk membatasi, menghitung, dan mengisolasi penggunaan sumber daya. 

**2. Apa perbedaan VM dan container dalam konteks isolasi resource?**

   **Jawaban**

   * **VM (Virtual Machine):** Isolasi dilakukan di level Hardware. VM memiliki kernel dan OS sendiri yang terpisah total. Sangat aman, tapi berat (memakan RAM statis besar).
   * **Container:** Isolasi dilakukan di level OS (menggunakan Namespaces & Cgroups). Semua container berbagi kernel milik Host. Lebih ringan dan efisien, namun isolasinya tidak sekompleks VM.

**3. Apa dampak limit memori terhadap aplikasi yang boros memori?**

   **Jawaban**

   * **Jika Swap Aktif:** Aplikasi akan menjadi sangat lambat (*thrashing*) karena sistem sibuk memindahkan data dari RAM ke Disk.
   * **Jika Swap Mati/Penuh:** Aplikasi akan langsung dimatikan paksa oleh sistem (*OOM Killed*), menyebabkan layanan down tiba-tiba.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

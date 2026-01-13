
# Laporan Praktikum Minggu [X]
Topik:  Virtualisasi Menggunakan Virtual Machine  


---

## Identitas
- **Nama**  : Zaki Humam Faradi  
- **NIM**   : 250202972 
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).  
2. Membuat dan menjalankan sistem operasi guest di dalam VM.  
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).  
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.  
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---
---

## Dasar Teori
1.  **Virtualisasi (Virtualization)**
   
    Virtualisasi adalah teknologi yang memungkinkan satu komputer fisik (Host) untuk menjalankan beberapa sistem operasi (Guest) secara bersamaan dengan membagi sumber daya *hardware* secara efisien. Ini menciptakan lapisan abstraksi antara *hardware* fisik dan sistem operasi.

2.  **VirtualBox**
   
    VirtualBox adalah perangkat lunak virtualisasi yang memungkinkan pengguna menciptakan mesin virtual untuk menjalankan satu atau lebih sistem operasi tambahan secara bersamaan di dalam satu komputer fisik. Fungsi utamanya adalah menyediakan lingkungan terisolasi untuk menguji perangkat lunak, mempelajari instalasi sistem operasi yang berbeda (seperti Linux di dalam Windows), serta memfasilitasi pengembangan aplikasi lintas platform tanpa risiko merusak sistem operasi utama.

3.  **Host OS vs Guest OS**
    * **Host OS:** Sistem operasi fisik yang menjalankan komputer (Windows 11).
    * **Guest OS:** Sistem operasi virtual yang berjalan di dalam *container* virtual (Ubuntu Linux).

4.  **Isolasi Resource & Sandboxing**
   
    Virtualisasi menyediakan mekanisme keamanan di mana kerusakan pada Guest OS (misalnya terkena virus atau *crash*) tidak akan memengaruhi Host OS. Setiap VM berjalan dalam lingkungan terisolasi (*sandbox*) yang memiliki jatah CPU dan RAM sendiri.

---

## Langkah Praktikum

Saya memilih untuk menjalankan Virtual OS Linux Ubuntu 24.04 LTS Dekstop, maka dari itu langkah praktikum sebagai berikut :


### A. Persiapan & Instalasi
1.  Mengunduh file ISO **Ubuntu 24.04 Desktop** dan aplikasi **Oracle VirtualBox**.
    -  **Ubuntu 24.04 Desktop** : https://ubuntu.com/download/desktop
    -  **Oracle VirtualBox** : https://download.virtualbox.org/virtualbox/7.2.4/VirtualBox-7.2.4-170995-Win.exe
2.  Menginstal VirtualBox pada Dekstop (Host OS).

### B. Konfigurasi Awal (High Resource)
1.  Membuat Virtual Machine baru dengan nama `Linux-Ubuntu`.
2.  Mengatur spesifikasi awal VM:
    * **RAM:** 4096 MB (4 GB).
    * **CPU:** 2 Core.
3.  Menjalankan VM dan menunggu proses instalasi Ubuntu selesai hingga masuk ke desktop.

### C. Eksperimen VM Linux Ubuntu 24.04 LTS
1.  Setelah Konfigurasi selesai, klik open untuk membuka Virtual Machine
2.  Membuka **Terminal** dan menjalankan perintah dasar untuk mengecek spesifikasi sistem.
3.  Membuka aplikasi **Firefox** dan memutar video YouTube serta membuka 5 tab sekaligus untuk memberikan beban kerja (*stress test*).
4.  Membuka **System Monitor** untuk memantau grafik penggunaan RAM dan CPU saat beban tinggi.

### D. Eksperimen VM Mengurangi Resource
1.  Mematikan VM (*Shutdown*).
2.  Masuk ke menu **Settings > System** di VirtualBox.
3.  Menurunkan alokasi resource menjadi:
    * **RAM:** 2048 MB (2 GB).
    * **CPU:** 1 Core.
4.  Menyalakan kembali VM dan mengulangi pengujian dengan membuka Firefox.
5.  Mengamati terjadinya penurunan performa (*lag*) dan peningkatan penggunaan memori hingga mendekati batas maksimal.

### E. Analisis dan Dokumentasi
1. Mencatat proses praktikum dari awal persiapan hingga akhir.
2. Screenshot hasil instalasi virtual box kemudian simpan di `screenshors/instalasi_vm.png`
3. Screenshot hasil konfigurasi Virtual Machine Linux Ubuntu 24.04 LTS dan simpan di `screenshots/konfigurasi_resource.png`
4. Screenshot hasil eksperimen di OS Guest dan simpan di `screenshots/os_guest_running.png`
5. Mencatat konfigurasi Spesifikasi Host OS dan Spefisikasi Guest OS kemudian simpan di code/`catatan_konfigurasi`

### F. Commit & Push
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
   git push origin main
   ```

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

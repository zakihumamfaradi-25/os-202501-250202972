
# Laporan Praktikum Minggu [X]
Topik:Arsitektur dan Sistem Operasi 

---

## Identitas
- **Nama**  : Zaki Humam Faradi 
- **NIM**   : 250202972
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan dasar-dasar arsitektur dan sistem operasi.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

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

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi
      Tiga fungsi utama sistem operasi (OS) adalah:
Manajemen Sumber Daya: Mengelola perangkat keras (CPU, memori, I/O).
Antarmuka Pengguna: Menyediakan cara bagi pengguna untuk berinteraksi dengan komputer (misalnya, melalui GUI).
Eksekusi Program: Menyediakan lingkungan untuk menjalankan aplikasi.
2.Jelaskan perbedaan antara kernel mode dan user mode.
     Berikut perbedaannya:
Kernel Mode (Istimewa): Kontrol penuh atas hardware, tempat OS berjalan. Kegagalan berarti sistem crash.
User Mode (Terbatas): Akses terbatas ke hardware, tempat aplikasi berjalan. Kegagalan hanya membuat aplikasi crash.
     
3.Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
     Monolithic Kernel:
Semua layanan inti OS berada dalam satu blok di Kernel.
Contoh: Linux, Solaris.
Microkernel:
Hanya fungsi dasar yang ada di Kernel; layanan lain berjalan terpisah di luar Kernel.
Contoh: QNX, Hurd.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
    tugas yang cukup sulit karena baru pertama kali 
- Bagaimana cara Anda mengatasinya?  
    berusaha sebaik mungkin 
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

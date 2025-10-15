
# Laporan Praktikum Minggu [X]
Topik:Arsitektur dan Sistem Operasi 

---

## Identitas
- **Nama**  : Zaki Humam Faradi 
- **NIM**   : 250202972
- **Kelas** : 1IKRA

---

## Tujuan
 
> Mahasiswa mampu menjelaskan dasar-dasar arsitektur dan sistem operasi.

---

## Dasar Teori
Sistem operasi adalah perangkat lunak yang mengontrol dan mengatur perangkat keras komputer serta menjalankan program aplikasi. Sistem ini bertindak sebagai penghubung antara pengguna dengan perangkat keras (system call), memungkinkan komputer berfungsi dan program dapat berjalan dengan baik, dengan bagian terpenting nya adalah kernel yang mengelolah sumber daya CPU,Memory,Storage (hardisk) dan I/O

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

<img width="1184" height="665" alt="zaki" src="https://github.com/user-attachments/assets/aab71dcc-d2c3-4de5-b261-c2afad4d3e7f" />


---

## Analisis
- uname -a adalah perintah di Linux yang digunakan untuk menampilkan semua informasi detail tentang sistem, termasuk nama kernel, nama mesin.

Perintah 1smod digunakan untuk menampilkan daftar modul kernel yang saat ini sedang dimuat (loaded) di sistem.

Modul kernel ini bisa berupa driver perangkat keras atau modul fungsional lainnya yang digunakan oleh kernel Linux Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).

Hubungkan hasil dengan teori

Hasil dapat dihubungkan dengan fungsi kernel sebagai inti sistem operasi yang menjembatani hardware dan software; panggilan sistem (\(syscall\)) sebagai jembatan antara aplikasi pengguna dan kernel untuk meminta layanan; dan arsitektur OS yang mendefinisikan struktur ini, di mana kernel menjadi komponen sentral yang mengelola sumber daya melalui panggilan sistem.

Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?

Perbedaan hasil antara Linux dan Windows terlihat dari struktur sistem file (garis miring / di Linux vs "C:\ di Windows), cara penamaan berkas (bisa ada dua berkas dengan nama sama di direktori berbeda di Linux, tidak bisa di Windows), sistem partisi (Linux lebih fleksibel, Windows mendukung partisi Linux namun Linux belum tentu mendukung partisi Windows), dan penggunaan baris perintah (terminal di Linux lebih ampuh, cmd di Windows lebih terbatas).

---

## Kesimpulan

Monolithic kernel adalah arsitektur sistem operasi di mana semua layanan inti OS, seperti manajemen memori, penjadwalan proses, dan manajemen perangkat keras, berjalan dalam satu ruang alamat (satu program besar) bagian dapat menyebabkan crash seluruh. Mikrokernel adalah jenis kernel sistem operasi yang hanya berisi fungsionalitas inti minimal, seperti manajemen memori dan komunikasi antarproses (IPC), sementara layanan lainnya (seperti driver perangkat dan sistem berkas) berjalan di ruang pengguna Arsitektur berlapis (layered architecture) adalah pola desain perangkat lunak yang membagi aplikasi menjadi beberapa lapisan terpisah, di mana setiap lapisan memiliki tanggung jawab tertentu dan hanya berinteraksi dengan lapisan di bawahnya, sebagai server terpisah.

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

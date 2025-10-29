
# Laporan Praktikum Minggu [X]
Topik: PROSES USER

---

## Identitas
- **Nama**  : Zaki Humam Faradi 
- **NIM**   : 250202972
- **Kelas** : 1ikra

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.  

---

## Dasar Teori
1. Definisi Proses User
- Proses user adalah program yang dijalankan dalam mode pengguna (user mode), yaitu lingkungan terbatas yang tidak memiliki akses langsung ke sumber daya kernel untuk menjaga keamanan sistem.

2. Pemrosesan oleh Sistem Operasi
- Sistem operasi bertanggung jawab untuk membuat, mengatur, dan menghapus proses user menggunakan Process Control Block (PCB) yang menyimpan informasi penting seperti status, prioritas, dan konteks eksekusi.

3. Transisi User–Kernel Mode
- Saat proses user membutuhkan layanan sistem (misalnya akses file, memori, atau perangkat keras), terjadi transisi ke mode kernel melalui system call. Setelah selesai, kontrol dikembalikan ke mode user.

4. Isolasi dan Keamanan
- Proses user diisolasi satu sama lain agar tidak saling mengganggu. OS menggunakan proteksi memori dan kontrol hak akses untuk mencegah pelanggaran keamanan antar proses.

5. Manajemen Multitasking
- Beberapa proses user dapat dijalankan secara bersamaan melalui penjadwalan CPU (scheduling), memungkinkan sistem mendukung multitasking secara efisien tanpa konflik sumber daya.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
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
 eksperimen 1 : Jelaskan setiap output dan fungsinya.(whoami,id,groups)
3. eksperimen 2 : Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
4. eksperimen 3 : Catat PID proses sleep
5. eksperimen 4 : Amati hierarki proses dan identifikasi proses induk (init/systemd).

**JAWAB** 
1. - Whoami Menampilkan nama user yang sedang login atau menjalankan terminal saat ini.Output evelin berarti user aktif saat ini bernama evelin.Perintah ini berguna untuk mengecek identitas user yang sedang digunakan, terutama setelah berpindah ke user lain menggunakan sudo.
   -id Menampilkan informasi lengkap tentang identitas user, termasuk UID (User ID),GID (Group ID),dan daftar grup yang diikuti oleh user.id memberikan informasi identitas lengkap user dalam bentuk angka (ID) dan nama (label).
   - groups Menampilkan semua grup yang diikuti oleh user yang sedang aktif. groups menampilkan daftar keanggotaan grup user, yang menentukan hak akses dan izin terhadap file atau perangkat.

2. - PID adalah nomor identitas unik untuk setiap proses yang sedang berjalan di sistem.
   - USER yaitu nama pengguna (user) yang menjalankan proses tersebut.
   - %CPU adalah Persentase penggunaan CPU oleh proses tersebut.
   - %MEM adalah Persentase penggunaan memori fisik (RAM) oleh proses
   - COMMAND adalah Perintah atau nama program yang dijalankan oleh proses.
3. - zaki       710  0.0  0.0   3124  1664 pts/0    S    16:44   0:00 sleep 1000
- zaki       712  0.0  0.0   4088  1920 pts/0    S+   16:45   0:00 grep --color=auto sleep

4. - Analisis hierarki proses
Proses paling atas (induk utama) adalah systemd(1), dengan PID 1.Semua proses lain seperti cron, dbus-daemon, rsyslogd, dan login merupakan proses turunan (child process) dari systemd.Proses seperti bash, head, dan pstree merupakan proses anak dari sesi login user (login atau bash).

- Proses induk utama sistem adalah:systemd (PID 1)
- Fungsinya:
1. Menginisialisasi sistem saat booting.
2. Menjalankan dan memonitor seluruh proses sistem.
3. Mengatur layanan (services) dan sesi pengguna.


---

## Kesimpulan
1. Setiap proses di Linux dijalankan oleh user tertentu dan memiliki identitas unik berupa PID (Process ID) yang digunakan sistem untuk mengelola, memantau, atau menghentikan proses tersebut.

2. User dan hak aksesnya menentukan kendali terhadap proses. Hanya user pemilik proses atau root yang dapat memodifikasi atau menghentikan proses tersebut.

3. Perintah seperti whoami, id, dan ps aux membantu mengenali identitas user dan proses yang sedang berjalan, sehingga memudahkan administrasi dan pengawasan sistem.


---

### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.  
2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.  
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.  
4. Upload laporan- whoami


**JAWAB** 


1. - id
Menampilkan identitas user (uid, gid) dan grup-grup yang diikutinya.

- groups
Menunjukkan daftar grup tempat user evelin tergabung, seperti sudo, adm, dan lainnya.

- sudo adduser praktikan
Menambahkan akun baru bernama praktikan ke sistem beserta home directory-nya.

- sudo passwd praktikan
Mengatur atau mengganti password untuk user praktikan.

- ps aux | head -10
Melihat daftar proses yang sedang berjalan di sistem, ditampilkan 10 baris pertama.

- top -n 1
Menampilkan penggunaan CPU, memori, dan daftar proses aktif saat ini (snapshot sekali).

- sleep 1000 &
Menjalankan proses sleep selama 1000 detik di background.

- ps aux | grep sleep
Mengecek apakah proses sleep masih berjalan dengan mencari berdasarkan nama.

- kill 710
Menghentikan proses sleep dengan PID 710.

- pstree -p | head -20
Menampilkan struktur hierarki proses dalam bentuk pohon, dengan systemd(1) sebagai induk utama. ke repositori Git tepat waktu.

2.  <img width="3756" height="1072" alt="diagram pohon" src="https://github.com/user-attachments/assets/8ec3ec06-e5c6-4a6c-bde0-59e68cc1b436" />

3. Hubungan antara user management dan keamanan sistem Linux sangat erat, karena pengelolaan pengguna adalah salah satu cara utama untuk mengontrol akses dan melindungi sistem dari penyalahgunaan.User management adalah fondasi utama keamanan Linux.
Dengan mengatur akun, hak akses, dan izin secara tepat, sistem dapat mencegah pelanggaran keamanan, membatasi dampak kesalahan manusia, dan menjaga integritas serta stabilitas sistem



## Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?  
2. Apa perbedaan antara `kill` dan `killall`?  
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?

**JAWAB**  
1. Fungsi dari proses init atau systemd dalam sistem Linux
- Menginisialisasi sistem setelah boot — menyiapkan lingkungan kerja, memeriksa file system, dan memulai service penting.
- Menjalankan dan mengatur proses background (daemon) seperti jaringan, logging, atau cron.
- Mengatur urutan start/stop service berdasarkan dependensi.
- Memantau dan menghidupkan ulang service jika terjadi kegagalan.

2.
- kill digunakan untuk menghentikan proses tertentu berdasarkan PID (Process ID).
Misalnya, jika kamu tahu proses dengan PID 1234 sedang berjalan
- killall digunakan untuk menghentikan semua proses yang memiliki nama tertentu.

3. Karena User root memiliki hak istimewa karena dibutuhkan untuk mengelola, mengamankan, dan memelihara sistem Linux secara penuh, sementara user biasa dibatasi agar sistem tetap stabil dan aman
   
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  pemahaman konsep dasar sistem Linux dan interpretasi hasil perintah secara logis
- Bagaimana cara Anda mengatasinya?  Belajar memahami konsep dasar dulu sebelum praktik,Diskusi dan latihan bersama teman

---


**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

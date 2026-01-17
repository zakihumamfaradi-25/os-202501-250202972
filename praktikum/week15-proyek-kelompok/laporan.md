# Laporan Proyek Kelompok  
## Mini Simulasi Sistem Operasi

---

## 1. Pendahuluan

### A. Latar Belakang

Sistem operasi merupakan perangkat lunak sistem yang berperan penting dalam mengelola sumber daya perangkat keras dan perangkat lunak komputer, serta bertindak sebagai perantara antara pengguna dan perangkat keras. Di dalam sistem operasi terdapat berbagai konsep fundamental, seperti **penjadwalan proses (CPU Scheduling)** dan **manajemen memori (Memory Management)**, yang menjadi dasar dalam pengoperasian sistem secara efisien.

Namun, konsep-konsep tersebut sering kali bersifat abstrak dan sulit dipahami apabila hanya dipelajari melalui teori. Tanpa adanya visualisasi atau simulasi, mahasiswa kerap mengalami kesulitan dalam memahami bagaimana sistem operasi mengambil keputusan, seperti menentukan urutan eksekusi proses atau mengganti halaman memori ketika kapasitas terbatas. Oleh karena itu, diperlukan suatu pendekatan praktis yang mampu merepresentasikan konsep sistem operasi secara sederhana dan mudah dipahami.

Proyek ini, yang berjudul **“Mini Simulasi Sistem Operasi”**, dikembangkan sebagai upaya untuk mengintegrasikan berbagai materi praktikum sistem operasi ke dalam sebuah aplikasi simulasi berbasis terminal. Aplikasi ini dirancang untuk mensimulasikan cara kerja sistem operasi melalui analogi aktivitas sehari-hari, sehingga konsep yang kompleks dapat dipahami dengan lebih intuitif.

Dalam proyek ini, diimplementasikan dua modul utama, yaitu:

1. **Simulasi Download Manager**, yang merepresentasikan algoritma penjadwalan CPU **First-Come First-Served (FCFS)**. Pada simulasi ini, berkas yang pertama kali diminta untuk diunduh akan diproses hingga selesai sebelum sistem melanjutkan ke berkas berikutnya, sesuai dengan prinsip kerja algoritma FCFS.

2. **Simulasi RAM pada Perangkat Mobile**, yang memodelkan algoritma **Page Replacement First-In First-Out (FIFO)**. Simulasi ini menggambarkan bagaimana sistem operasi pada ponsel pintar mengelola memori, di mana aplikasi yang paling lama berada di dalam memori akan dikeluarkan terlebih dahulu ketika kapasitas RAM telah penuh dan pengguna membuka aplikasi baru.

Selain fokus pada implementasi konsep sistem operasi, proyek ini juga menerapkan prinsip rekayasa perangkat lunak modern, seperti penggunaan **Git** untuk pengelolaan kode sumber secara kolaboratif serta **Docker** untuk menciptakan lingkungan eksekusi yang konsisten dan dapat dijalankan di berbagai sistem operasi.

---

### B. Tujuan Proyek

Berdasarkan deskripsi tugas Praktikum Sistem Operasi Minggu ke-15, tujuan dari pelaksanaan proyek **Mini Simulasi Sistem Operasi** ini adalah sebagai berikut:

1. Mahasiswa mampu bekerja secara kolaboratif dalam sebuah tim dengan pembagian peran yang jelas dan terstruktur, seperti **Project Leader**, **Developer**, dan **Documentation/Quality Assurance**.
2. Mahasiswa mampu mengimplementasikan serta mengintegrasikan minimal dua konsep utama sistem operasi, yaitu **penjadwalan CPU** dan **manajemen memori**, ke dalam satu aplikasi simulasi yang terpadu.
3. Mahasiswa mampu menerapkan pengelolaan kode sumber (*source control*) menggunakan **Git**, termasuk penggunaan *branching*, *commit*, dan *merge/pull request* secara sistematis dan terorganisir.
4. Mahasiswa mampu membungkus aplikasi ke dalam **container Docker**, sehingga aplikasi dapat dijalankan secara konsisten tanpa bergantung pada perbedaan lingkungan sistem operasi.
5. Mahasiswa mampu menyusun laporan teknis proyek secara sistematis serta melakukan analisis terhadap hasil simulasi untuk menunjukkan pemahaman konsep sistem operasi secara komprehensif.

---

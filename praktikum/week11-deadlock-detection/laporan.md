
# Laporan Praktikum Minggu [11]
Topik:Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Zaki Humam Faradi  
- **NIM**   : 250202972
- **Kelas** : 1IKRA

---

## Tujuan
1. Membuat program sederhana untuk mendeteksi deadlock.
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.
4. Memberikan interpretasi hasil uji secara logis dan sistematis.
5. Menyusun laporan praktikum sesuai format yang ditentukan.


---

## Dasar Teori
1. Definisi Deadlock: Kondisi di mana sekumpulan proses saling menunggu sumber daya secara permanen sehingga eksekusi terhenti total.

2. Kondisi Coffman: Deadlock hanya terjadi jika empat syarat terpenuhi serentak: Mutual Exclusion, Hold and Wait, No Preemption, dan Circular Wait.

3. Deteksi & RAG: Identifikasi dilakukan menggunakan Resource Allocation Graph (RAG); jika terdapat siklus (cycle) dalam graf alokasi tersebut, maka sistem terdeteksi mengalami deadlock.

---

## Langkah Praktikum
## Langkah Praktikum
1. Menyiapkan Dataset Gunakan dataset sederhana yang berisi:
Daftar proses
Resource Allocation
Resource Request / Need
2. Implementasi Algoritma Deteksi Deadlock
Program minimal harus:
Membaca data proses dan resource.
Menentukan apakah sistem berada dalam kondisi deadlock.
Menampilkan proses mana saja yang terlibat deadlock.
3. Eksekusi & Validasi
Jalankan program dengan dataset uji.
Validasi hasil deteksi dengan analisis manual/logis.
Simpan hasil eksekusi dalam bentuk screenshot.
4. Analisis Hasil
Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).
Jelaskan mengapa deadlock terjadi atau tidak terjadi.
Kaitkan hasil dengan teori deadlock (empat kondisi).
5. Commit & Push
git add .
git commit -m "Minggu 11 - Deadlock Detection"
git push origin main



---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
praktikum/week11-deadlock-detection/
├─ code/
│  ├─ deadlock_detection.*
│  └─ dataset_deadlock.csv
├─ screenshots/
│  └─ hasil_deteksi.png
└─ laporan.md
```

---

## Hasil Eksekusi

<img width="1920" height="1080" alt="Screenshot 2026-01-04 212931" src="https://github.com/user-attachments/assets/342d6bda-d926-460b-9ca3-6c9b3279c544" />



## Analisis
## Hasil Deteksi Deadlock

### 1. Tabel Hasil Deteksi

Berdasarkan hasil eksekusi algoritma deteksi deadlock menggunakan *Wait-For Graph*, diperoleh hasil sebagai berikut:

| Proses | Status |
|:--:|:--:|
| P1 | Terlibat Deadlock |
| P2 | Terlibat Deadlock |
| P3 | Terlibat Deadlock |

**Kesimpulan sistem:**  
Sistem berada dalam kondisi **deadlock**.

---

### 2. Penjelasan Terjadinya Deadlock

Dataset yang digunakan:

| Proses | Allocation | Request |
|:--:|:--:|:--:|
| P1 | R1 | R2 |
| P2 | R2 | R3 |
| P3 | R3 | R1 |

Analisis:
- Proses **P1** memegang resource **R1** dan menunggu **R2** yang sedang dipegang oleh **P2**
- Proses **P2** memegang resource **R2** dan menunggu **R3** yang sedang dipegang oleh **P3**
- Proses **P3** memegang resource **R3** dan menunggu **R1** yang sedang dipegang oleh **P1**

Hubungan tunggu yang terbentuk adalah:

P1 → P2 → P3 → P1


Hubungan tersebut membentuk **siklus (circular wait)**, sehingga tidak ada proses yang dapat melanjutkan eksekusi. Akibatnya, sistem mengalami deadlock.

---

### 3. Kaitan dengan Teori Deadlock (Empat Kondisi Coffman)

Deadlock terjadi apabila keempat kondisi berikut terpenuhi secara bersamaan:

1. **Mutual Exclusion**  
   Setiap resource hanya dapat digunakan oleh satu proses pada satu waktu.  
   ✔️ Terpenuhi

2. **Hold and Wait**  
   Proses menahan resource yang dimiliki sambil menunggu resource lain.  
   ✔️ Terpenuhi

3. **No Preemption**  
   Resource tidak dapat direbut secara paksa dan hanya dilepas oleh proses yang memegangnya.  
   ✔️ Terpenuhi

4. **Circular Wait**  
   Terdapat siklus proses yang saling menunggu resource.  
   ✔️ Terpenuhi

Karena keempat kondisi Coffman terpenuhi, maka sistem **pasti mengalami deadlock**.

---

### 4. Kesimpulan

Berdasarkan hasil simulasi dan analisis menggunakan algoritma *Wait-For Graph*, sistem terdeteksi berada dalam kondisi deadlock. Semua proses (P1, P2, dan P3) terlibat dalam deadlock akibat adanya siklus ketergantungan resource. Kondisi ini sesuai dengan teori deadlock Coffman, di mana seluruh syarat deadlock terpenuhi secara bersamaan.



---

## Quiz
## 1. Perbedaan Deadlock Prevention, Avoidance, dan Detection

### a. Deadlock Prevention
Deadlock prevention adalah pendekatan yang bertujuan **mencegah deadlock sejak awal** dengan memastikan bahwa **setidaknya satu dari empat kondisi deadlock (Coffman) tidak pernah terpenuhi**.

Ciri utama:
- Sistem membatasi cara proses meminta atau memegang resource
- Contoh: melarang *hold and wait* atau menerapkan urutan pengambilan resource

Kelebihan:
- Deadlock **tidak mungkin terjadi**
- Sistem lebih aman

Kekurangan:
- Kurang fleksibel
- Dapat menurunkan efisiensi penggunaan resource

---

### b. Deadlock Avoidance
Deadlock avoidance adalah pendekatan yang **menghindari kondisi deadlock saat runtime** dengan cara **menganalisis setiap permintaan resource** dan hanya mengabulkannya jika sistem tetap berada dalam *safe state*.

Ciri utama:
- Membutuhkan informasi kebutuhan resource di masa depan
- Contoh algoritma: **Banker’s Algorithm**

Kelebihan:
- Lebih fleksibel dibanding prevention
- Resource dimanfaatkan lebih optimal

Kekurangan:
- Membutuhkan informasi maksimum kebutuhan proses
- Overhead komputasi lebih tinggi

---

### c. Deadlock Detection
Deadlock detection adalah pendekatan yang **membiarkan deadlock terjadi**, lalu **mendeteksinya menggunakan algoritma tertentu**, kemudian melakukan pemulihan.

Ciri utama:
- Tidak membatasi permintaan resource
- Deadlock dideteksi setelah terjadi
- Contoh: **Wait-For Graph**

Kelebihan:
- Paling fleksibel
- Pemanfaatan resource tinggi

Kekurangan:
- Deadlock tetap bisa terjadi
- Membutuhkan mekanisme pemulihan

---

## 2. Alasan Deteksi Deadlock Tetap Diperlukan dalam Sistem Operasi

Deteksi deadlock tetap diperlukan karena tidak semua sistem dapat menerapkan prevention atau avoidance secara efektif.

Beberapa alasannya:
- Tidak semua kebutuhan resource proses dapat diprediksi di awal
- Pembatasan ketat dapat menurunkan kinerja sistem
- Sistem modern bersifat dinamis dan kompleks
- Deadlock jarang terjadi, sehingga lebih efisien mendeteksi daripada mencegah terus-menerus

Dengan deteksi deadlock, sistem dapat:
- Memberikan fleksibilitas tinggi kepada proses
- Mengoptimalkan pemanfaatan resource
- Menangani deadlock hanya saat benar-benar terjadi

---

## 3. Kelebihan dan Kekurangan Pendekatan Deteksi Deadlock

### Kelebihan Deteksi Deadlock
- Tidak membatasi permintaan resource proses
- Utilisasi resource lebih optimal
- Cocok untuk sistem dengan beban kerja dinamis
- Implementasi relatif sederhana untuk sistem kecil–menengah

### Kekurangan Deteksi Deadlock
- Deadlock tetap dapat terjadi
- Membutuhkan mekanisme pemulihan (terminasi proses atau preemption)
- Deteksi memerlukan overhead komputasi
- Pemulihan deadlock dapat menyebabkan hilangnya data atau proses harus diulang

---


  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

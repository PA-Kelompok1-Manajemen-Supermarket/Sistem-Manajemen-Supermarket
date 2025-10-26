# PA-SISTEM-MANAJEMEN-SUPERMARKET
Project Akhir Kelompok 01 - Sistem Informasi C'2025
- Khairul Ikhsan (2509116097)
- Ahmad Ribbiy Aldi (2509116100)
- Charist Evlyn Myscha Rerung (2509116102)
- Qonitah Khansa' Ayu Madani Alamsyah (2509116113)
  
---

## FLOWCHART
###  **Menu Utama**
![PADDP-Menu Utama](https://github.com/user-attachments/assets/181891bc-2009-483b-a539-b3a10b896f50)

Flowchart sistem login dan registrasi ini menggambarkan alur pengguna dari tampilan awal hingga masuk ke menu utama. Pengguna dapat memilih untuk login, registrasi, atau keluar dari sistem. Saat login, sistem akan memverifikasi username dan password untuk menentukan akses sebagai admin atau customer. Jika data tidak valid, muncul pesan kesalahan, sedangkan pada registrasi akun baru akan disimpan dan pengguna kembali ke menu utama.

---

### **Menu Admin**
![PADDP-Menu Admin](https://github.com/user-attachments/assets/00184d55-976f-43c8-9db9-549c0d5c6f63)
Flowchart menu admin menggambarkan alur kerja fitur yang digunakan oleh admin untuk mengelola data produk dalam sistem. Melalui menu ini, admin dapat menambahkan produk baru, melihat daftar produk yang tersedia, memperbarui informasi produk, menghapus produk yang tidak diperlukan, serta keluar (logout) dari sistem. Setiap proses memiliki tahapan validasi untuk memastikan data yang dikelola benar dan tidak terjadi duplikasi atau kesalahan input.
📋 Deskripsi Alur

---

**Tambah Produk**
- Admin memilih opsi tambah produk.
        
- Sistem meminta input berupa kode, nama, harga, dan stok produk.
        
- Sistem memeriksa apakah kode produk sudah ada dan apakah data yang dimasukkan valid.
        
- Jika valid, data produk disimpan dan muncul pesan “Produk berhasil ditambahkan”.
        
\
**Lihat Produk**
- Admin memilih opsi lihat produk.
- Sistem mengakses data produk dan menampilkan seluruh produk yang tersedia.
  
**Update Produk**
- Admin memilih opsi update produk.
- Sistem meminta kode produk yang ingin diperbarui.
- Jika kode ditemukan dan valid, admin dapat mengubah nama, harga, atau stok produk.
- Setelah data disimpan, sistem menampilkan pesan “Data produk berhasil diupdate”.

**Hapus Produk**
- Admin memilih opsi hapus produk.
- Sistem meminta kode produk yang akan dihapus dan memverifikasi kodenya.
- Jika valid, sistem meminta konfirmasi penghapusan.
- Jika dikonfirmasi, produk dihapus dan muncul pesan “Produk berhasil dihapus”.

**Logout**
- Admin memilih logout untuk keluar dari menu admin.
- Sistem akan mengembalikan admin ke menu utama.

---

### Menu Pembeli
![PADDP-Menu Pembeli](https://github.com/user-attachments/assets/254f922f-b537-4536-b07d-7ae9e650961f)
Flowchart menu pembeli menggambarkan alur aktivitas pengguna saat melakukan transaksi pembelian produk. Melalui menu ini, pembeli dapat melihat daftar produk, membeli produk, mengecek saldo, melakukan top up saldo, serta keluar dari sistem. Setiap proses memiliki tahap validasi agar transaksi berjalan dengan benar dan saldo pengguna diperbarui secara otomatis.

---

**Beli Produk**

- Pembeli memilih opsi beli produk.

- Sistem menampilkan seluruh produk yang tersedia.

- Pembeli memasukkan kode produk dan jumlah yang ingin dibeli.

- Sistem menghitung total harga dan memeriksa apakah saldo mencukupi.

- Jika saldo tidak cukup, transaksi dibatalkan dengan pesan “Saldo tidak mencukupi”.

- Jika saldo mencukupi, sistem mengurangi saldo pengguna, menyimpan data transaksi, dan menampilkan pesan “Transaksi berhasil”.

**Cek Saldo**

- Pembeli memilih opsi cek saldo.

- Sistem mengakses data akun pengguna dan menampilkan informasi saldo saat ini.

**Top Up Saldo**

- Pembeli memilih opsi top up saldo.

- Sistem menampilkan daftar nominal top up (contoh: Rp50.000, Rp100.000, Rp300.000, Rp500.000).

- Pembeli memilih nominal yang diinginkan.

- Sistem menambahkan saldo sesuai pilihan dan menampilkan pesan “Saldo berhasil ditambahkan”.

- Data saldo terbaru disimpan ke sistem.

**Logout**

- Pembeli memilih logout untuk keluar dari menu pembeli.

- Sistem akan mengembalikan pengguna ke menu utama.



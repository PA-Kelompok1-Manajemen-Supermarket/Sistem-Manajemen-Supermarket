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

# PENJELASAN OUTPUT

<img width="296" height="185" alt="image" src="https://github.com/user-attachments/assets/7b84723c-6016-43e6-9633-c414e3c65595" />\
Pada saat program dijalankan, tampilan pertama yang ditampilkan program ini adalah pilihan untuk melakukan login sebagai Admin atau User. Jika memilih “1”, maka akan muncul tampilan login admin dan diminta untuk memasukkan username dan password untuk admin. Jika memilih “2”, maka akan muncul tampilan opsi register, dan jika memilih “3”, maka  akan keluar dari program

## Menu Admin
<img width="236" height="119" alt="image" src="https://github.com/user-attachments/assets/25f032e2-a810-4291-ad10-492d1ba5dc9d" />

Di menu login admin ini kita diminta untuk memasukkan username dan password untuk admin.

<img width="218" height="202" alt="image" src="https://github.com/user-attachments/assets/a7e0095f-5708-4b55-ad89-a8b4f59af347" />

Pada menu admin terdapat 5 pilihan yang bisa dipilih dan admin diminta untuk memasukkan salah satu pilihan.
- pilihan pertama, tambah barang memiliki fungsi untuk menambahkan ID produk, nama produk, harga produk dan stok produk baru.
- pilihan kedua, tampilkan barang memiliki fungsi untuk menampilkan semua barang yang ada dalam bentuk table.
- pilihan ketiga, ubah barang memiliki fungsi untuk mengubah ID produk, nama produk, harga produk dan stok produk.
- pilihan keempat, hapus barang, memiliki fungsi untuk menghapus produk yang ada di dalam data produk.
- pilihan kelima, keluar memiliki fungsi untuk keluar dari menu admin.


<img width="522" height="195" alt="image" src="https://github.com/user-attachments/assets/e7857617-cbc9-4bbe-a82c-66cb5bc61735" />\
Jika admin memilih pilihan **1**, maka admin diminta untuk menginputkan ID produk, nama produk, harga produk dan stok produk 
yang ingin ditambahkan.

<img width="698" height="342" alt="image" src="https://github.com/user-attachments/assets/5a29371f-7ced-4331-9e22-8a2900e9fc79" />

Jika admin memilih pilihan **2**, maka program akan menampilkan ID produk, nama produk, harga produk dan stok produk yang tersedia. 

<img width="654" height="406" alt="image" src="https://github.com/user-attachments/assets/5e3916a1-fde5-40d4-8fa5-80cbd53b7191" />

Jika admin memilih pilihan **3**, maka admin diminta untuk memasukkan ID  produk yang ingin diubah. lalu lanjut ke ubah nama, harga, dan stok.\
Admin bisa memilih untuk hanya mengubah salah satu atau semua data dari produk. Jika telah selesai diubah, maka data yang telah diubah akan langsung tersimpan. 

<img width="668" height="461" alt="image" src="https://github.com/user-attachments/assets/e3d2363c-4485-4797-9d2d-5b1a55f1bbc8" />\
jika admin memilih pilihan 4, maka admin diminta untuk menginput ID produk yang ingin dihapus.

<img width="467" height="396" alt="image" src="https://github.com/user-attachments/assets/1c1631e4-cea2-49b8-9f86-f278e4f863b8" />

jika admin memilih 5, maka admin akan keluar dari menu admin dan kembali pada menu awal program.

## Menu Pembeli
<img width="658" height="446" alt="image" src="https://github.com/user-attachments/assets/a8cc912e-741f-4745-9083-b6623046e7fb" />

Di dalam menu pembeli ini terdapat 4 pilihan uang dapat dipilih oleh pembeli. Pembeli akan diminta memasukkan pilihan yang diinginkan untuk menjalankan program. 

<img width="729" height="440" alt="image" src="https://github.com/user-attachments/assets/685afd65-701c-4e19-b437-55cfccf9dd5d" />

jika pembeli memilih 1, maka pembeli akan diminta untuk memasukkan ID produk dan jumlah produk yang ingin dibeli.

<img width="813" height="383" alt="image" src="https://github.com/user-attachments/assets/ae154511-0b26-4dd4-829c-570d053e8990" />
Setelah selesai memasukkan ID dan jumlah produk, maka pembeli akan diminta untuk memilih metode pembayaran yaitu e-money. Ini adalah struk belanja

<img width="481" height="101" alt="image" src="https://github.com/user-attachments/assets/2ea419dd-67c7-47dc-a357-818af7df746b" />

Jika pembeli memilih pilihan 2, maka pembeli dapat memilih pilihan jumlah saldo yang tersedia. Jika sudah memilih maka jumlah saldo e-money akan terlihat

<img width="512" height="283" alt="image" src="https://github.com/user-attachments/assets/e7ea963d-2803-4187-9f5a-e27c4e2ae8cb" />

Jika pembeli memilih pilihan 3, maka akan di tampilkan saldo yang dimiliki oleh pembeli. Kemudian pembeli akan diminta untuk memilih jumlah saldo yang ingin ditambahkan.

<img width="620" height="133" alt="image" src="https://github.com/user-attachments/assets/86700a04-3744-4c81-b70f-dcad4d0918b9" />

Jika sudah memilih maka saldo e-money telah berhasil ditambahkan ke akun pembeli.

<img width="544" height="389" alt="image" src="https://github.com/user-attachments/assets/5593c36b-4a5b-461d-8e7d-d0992cb23078" />

Jika pembeli memilih pilihan 4, maka pembeli akan keluar dari menu pembeli dan Kembali ke menu login user.

<img width="571" height="148" alt="image" src="https://github.com/user-attachments/assets/e8ad196f-f738-47ee-bc34-3015dcacf946" />

untuk mengakhiri program, maka pembeli dapat memilih pilihan 3 yaitu keluar




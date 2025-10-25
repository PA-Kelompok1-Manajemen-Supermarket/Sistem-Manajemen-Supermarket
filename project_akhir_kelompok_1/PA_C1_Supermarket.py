import csv
import pwinput
import os
from prettytable import PrettyTable
os.system("cls")


# database
users = "users.csv"
product = "product.csv"


# prettytable
etalase_produk = PrettyTable()
etalase_produk.field_names = ["ID Produk", "Nama Produk", "Harga Produk", "Stok Produk"]


# membersihkan
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# main program
def main():
    while True:
        try :
            print("""
    ===============================
    |       SELAMAT DATANG DI     |
    |           K3A MART          |
    ===============================\n""")
            table = PrettyTable()
            table.field_names = ["NO", "MENU USER"]
        
            table.add_row(["1", "LOGIN"])
            table.add_row(["2", "REGISTER"])
            table.add_row(["3", "KELUAR"])
            
            table.align["NO"] = "l"
            table.align["MENU USER"] = "l"
            print(table)
            
            pilihan = input("Masukkan pilihan (1/2/3): ")
            os.system("cls")
            
            if pilihan == "1":
                login_user()
                
            elif pilihan == "2" :
                regis()
                
            elif pilihan == "3":
                clear()
                print("""
    =======================================
    |        PROGRAM TELAH SELESAI        |
    |   Terima kasih! dan sampai jumpa :) |
    =======================================
        """)
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
    
        except KeyboardInterrupt :
                print("> PERHATIKAN INPUT")


# register 
def regis():
    clear()
    print("""
    ===========================
    |   REGISTRASI AKUN BARU  |
    ===========================
    """)

    if not os.path.exists(users):
        with open(users, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "password", "saldo", "role"])

    username = input("Masukkan Username: ").strip()
    if username == "":
        print("> Username tidak boleh kosong!")
        return
    elif len(username) < 4:
        print("> Username terlalu pendek! Minimal 4 karakter.")
        return
    elif len(username) > 12:
        print("> Username terlalu panjang! Maksimal 12 karakter.")
        return

    with open(users, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if not row:
                continue
            if row[0] == username:
                print("> Username sudah terdaftar")
                return

    password = pwinput.pwinput("Masukkan password: ", mask="*").strip()
    if password == "":
        print("> Password tidak boleh kosong!")
        return

    with open(users, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([username, password, 0, "customer"])

    clear()
    print("=" * 40)
    print("✅ Akun berhasil dibuat!")
    print(f"👤 Username : {username}")
    print("🔑 Role anda : customer")
    print("=" * 40 + "\n")


# login User
def login_user():
    clear()
    print("""
    ==============================
    |          LOGIN USER        |
    ==============================
    """)
    username = input("Masukkan Username Anda: ")
    password = pwinput.pwinput("Masukkan Password Anda: ", mask="*")

    try:
        with open(users, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None) 
            for row in csv_reader:
                if len(row) >= 4:
                    user, pw, saldo, role = row
                    if username == user and password == pw:
                        print(f"\nLogin berhasil sebagai {role}!\n")

                        if role.lower() == "admin":
                            return menu_admin()
                        elif role.lower() == "customer":
                            return menu_customer(username)
                        else:
                            print("Role tidak dikenali.")
                            return
            clear()
            print("\nUsername atau password salah.")
    except FileNotFoundError:
        print("\nFile 'users.csv' belum ditemukan")


#---------------------------------------------------------------------- CUSTOMER ---------------------------------------------------------------------------


# menu customer
def menu_customer(username):
    clear()
    
    try :
        print("""
    ==============================
    |        SELAMAT DATANG      |
    |           CUSTOMER         |
    ==============================
    """)
        while True:
            table = PrettyTable()
            table.field_names = ["NO", "MENU PEMBELI"]
            table.align["NO"] = "c"
            table.align["MENU PEMBELI"] = "l"

            table.add_row(["1", "BELI BARANG"])
            table.add_row(["2", "CEK SALDO E-MONEY"])
            table.add_row(["3", "TOP UP E-MONEY"])
            table.add_row(["4", "KELUAR"])

            print("\n========== MENU PEMBELI ==========")
            print(table)
            
            pilihan = int(input("Masukkan nomor menu yang Anda inginkan (1/2/3/4): "))

            if pilihan == 1:
                beli_barang(username)
            elif pilihan == 2:
                cek_saldo(username)
            elif pilihan == 3:
                emoney(username)
            elif pilihan == 4:
                clear()
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
    except ValueError :
        print("> PERHATIKAN INPUT")


# beli barang
def beli_barang(username):
    clear()
    tampilkan_barang()

    with open("users.csv", "r") as f:
        data_user = list(csv.reader(f))
    with open("product.csv", "r") as f:
        data_produk = list(csv.reader(f))

    user_index = None
    for i, user in enumerate(data_user):
        if user[0] == username:
            user_index = i
            break

    if user_index is None:
        print("User tidak ditemukan.")
        menu_customer(username)
        return

    saldo_user = int(data_user[user_index][2])
    if saldo_user <= 0:
        print("\n❌ Saldo Anda kosong! Silakan isi saldo terlebih dahulu sebelum berbelanja.")
        input("\nTekan Enter untuk kembali...")
        menu_customer(username)
        return

    keranjang = []

    while True:
        clear()
        tampilkan_barang()
        print(f"\nSaldo Anda: Rp {saldo_user:,}")
        id_produk = input("\nMasukkan ID produk yang ingin dibeli: ")

        produk_index = None
        for j, produk in enumerate(data_produk):
            if produk[0] == id_produk:
                produk_index = j
                break

        if produk_index is None:
            print("❌ Produk tidak ditemukan!")
            lanjut = input("Ingin coba lagi? (y/n): ").lower()
            if lanjut != "y":
                break
            else:
                continue

        nama_produk = data_produk[produk_index][1]
        harga_produk = int(data_produk[produk_index][2])
        stok_produk = int(data_produk[produk_index][3])

        while True:
            jumlah_input = input(f"Masukkan jumlah {nama_produk} yang ingin dibeli: ").strip()
            if not jumlah_input.isdigit():
                print("❌ Input tidak valid! Jumlah harus berupa angka.")
                continue
            jumlah = int(jumlah_input)
            if jumlah <= 0:
                print("❌ Jumlah harus lebih dari 0.")
                continue
            break

        if jumlah > stok_produk:
            print("❌ Stok tidak cukup!")
            continue

        total_harga = harga_produk * jumlah

        if saldo_user < total_harga:
            print("❌ Saldo tidak cukup untuk membeli produk ini!")
            continue

        keranjang.append({
            "id": id_produk,
            "nama": nama_produk,
            "jumlah": jumlah,
            "harga": harga_produk,
            "total": total_harga
        })

        saldo_user -= total_harga
        data_produk[produk_index][3] = str(stok_produk - jumlah)

        lanjut = input("Apakah ingin menambah barang lain? (y/n): ").lower()
        if lanjut != "y":
            break

    if not keranjang:
        print("\nTidak ada barang yang dibeli.")
        menu_customer(username)
        return

    data_user[user_index][2] = str(saldo_user)
    with open("users.csv", "w", newline="") as f:
        csv.writer(f).writerows(data_user)
    with open("product.csv", "w", newline="") as f:
        csv.writer(f).writerows(data_produk)

    clear()
    print("\n🧾===== INVOICE PEMBELIAN =====🧾\n")
    tabel_invoice = PrettyTable()
    tabel_invoice.field_names = ["Nama Produk", "Jumlah", "Harga Satuan", "Total Harga"]
    tabel_invoice.align = "l"

    total_semua = 0
    for item in keranjang:
        tabel_invoice.add_row([
            item["nama"],
            f"{item['jumlah']} pcs",
            f"Rp {item['harga']:,}",
            f"Rp {item['total']:,}"
        ])
        total_semua += item["total"]

    print(tabel_invoice)
    print(f"Total Pembayaran : Rp {total_semua:,}")
    print(f"Sisa Saldo       : Rp {saldo_user:,}")
    print("✅ Transaksi Berhasil! Terima kasih telah berbelanja di K3A Mart ❤️\n")

    lanjut = input("Apakah ingin lanjut belanja? (y/n): ").lower()
    if lanjut == "y":
        menu_customer(username)
    else:
        clear()
        print("\nTerima kasih sudah berbelanja 🙏")
        login_user()


#Cek saldo
def cek_saldo(username):
    clear()
    with open(users, "r") as f:
        data = list(csv.reader(f))

    for row in data:
        if row[0] == username:
            print(f"\nSaldo e-Money anda: Rp.{row[2]}")
            return

    print("> PENGGUNA TIDAK DITEMUKAN")


#Top Up saldo
def emoney(username):
    clear()
    if not os.path.exists(users):
        with open(users, "w", newline="") as f:
            csv.writer(f).writerow(["username", "password", "saldo", "role"])

    with open(users, "r") as f:
        data = list(csv.reader(f))

    found = False
    for i, row in enumerate(data):
        if row[0] == username:
            found = True
            saldo = int(row[2])
            break

    if not found:
        print("> PENGGUNA TIDAK DI TEMUKAN")
        return

    table = PrettyTable()
    table.field_names = ["NO", "NOMINAL TOP UP"]
    table.add_row(["1", "Rp. 50.000"])
    table.add_row(["2", "Rp. 100.000"])
    table.add_row(["3", "Rp. 300.000"])
    table.add_row(["4", "Rp. 500.000"])

    print(f"\nSaldo saat ini: Rp {saldo}")
    print(table)

    pilihan = input("Pilih nominal Top Up (1-4): ")

    nominal = {
        "1": 50000,
        "2": 100000,
        "3": 300000,
        "4": 500000
    }.get(pilihan)

    clear()
    if nominal:
        saldo += nominal
        data[i][2] = str(saldo)
        with open(users, "w", newline="") as f:
            csv.writer(f).writerows(data)

        print("<<< Pengisian saldo e-Money Berhasil >>>")
        print("================================================")
        print(f"Saldo e-Money anda sekarang: Rp.{saldo}")
        print("================================================")
    else:
        print("> Pilihan tidak valid")


#---------------------------------------------------------------------- ADMIN ---------------------------------------------------------------------------


# menu admin
def menu_admin():
    clear()
    print("""
    ==============================
    |        SELAMAT DATANG      |
    |             ADMIN          |
    ==============================
    """)
    while True:
        table = PrettyTable()
        
        table.field_names = ["NO", "MENU ADMIN"]
        
        table.add_row(["1", "TAMBAH BARANG"])
        table.add_row(["2", "TAMPILKAN BARANG"])
        table.add_row(["3", "UBAH BARANG"])
        table.add_row(["4", "HAPUS BARANG"])
        table.add_row(["5", "KELUAR"])
        
        table.align["NO"] = "l"
        table.align["MENU ADMIN"] = "l"
        
        print(table)
        
        admin = input("Pilih opsi: ")

        if admin == "1":
            tambah_barang()
        elif admin == "2":
            tampilkan_barang()
        elif admin == "3":
            update_barang()
        elif admin == "4":
            hapus_barang()
        elif admin == "5":
            clear()
            print("Logout Berhasil!")
            break
        else:
            print("Opsi tidak tersedia!")


# Create barang (admin)
def tambah_barang():
    clear()
    print("\n+--------TAMBAHKAN PRODUK BARU--------+")

    while True:
        id_produk = input("Masukkan ID Produk (angka saja): ")
        if not id_produk.isdigit():
            print("❌ ID Produk hanya boleh berisi angka!\n")
        else:
            break

    nama_produk = input("Masukkan Nama Produk: ")
    harga_produk = input("Masukkan Harga Produk: ")
    stok_produk = input("Masukkan Stok Produk: ")

    # mengecek id apakah ada di database
    if os.path.exists(product):
        with open(product, "r") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row and row[0] == id_produk:
                    print("\n❌ ID Produk sudah ada!\n")
                    return

    etalase_produk.add_row([id_produk, nama_produk, harga_produk, stok_produk])

    with open(product, "a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["ID Produk", "Nama Produk", "Harga Produk", "Stok Produk"])
        writer.writerow([id_produk, nama_produk, harga_produk, stok_produk])

    print("\nBarang berhasil ditambahkan!\n")
    print(etalase_produk)


# Read barang (admin) 
def tampilkan_barang():
    clear()
    try:
        print("\n+---------+---------DAFTAR PRODUK----------+-----------+")
        table = PrettyTable()
        table.field_names = ["ID Produk", "Nama Produk", "Harga Produk", "Stok Produk"]
        found = False

        with open(product, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)
            for row in csv_reader:
                if len(row) == 4:
                    table.add_row(row)
                    found = True

        if found:
            print(table)
        else:
            print("Tidak ada barang yang tersedia.")
    
    except FileNotFoundError:
        print("File 'product.csv' tidak ditemukan")


# Update barang (admin) 
def update_barang():
    clear()
    tampilkan_barang()
    while True:
        id_produk = input("Masukkan ID Produk yang ingin diubah: ")
        if not id_produk.isdigit():
            print("❌ ID Produk hanya boleh berisi angka!\n")
        else:
            break

    updated_rows = []
    found = False

    with open(product, mode='r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if row[0] == id_produk:
                print(f"\n=== Update Data untuk {row[1]} ===")
                nama_baru = input("Nama Produk baru (kosongkan jika tidak diubah): ") or row[1]
                harga_baru = input("Harga Produk baru (kosongkan jika tidak diubah): ") or row[2]
                stok_baru = input("Stok Produk baru (kosongkan jika tidak diubah): ") or row[3]

                updated_rows.append([id_produk, nama_baru, harga_baru, stok_baru])
                found = True
                print(f"\nProduk '{row[1]}' berhasil diperbarui.")
            else:
                updated_rows.append(row)

    if not found:
        print(f"\nProduk dengan ID '{id_produk}' tidak ditemukan.")
        return

    with open(product, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(updated_rows)


# Delete barang (admin) 
def hapus_barang():
    clear()
    tampilkan_barang()
    while True:
        id_produk = input("Masukkan ID Produk yang ingin diubah: ")
        if not id_produk.isdigit():
            print("❌ ID Produk hanya boleh berisi angka!\n")
        else:
            break

    updated_rows = []
    found = False

    try:
        with open(product, mode='r') as file:
            csv_reader = list(csv.reader(file))
            if len(csv_reader) > 0:
                header = csv_reader[0]
                updated_rows.append(header)
                for row in csv_reader[1:]:
                    if row[0] == id_produk:
                        found = True
                        print(f"\nProduk '{row[1]}' berhasil dihapus.")
                    else:
                        updated_rows.append(row)

        if not found:
            print(f"\nProduk dengan ID '{id_produk}' tidak ditemukan.")
            return

        with open(product, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(updated_rows)

    except FileNotFoundError:
        print("File 'product.csv' belum ditemukan")


# jalankan program 
main()


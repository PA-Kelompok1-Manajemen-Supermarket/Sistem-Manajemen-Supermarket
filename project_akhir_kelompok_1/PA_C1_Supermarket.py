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


# register 
def regis():
    print("""
    ===========================
        REGISTRASI AKUN BARU
    ===========================
    """)

    if not os.path.exists(users):
        with open(users, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "password", "saldo", "role"])

    username = input("Masukkan username: ")
    if username == "":
        print("> Username tidak boleh kosong!")
        return

    with open(users, "r") as f:
        reader = csv.reader(f)
        next(reader, None) 
        for row in reader:
            if row[0] == username:
                print("> Username sudah terdaftar, silakan login.")
                return

    password = pwinput.pwinput("Masukkan password: ", mask="*")
    if password == "":
        print("> Password tidak boleh kosong!")
        return

    with open(users, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([username, password, 0, "customer"])

    os.system("cls" if os.name == "nt" else "clear")
    print("Akun berhasil dibuat! Role anda: customer\n")


# login User
def login_user():
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
            print("\nUsername atau password salah.")
    except FileNotFoundError:
        print("\nFile 'users.csv' belum ditemukan")


# menu customer
def menu_customer(username):
    try :
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
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
    except ValueError :
        print("> PERHATIKAN INPUT")


def beli_barang():
    tampilkan_barang()
    input("Masukkan ID produk yang ingin anda beli : ")
    input("Jumlah produk : ")


def cek_saldo(username):
    with open(users, "r") as f:
        data = list(csv.reader(f))

    for row in data:
        if row[0] == username:
            print(f"\nSaldo e-Money anda: Rp.{row[2]}")
            return

    print("> PENGGUNA TIDAK DITEMUKAN")


def emoney(username):
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

    # Tampilkan menu top-up
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


# menu admin
def menu_admin():
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
            print("Logout Berhasil!")
            break
        else:
            print("Opsi tidak tersedia!")


# Create barang (admin)
def tambah_barang():
    print("\n+--------TAMBAHKAN PRODUK BARU--------+")
    id_produk = input("Masukkan ID Produk: ")
    nama_produk = input("Masukkan Nama Produk: ")
    harga_produk = input("Masukkan Harga Produk: ")
    stok_produk = input("Masukkan Stok Produk: ")


    etalase_produk.add_row([id_produk, nama_produk, harga_produk, stok_produk])

    with open(product, mode="a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["ID Produk", "Nama Produk", "Harga Produk", "Stok Produk"])
        writer.writerow([id_produk, nama_produk, harga_produk, stok_produk])

    print("\nBarang berhasil ditambahkan!\n")
    print(etalase_produk)


# Read barang (admin) 
def tampilkan_barang():
    try:
        print("\n+-----------DAFTAR PRODUK-----------+")
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
    tampilkan_barang()
    id_produk = input("\nMasukkan ID Produk yang ingin diubah: ")

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
    tampilkan_barang()
    id_produk = input("\nMasukkan ID Produk yang ingin dihapus: ")
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


# main program
def main():
    while True:
        try :
            print("""
===============================
        SELAMAT DATANG DI 
            K3A MART
===============================""")
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
                print("""
    =======================================
            PROGRAM TELAH SELESAI
        Terima kasih! dan sampai jumpa :)
    =======================================
        """)
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
    
        except KeyboardInterrupt :
                print("> PERHATIKAN INPUT")

# jalankan program 
main()
import datetime

data_perpustakaan = {}

while True:
    print("\n================================")
    print("   SISTEM MANAJEMEN PERPUSTAKAAN")
    print("================================")

    judul = input("Judul Buku: ")
    penulis = input("Nama Penulis: ")
    tahun = int(input("Tahun Terbit: "))

    tanggal_pinjam = input("Tanggal Terakhir Pinjam (YYYY-MM-DD): ")

    status = input("Status (Tersedia/Tidak): ").capitalize()

    tanggal = datetime.datetime.strptime(tanggal_pinjam, "%Y-%m-%d")

    KEY = (judul, penulis)

    data_buku = {
        "judul": judul,
        "penulis": penulis,
        "tahun_terbit": tahun,
        "tanggal_terakhir_pinjam": tanggal,
        "status": status
    }

    data_perpustakaan[KEY] = data_buku

    print("\nBuku berhasil ditambahkan!")

    print("\n================================")
    print("       DATA PERPUSTAKAAN")
    print("================================")

    for key, buku in data_perpustakaan.items():
        print("--------------------------------")
        print(f"KEY: {key}")
        print(f"Judul Buku: {buku['judul']}")
        print(f"Penulis: {buku['penulis']}")
        print(f"Tahun Terbit: {buku['tahun_terbit']}")
        print(f"Tanggal Terakhir Pinjam: {buku['tanggal_terakhir_pinjam'].strftime('%Y-%m-%d')}")
        print(f"Status: {buku['status']}")

    tambah = input("\nApakah ingin menambahkan buku lagi? (y/n): ")

    if tambah.lower() == "n":
        break

print("\nProgram selesai. Terima kasih!")
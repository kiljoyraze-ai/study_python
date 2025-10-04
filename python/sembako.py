class TokoSembako:
    def __init__(self):
        self.stok =[]
    
    def tambah_barang (self, nama_barang, harga, jumlah):
        self.stok.append({'nama_barang': nama_barang, 'harga': harga, 'jumlah':jumlah})
        print("Barang berhasil ditambahkan!")

    def lihat_stok(self):
        if self.stok:
            for index, barang in enumerate(self.stok):
                print("ID:", index)
                print("Nama Barang:", barang['nama_barang'])
                print("Harga:", barang['harga'])
                print("Jumlah:", barang['jumlah'])
                print("---------------------------")
        else:
            print("Stok kosong")

    def update_barang(self, id, nama_barang, harga, jumlah):
        if id < len(self.stok):
            self.stok[id] = {'nama_barang' : nama_barang, 'harga': harga, 'jumlah': jumlah}
            print("Barang berhasil di update")
        else:
            print("ID barang tidak ditemukan")

    def hapus_barang(self,id):
        if id < len(self.stok):
            del self.stok[id]
            print("Barang berhasil dihapus")
        else:
            print("ID barang tidak ditemukan")

    # contoh penggunaan
if __name__ == "__main__":
    toko = TokoSembako()

    while True:
        print("\n======= MENU =======")
        print("1. Tambah Barang ")
        print("2. Lihat Stok")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Keluar")

        pilihan = input("pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama barang: ")
            harga = int(input("Masukkan harga barang: "))
            jumlah = int(input("Masukkan jumlah barang"))
            toko.tambah_barang(nama, harga, jumlah)

        elif pilihan == "2":
            print("\n==== Stok toko sembako=====3")
            toko.lihat_stok()

        elif pilihan == "3":
            id = int(input("Masukkan ID barang yang ingin di update: "))
            nama = input("Masukkan nama barang baru: ")
            harga = int(input("Masukkan harga baru: "))
            jumlah= int(input("Masukkan jumlah baru: "))
            toko.update_barang(id, nama, harga,jumlah)

        elif pilihan == "4":
            id = int(input("Masukkan ID barang yang ingin dihapus: "))
            toko.hapus_barang(id)

        elif pilihan == "5":
            print("Terima Kasih")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi")

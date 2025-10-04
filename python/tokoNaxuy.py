print("-------------------")
print("-----TOKO NAXUY----")
print("-------------------")

nama = input("Masukkan nama barang = ")
harga = int(input("Masukkan harga barang = "))
jumlah = int(input("Masukkan jumlah barang = "))

total = harga*jumlah
print("Total pembelain Rp",total)

pembayaran = int(input("masukkan pembayaran anda = "))
kembalian = pembayaran - total
print("Kembalian anda Rp",kembalian)
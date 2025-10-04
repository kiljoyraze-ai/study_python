print("|=====================================|")
print("|       PROGRAM KASIR SEDERHANA       |")
print("|=====================================|")
print("|       : PILIH MENU MAKANAN :        |")
print("|=====================================|")
print("|Ayam bakar              Rp15000      |")
print("|Ayam geprek             Rp20000      |")
print("|Nasi goreng             Rp10000      |")
print("|Pecel lele              Rp25000      |")
print("|Mie sedap               Rp5000       |")
print("|=====================================|")

nomer_makanan = int(input("pilih (1/2/3/4/5) = "))
jml_porsi = int(input("Berapa Porsi = "))


if nomer_makanan == 1:
    total_makanan = jml_porsi *15000
    print(f"Ayam Bakar {jml_porsi} Porsi Rp.{total_makanan}")
    makanan = "Ayam Bakar"

elif nomer_makanan == 2:
    total_makanan = jml_porsi *20000
    print(f"Ayam Geprek {jml_porsi} Porsi Rp.{total_makanan}")
    makanan = "Ayam Geprek"

elif nomer_makanan == 3:
    total_makanan = jml_porsi *10000
    print(f"Nasi Goreng {jml_porsi} Porsi Rp.{total_makanan}")
    makanan = "Nasi Goreng"

elif nomer_makanan == 4:
    total_makanan = jml_porsi *25000
    print(f"Pecel Lele {jml_porsi} Porsi Rp.{total_makanan}")
    makanan = "Pecel Lele"

elif nomer_makanan == 5:
    total_makanan = jml_porsi *5000
    print(f"Mie sedap {jml_porsi} Porsi Rp.{total_makanan}")
    makanan = "Mie sedap"

else:
    print("menu tidak terdaftar!")

print("|=====================================|")
print("|       PROGRAM KASIR SEDERHANA       |")
print("|=====================================|")
print("|       : PILIH MENU MINUMAN :        |")
print("|=====================================|")
print("|Es Jeruk                Rp15000      |")
print("|Es teh                  Rp20000      |")
print("|Lemon tea               Rp10000      |")
print("|Es amngga               Rp25000      |")
print("|Air putih               Rp5000       |")
print("|=====================================|")

nomer_minuman = int(input("pilih (1/2/3/4/5) = "))
jml_gelas = int(input("Berapa Gelas = "))


if nomer_minuman == 1:
    total_minuman = jml_gelas *15000
    print(f"Es jeruk {jml_gelas} Porsi Rp.{total_minuman}")
    minuman = "Es jeruk"

elif nomer_minuman == 2:
    total_minuman = jml_gelas *20000
    print(f"Es teh {jml_gelas} Porsi Rp.{total_minuman}")
    minuman = "Es teh"

elif nomer_minuman == 3:
    total_minuman = jml_gelas *10000
    print(f"Lemon tea {jml_gelas} Porsi Rp.{total_minuman}")
    minuman = "Lemon tea"

elif nomer_minuman == 4:
    total_minuman = jml_gelas *25000
    print(f"Es mangga {jml_gelas} Porsi Rp.{total_minuman}")
    minuman = "Es mangga"

elif nomer_minuman == 5:
    total_minuman = jml_gelas *5000
    print(f"Air putih {jml_gelas} Porsi Rp.{total_minuman}")
    minuman = "Air putih"

else:
    print("menu tidak terdaftar!")


total_semua = total_makanan+ total_minuman
print(f"Total yang harus di bayar Rp.{total_semua}")

bayar = int(input("Masukkan Pembayaran anda : "))

if bayar > total_semua:
    kembalian = bayar - total_semua
else:
    uang_kurang = total_semua - bayar
    print("Uang yang dibayar anda kurang!")
    exit()

print("|=====================================|")
print("|           STRUK PEMBELIAN           |")
print("|=====================================|")
print("|Makanan          :",makanan,"\t\t|")
print("|Jumlah Porsi     :",jml_porsi,"\t\t|")
print("|Minuman          :",minuman,"\t\t|")
print("|jumlah gelas     :",jml_gelas,"\t\t|")
print("|Total Pembayaran :",total_semua,"\t\t|")
print("|Bayar            :",bayar,"\t\t|")
print("|Kembalian        :",kembalian,"\t\t|")
print("|=====================================|")
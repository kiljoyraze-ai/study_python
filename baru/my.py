

hargaGame = 2000
hargaMakan = 10000
uangSaya = 30000

total = ''
#conditional
# < , <= , > , >= , ==
# negasi adalah != 
# multi fungsional -> and | or 
if hargaGame > hargaMakan and uangSaya:
    print("harga game lebih besar dari harga makan (" , hargaGame , ")")
else:
    print("harga makan lebih murah dari harga game (" , hargaMakan , ")")

daftar_nama = ("Dian", "agus", "rafel")
for x in daftar_nama:
    print(daftar_nama[1] + " aowkoawkoakwo")

if daftar_nama == "agus":
        print("aowkaowkowakow")


number = 1
while number < 5:
     print("angka: " + str(number))
     number = number + 1

for y in range(1, 10):
        print(y)

for y in range(1, 10, 2): #lonkgap dua 
        print(y)

def sum(a, b):
     return a + b
print(sum(50, 90))
print(sum(12, 18))

nomor = sum(10, 90)
nomor = 200 * nomor
print(nomor)

kurang = sum(10, 80)
kurang = 100 - kurang
print(kurang)

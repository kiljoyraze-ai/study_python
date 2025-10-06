print("Hello World!!!")
print("Verifikasi diri anda terlebih dahulu dibawah ini!")
nama = input("Masukkan nama anda: ")
print("Holla ",nama)

# menu warteg warkop 
def menu():
    print("====DAFTAR MENU====")
    print("1. Mie ayam    Rp15000")
    print("2. Ayam goreng Rp15000")
    print("3. Krupuk      Rp15000")
    print("4. Sayur Lodeh Rp15000")
    print("5. Rendang     Rp15000")
    pilihMakan = input("masukkan nomor yang anda inginkan: ")
    
    match pilihMakan:
        case "1":
            print("Mie Ayam")
            hargaMkn = 15000
        case "2":
            print("Ayam goreng")
            hargaMkn = 15000
        case "3":
            print("Krupuk")
            hargaMkn = 15000
        case "4":
            print("Sayur Lodeh")
            hargaMkn = 15000
        case "5":
            print("Rendang")
            hargaMkn = 15000
    print("Makanan -> ",pilihMakan, hargaMkn)
menu()
    
def minuman():
    print("MENU ANEKA MINUMA")
    print("1. Es teh manis/tawar Rp10000")
    print("2. Sirup marjan       Rp10000")
    print("3. Es jeruk           Rp10000")
    print("4. Kopi Espresso      Rp10000")
    print("5. Jus mangga         Rp10000")

    nomor = str(input("masukkan nomor: "))

    if(nomor == "1"):
        print("Es teh manis/tawar")
        hargaMnm = 10000
    elif(nomor == "2"):
        print("Sirup marjan ")
        hargaMnm = 10000
    elif(nomor == "3"):
        print("Es jeruk  ")
        hargaMnm = 10000
    elif(nomor == "4"):
        print("Kopi Espresso ")
        hargaMnm = 10000
    elif(nomor == "5"):
        print("Jus mangga  ")
        hargaMnm = 10000
    else:
        print("daftar tidak tersedia ")
minuman()

def total():
    hrg_Makan = int(input("masukkan harga makan: "))
    hrg_Minum = int(input("Masukkan harga minuman: "))
    jumlah = hrg_Makan + hrg_Minum
    print("Hasil total semuanya")
    print(jumlah)
total()

# jika semua orang meragukan skill 
# maka berikan sebuah pembuktian bahwa skill ini bukan hanya wacana verbal
# Dunia ini meributkan tentang keadilan, bahwa yang menentukan salah benarnya adalah hanya tuhan sang maha mengetahui
# Bahwa perlu diketahui salah benarnya sifat manusia tidak ada yang berhak untuk menuntut nya 
# Karna manusia alaminya salah 


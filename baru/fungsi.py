def hola(nama):
    text = "nama dia " + nama
    print (text)

hola("DoniAjif")

def indentity(nama , nik, nis, agama):
     
    print("======IDENTITAS======\n"
     "nama :|"+     nama      + "|\n"
     "nik  :|"+     str(nik)  + "|\n"
     "nis  :|"+     str(nis)  + "|\n"
     "agama:|"+     agama     + "|\n")
indentity("Rudo", 121300, 123222, "Catholic")

#fungsi sebuah kalkulator
def kalkulator():
    angka = int(input("masukkan angka pertama: "))
    angka2 = int(input("masukkan angka kedua  : "))
   
    print("=====CALCULATOR=====\n"
        "num1: ", angka,  "\n"
        "num2: ", angka2 )
    
    penjumlahan = angka + angka2
    pengurangan = angka - angka2
    pembagian = angka / angka2
    perkalian = angka * angka2
    print("hasil penjumlahan dari ",angka, "+", angka2 ,"=", penjumlahan)

kalkulator()
#kesalahan pertama dalam menggunakan fungsi 
# Parameter fungsi tidak dibutuhkan jika semua menggunakan input di dalam fungsi.
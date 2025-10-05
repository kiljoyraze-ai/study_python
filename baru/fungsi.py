def hola(nama):
    text = "nama dia " + nama
    print (text)

hola("DoniAjif")

def indentity():
     nama = str(input(" Nama: "))
     nik = int(input("  Nik:"))
     nis = int(input("  Nis: "))
     agama = str(input("Agama: "))

     print("====IDENTITAS-DIRI==== \n"
          "Nama : ", nama, "\n" 
          "Nik  : ", nik, "\n"
          "Nis  : ", nis, "\n"
          "Agama: ", agama)
indentity()

# indentity("Rudo", 121300, 123222, "Catholic")

#fungsi sebuah kalkulator
def kalkulator():
    pickOperator = input("Pilih oprasi (+ , - , * , /): ")
    angka = int(input("masukkan angka pertama: "))
    angka2 = int(input("masukkan angka kedua  : "))
    hasil = ''
    operator = ""
    match pickOperator:
        case "+":
            operator = "Penjumlahan"
            hasil = angka + angka2
        case "-":
            operator = "Pengurangan"
            hasil = angka - angka2
        case "*":
            operator = "Perkalian"
            hasil = angka * angka2
        case "/":
            operator = "Pembagian"
            hasil = angka / angka2

    print("=====CALCULATOR=====\n"
        "num1: ", angka,  "\n"
        "num2: ", angka2, "\n",
        "Hasil dari {}".format(operator) , hasil)
    

kalkulator()
#kesalahan pertama dalam menggunakan fungsi 
# Parameter fungsi tidak dibutuhkan jika semua menggunakan input di dalam fungsi.
print("---------R-E-S-T-O-L-E-G-I-U-N--------")
pembeli= input("Nama pembeli: ")
print("Nama Pembeli: ",pembeli)

def fungsimakanan():
    global totalmkn
    global porsi
    global mkn
    print("------------Menu Makanan-----------")
    print("1. Nasi goreng   - Rp12000")
    print("2. Mie ayam      - Rp10000")
    print("3. Mie tek tek   - Rp23000")
    print("4. Steak spesial - Rp30000")
    nomor = int(input(" Nomer makanan yang anda pilih : "))
    porsi = int(input("Porsi makanan : "))

    if nomor==1:
        totalmkn=porsi*12000
        print(porsi,"Porsi nasi goreng  = Rp", totalmkn)
        mkn=("Nasi goreng")
    elif nomor==2:
        totalmkn=porsi*10000
        print(porsi,"Porsi Mie ayam = Rp", totalmkn)
        mkn=("Mie ayam")
    elif nomor==3:
        totalmkn=porsi*23000
        print(porsi,"Porsi Mie tek tek  = Rp", totalmkn)
        mkn=("Mie tek tek")
    elif nomor==4:
        totalmkn=porsi*30000
        print(porsi,"Steak Spesial = Rp", totalmkn)
        mkn=("Steak Spesial")
    else:
        print("Anda belum memesan apapun")
        fungsimakanan()
fungsimakanan()
print()


def fungsiminuman():
    global totalmnm
    global gelas
    global mnm
    print("------MENU MINUMAN------")
    print("1. ES teh manis - Rp5000")
    print("2. ES jeruk - Rp7000")
    print("3. Air mineral - Rp4000")
    print("4. Jus Mangga - Rp8000")
    nomor = int(input("Nomer Minuman: "))
    gelas = int(input("Berapa gelas: "))

    if nomor==1:
        totalmnm=gelas*5000
        print(gelas,"ES teh manis",totalmnm)
        mnm=("ES teh manis")
    elif nomor==2:
        totalmnm=gelas*7000
        print(gelas,"ES jeruk",totalmnm)
        mnm=("ES jeruk")
    elif nomor==3:
        totalmnm=gelas*4000
        print(gelas,"Air mineral",totalmnm)
        mnm=("Air mineral")
    elif nomor==4:
        totalmnm=gelas*8000
        print(gelas,"Jus mangga ",totalmnm)
        mnm=("Jus mangga")
    else:
        print("Anda belum memesan!")
        fungsiminuman()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print()
print("\n total : Rp",totalsemua)
uang = int(input("Uang dibayar : Rp"))
kembalian=(totalsemua-uang)
print("kembalian : Rp",kembalian)
print()

print("|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
print("|=-=-=-=-=-=-=PEMBELANJAAN-=-=-=-=-=|")
print("|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
print("Nama\t\t: ",pembeli)
print("Beli\t\t: ",porsi,mkn, "(Rp",totalmkn,")")
print("Beli\t\t: ",gelas,mnm, "(Rp",totalmnm,")")
print("Tagihan\t\t: ",totalsemua)
print("Dibayar\t\t:",uang)
print("Kembalian\t:",kembalian)
print("|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
print("|=-=-=-=-=-TENGKYU PERIMACH=-=-=-=-=-=|")
print("|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
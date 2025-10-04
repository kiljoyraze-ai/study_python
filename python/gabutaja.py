print("|====================================|")
print("|==============PEKERJAAN=============|")
print("|====================================|")
print("|Polisi                Gaji: 50000   |")
print("|Damkar                Gaji: 60000   |")
print("|Dokter                Gaji: 40000   |")
print("|Teknik                Gaji: 95000   |")
print("|Progammer             Gaji: 195000  |")
print("|====================================|")

nomor = int(input("masukkan nomor pekerjaan  ; "))
jml_org = int(input("JUmlah orang : "))

if nomor == 1:
    total = jml_org * 50000
    print(f"Jumlah {jml_org} Gaji Rp.{total}")
    print("Polisi")

elif nomor == 2:
    total = jml_org * 60000
    print(f"JUmlah {jml_org} Gaji Rp.{total}")
    print("Damkar")

elif nomor == 3 :
    total = jml_org * 40000
    print(f"Jumlah {jml_org} Gaji Rp.{total}")
    print("Dokter")

elif nomor == 4:
    total = jml_org *95000
    print(f"Jumlah {jml_org} Gaji Rp.{total}")
    print("Teknik")

elif nomor == 5:
    total = jml_org * 195000
    print(f"Jumlah {jml_org} Gaji Rp.{total}")
    print("Programmer")

else:
    print("Profesi tidak terdaftar!")

import time

teks = """jadi kita akan mengambil angka melalui keyword atau kata kunci ('f') ,
      atau bisa dibilang f itu format yang memudahkan kita untuk menggabungkan antara tanda kutip string dengan variabel, 
      sehingga ini sangat memudahkan programmer untuk menulis sesuatu dengan dinamis bisa dikatakan ini lebih dinamis:"""

for huruf in teks:
    print(huruf, end='', flush=True)
    time.sleep(0.1) # jeda 0.1 detik antar karakter
print() # baris baru setelah selesai

teks = "Ini adalah contoh tampil per kata seperti lirik lagu"
for kata in teks.split():
    print(kata, end=' ', flush=True)
    time.sleep(0.3)  # jeda 0.3 detik antar kata
print()
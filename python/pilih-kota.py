tabel = [['Baden',      'Australia'],
         ['Bandung',    'Indonesia'],
         ['Bogor',      'Indonesia'],
         ['Graz',       'Australia'],
         ['Innsbruck',  'Australia'],
         ['Kariya',     'Jepang'],
         ['Kudus',      'Indonesia'],
         ['Kyoto',      'Jepang'],
         ['Linz',       'Australia'],
         ['Nagoya',     'Jepang'],
         ['Samarinda',  'Indoensia'],
         ['Tokyo',      'Jepang'],
         ['Toyokawa',   'Jepang'],
         ['Wina',       'Australia']]

print('Daftar kota di suatu negara ')
print('-----------------------------')

namaNegara = input('nama negara: ')

jumKota = 0
for indeks in range(0, len(tabel)):
    if namaNegara.lower() == tabel[indeks] [1].lower():
        jumKota += 1

        print(tabel[indeks][0])

print()
if jumKota == 0:
    print('Data tidak ditemukan')
else:
    print('jumlah kota : ', jumKota)
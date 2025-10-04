import time

def tampilkan_lirik(lirik, delay_baris=1.0, delay_kata=0.3):
    """
    Menampilkan lirik lagu dengan ritme.
    :param lirik: List berisi baris-baris lirik.
    :param delay_baris: Delay antara baris (dalam detik).
    :param delay_kata: Delay antara kata (dalam detik).
    """
    for baris in lirik:
        for kata in baris.split():  # Pisahkan kata-kata dalam baris
            print(kata, end=' ', flush=True)  # Cetak kata dengan spasi
            time.sleep(delay_kata)  # Delay antara kata
        print()  # Pindah ke baris baru setelah satu baris selesai
        time.sleep(delay_baris)  # Delay antara baris

# Contoh lirik lagu
lirik_lagu = [
    "Hari ini ku bangun pagi",
    "Melihat mentari bersinar terang",
    "Kupikirkan dirimu lagi",
    "Membuat hatiku berdebar-debar",
    "",
    "Kau bintang di malam gelap",
    "Terangi jalanku yang kelam",
    "Bersamamu, aku tak takut",
    "Kita menuju masa depan yang indah"
]

# Tampilkan lirik dengan ritme
tampilkan_lirik(lirik_lagu, delay_baris=1.5, delay_kata=0.2)
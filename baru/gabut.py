import random
import time

def glitch_text(text, iterations=30):
    """Efek glitch pada teks"""
    glitch_chars = "!@#$%^&*()_+-=[':\",./<>?`~@#$%^&?^%?^?&*()_(*&^%$#$*()*&%$#%^*&()_()(**&^%^$^*&()*&%^$))"
    
    for i in range(iterations):
        glitched = ""
        for char in text:
            if random.random() < 0.3:
                glitched += random.choice(glitch_chars)
            else:
                glitched += char
        print(f"\r{glitched}", end='', flush=True)
        time.sleep(0.7)
    print(f"\r{text}")

glitch_text(f"""\033[32mjadi kita akan mengambil angka melalui keyword atau kata kunci ('f') ,
atau bisa dibilang f itu format yang memudahkan kita untuk menggabungkan antara tanda kutip string dengan variabel, 
sehingga ini sangat memudahkan programmer untuk menulis sesuatu dengan dinamis bisa\033[0m""")


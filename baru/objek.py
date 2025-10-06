class Player:
    nama = ""
    umur = ''
    hobby = ''
    ststus= ''

    def getName(aku, nama): #ternyata beda itu bisa (plesetan dari kata indah |JK XD)
        aku.nama = nama
        return aku.nama
    
    def getUmur(self, umur):
        self.umur = umur
        return self.umur
    
    def getHobby(self, hobby):
        self.hobby = hobby
        return self.hobby
    
    def getStatus(self, status):
        self.status = status
        return self.status 
    
identity = Player()
print("NAMA ->", identity.getName("ajeng"),"\n",
      "UMUR ->", identity.getUmur(20), "\n",
      "HOBBY  ->",identity.getHobby("Soccer Ball"), "\n",
      "STATUS ->",identity.getStatus("Jomblo sejati"))

#jika kamu ingin membuat sebuah fungsi di dalam class maka parameter pertama itu --
#merujuk kepada nama classny itu sendiri, tujuannya untuk mendeklarasikan variabel yang ada dalam classnya 

class menuKantinMetik:
    mkn = ''
    mnm = ''

    def __init__(self, mkn, mnm):
        self.mkn = mkn
        self.mnm = mnm
    def namaMkn(self):
        return self.mkn
    def namaMnm(self):
        return self.mnm
kantin = menuKantinMetik("mie ayam", "es teh")
print(kantin.namaMkn() , kantin.namaMnm())
   
# akan tetapi kita mempunyai cara yang mudah dengan metode __str__

class User:
    def __init__(self, pysical, mana):
          self.pysical = pysical
          self.mana = mana

    def __str__(self):
        return f"{self.pysical}{self.mana}"
panggil = User(200, 100)
print(panggil)
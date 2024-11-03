#class olusturma ve metotlar KALITIM İNSAN PROF DİYE AYRILMASI
"""
class Ucus():
    havayolu="THY"

ucus1=Ucus()

print(ucus1.havayolu)
"""
"""
class Ucus():
    havayolu="THY"

    def __init__(self,kod,kalkis,kapasite):
        self.kod=kod
        self.kalkis=kalkis
        self.kapasite=kapasite
        
#ucus2=Ucus() BUNU DEMEK HATALİ

ucus2=Ucus("a123","mugla",90)

print(ucus2.kalkis)
"""

class Ucus():
    havayolu="THY"

    def __init__(self,kod,kalkis,kapasite):
        self.kod=kod
        self.kalkis=kalkis
        self.kapasite=kapasite
        
    def ananons_yap(self):
        return "{} kodlu ucus {} konumundan kalkacaktir".format(self.kod,self.kalkis)
    
ucus3=Ucus("s789","izmir",300)

print(ucus3.ananons_yap())
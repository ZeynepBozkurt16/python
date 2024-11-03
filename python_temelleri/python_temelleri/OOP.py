class Ucus():
    havayolu ="THY"

    def __init__(self,kod,varis):
        self.kod=kod 
        self.varis=varis

    def ananos_yap(self):
        return "{} sefer sayili ucus {} 'a gidecektir ".format(self.kod,self.varis)


ucus1=Ucus("4200","LONDON")

print(ucus1.kod)
ucus2=Ucus("tk27","NYC")

print(ucus2.ananos_yap())
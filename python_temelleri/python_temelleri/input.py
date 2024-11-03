'''
input("bir sayi girin: ")

girdi=input("sayiyi gir: ")
print(girdi)
'''

def uygulama():
    girdi=input("sayiyi giriniz: ")
    islem=input("verinin tek mi cift mi oldugunu sorgula: ")

    if islem=="cift":
        if int(girdi)%2==0:
            return "bu cift bir sayidir"
        else:
            "hayir bu cift sayi degildir"
    
    elif islem=="tek":
        if int(girdi)%2==1:
            return "evet tek sayidir"
        else:
            return "hayir tek sayi degildir"
        
print(uygulama())
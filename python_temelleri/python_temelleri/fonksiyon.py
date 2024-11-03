'''
fonksiyon oluşturmak için

def fonksiyon adi(argumanlar): snake_case


    bu kod ne ise yarar     #docstring(3 tirnakli kisim fonksitonun ne yapacagini anlatir)
                             #return/print

 #return/print
     '''
#fonksiyonu tanimladik 
def bes_bastir():
    print(5)
#fonksiyonu çalıştırdık
bes_bastir()
#retun değer dödürür ancak print deger döndürmesi istenirse none verir yani bosluk

def yedi_dondur():
    return 7

print(yedi_dondur())
print(bes_bastir())# görüldüğü üzere print değer döndürmez ancak retun eden fonksiyonu print ile yazdırırsan sana cıktı verir
#fonksiyonlarda argümanlar

def sayi_dondur(sayi):
    return sayi

print(sayi_dondur(753952753985))

#default kullanımı aksi iddia edilmediği sürece verilen argumanı kullanır.
def fonksiyon(sayi=213):
    return sayi

print(fonksiyon())
print(fonksiyon(59))

def buyuk_sayi_dondur(a,b):   #eger birden fazla retun varsa ilk returnden sonra donguden cıkar
    if a>b:
        return a
    elif b>a:
        return b
    
print(buyuk_sayi_dondur(74,90))    


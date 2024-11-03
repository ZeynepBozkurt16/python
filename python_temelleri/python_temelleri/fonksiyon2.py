#fonksiyonların birbiriyle ilişkisi
def buyuk_sayi_dondur(a,b):
    if a>b:
        return a 
    elif b>a:
        return b 

print(buyuk_sayi_dondur(78,90))

def metin_olustur(a,b):
    buyuk_sayi=buyuk_sayi_dondur(a,b)
    sablon_metin="{} daha buyuk sayidir".format(buyuk_sayi)
    print(sablon_metin)

metin_olustur(20,22)
#fonk birden fazla sonuc dondurebilir splitten sonraki() parantezi unutma

def isim_soyisim_ayirma(isim_soyisim):
    isim=isim_soyisim.split()[0]
    soyisim=isim_soyisim.split()[1]
    return isim,soyisim

print(isim_soyisim_ayirma("zeynep bozkurt"))
#hoin ile eleman birleştirme 2 eleman birleştirir

def isim_soyisim_birlestir(isim,soyisim):
    return " ".join([isim,soyisim])

print(isim_soyisim_birlestir("zeynep","bozkurt"))
#args kullanımı liste gibi birden cok parametreyi birlestirir.

def birlestir(*args):
    return " ".join(args)

print(birlestir("zeynep","nur"))
#kwargs kullanımı dic

def gobek_adi(**kwargs):
    if "gobekadi" in kwargs:
        print(kwargs[gobek_adi])
    else:
        print("yok!")

gobek_adi(gobek_adi="zey",soyisim="aaa")    


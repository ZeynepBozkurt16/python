#is digit komutu sayi olup olmadıgını sorgulatmak için kullanılır.
"""
def sayi_kontrol():
    girdi=input("bir sayi girniz: ")

    if girdi.isdigit():
        print("tebrikler bir sayi girdiniz ")
    
    else:
        print("maalesef bir sayi girmedniz:")

sayi_kontrol()
"""
def sorgu():
    giris=input("bir sayi girin: ")

    while not giris.isdigit():
        print("bu bir sayi değil: ")
        giris=input("bir sayi girin: ")
    else:
        print("tebrikler") 

sorgu()   
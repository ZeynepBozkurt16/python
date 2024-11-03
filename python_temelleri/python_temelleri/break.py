liste=["a","b","c","e"]*10

for index,harf in enumerate(liste):
    if harf=="c":
        print("{} harfi {} indekste bulunuyor".format(harf,index))
        break

#contiune kullanımı 

for sayi in range(1,6):
    if sayi%2==0:
        continue
    print(sayi)
#pass kullanimi:

for sonuc in range(2,17):
    if sonuc%2==0:
        pass
    else:
        print(sonuc)
a=20
if a<15:
    pass
else:
    print("merhaba dünya")        
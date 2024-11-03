liste=[1,2,3]
deneme=1,8,"on dokuz"

print(type(liste))
print(type(deneme))

#elemanlarına listedeki gibi ulaşmak mümkün
print(liste[2])
print(deneme[1])

#uzunluğu hesaplatılabilir
print(len(liste))
print(len(deneme))
#listeyi de tuple da baştan yazabiliriz: eski değeri görünmez

deneme="ayse,fatma,rana"
liste=[18,97,"zeynep"]

print(deneme)
print(liste)
#tuple da değişiklik yapılmaz elemanda ,tupleda count ve index özelliği bulunabilir

liste[0]="aliye"
#deneme[0]="berk"

print(deneme)
print(liste)
#listdeki gibi ekleme işlemi yapılabilir:
isim=("fatma,esra,selin,dilan")
res="sehir,hayvan,bitki"

print(res+isim)
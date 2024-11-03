kullanici1={
    "ad":"ferhat",
    "soyad":"ibrik",
    "uzmanlik":["front-end"]
}

kullanici2={
    "ad":"gokce",
    "soyad":"gun",
    "uzmanlik":["tasarim"]
}

kullanici3={
    "ad":"mesut",
    "soyad":"gun",
    "uzmanlik":["front-end"]
}

#ferhat ibrik adlı kullanıinin uzmanlık alanını döndür

print(kullanici1["uzmanlik"])

kullanici_listesi=[kullanici1,kullanici2,kullanici3]

#front end konusundaki uzman isimleri döndür

for kullanici in kullanici_listesi:
    if kullanici["uzmanlik"]==["front-end"]:
        print(kullanici["ad"])
   

#mesut yazilim öğrendi bilgileri güncelle dikakt et
kullanici3["uzmanlik"].append("yazilim")
print(kullanici3)

#birden fazla uzmanlık alanı olanları döndür

for kullanici in kullanici_listesi:
    if len(kullanici["uzmanlik"])>1 :
        print(kullanici["ad"])


#zip kulalnarak iki listeyi birleştir ve yaşı 30dan küçük olanların ismini yazdir
kullanici_yaşlari_listesi=[22,34,32]

for toplam in zip(kullanici_listesi,kullanici_yaşlari_listesi):
    print(toplam)


for kullanici,yas in zip(kullanici_listesi,kullanici_yaşlari_listesi):
    if yas<30:
        print(kullanici["ad"])
#değer isimli değişkene atanan sayinin asal olup olmadığını söyle yapilamadi


#elimde değer var bir döngü kullanmalıyım if sorgusu kullanmalıyım asal sayi1 ve kendinden baska boleni olamalı 

    

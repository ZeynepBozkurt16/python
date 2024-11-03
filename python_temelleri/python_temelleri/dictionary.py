#key value ilişkisi ile çalışır
sehir={"denizli":20,"izmir":35}
print(sehir["denizli"])
#dictionary şeklindeki listeye yeni eleman eklenebilir ve mevcut value değiştirilebilir
sehir["muğla"]=48
print(sehir)
sehir["denizli"]=19
print(sehir)


kullanıcı={
    
"zeynep":{
"age":19,
"phone":185555,
"mail":"gyhrfuıjkjngjhrjf"},

"ali":{
"age":26,
"phone":54565,
"mail":"fhjdnbghdj"
}
}
print(kullanıcı["zeynep"])
print(kullanıcı["ali"]["age"])


#örnek
ogrenciler={}
numara=input("numarayı giriniz: ")
isim=input("adı giriniz: ")
soyisim=input("soyismi giriniz: ")
phone=input("numarayı giriniz: ")
ogrenciler[numara]={
"ad":isim,
"soyad":soyisim,
"telefon":phone,

}
print(ogrenciler)
#aynı şeyler update metodu ile de yapılabilir
ogrenciler.update({
    numara:
    {
        "ad":isim,
        "soyisim":soyisim,
        "telefon":phone
    }
})
print(ogrenciler)

names=["zeynep","nur","dila","zayn"]
years=[1999,1976,2003,2008]
#fatmayı namesin sonuna ekleyin
result=names.append("fata")

# sena değerini listenin sonuna ekleyiniz:
result=names.insert(0,"sena")

#nur ismini listeden siliniz
names.remove("nur")
#ali names listesinde var mıdır
result= "ali" in names
print(result)
result=names.index("zeynep")
print(result)
#liste elelamnlarını ters çevirin

names.reverse()
print(names)

#elemanları alfabetik olarak sırala
names.sort()
print(names)

#years listesini sıaralayınız
years.sort()
print(years)

a="ayse,fatma".split(",")
print(a)
#years dizisinin en büyük ve enküçük dizisini bulunuz
min_deger=min(years)
print(min_deger)
max_deger=max(years)
print(max_deger)
#years dizisinin tüm elemanlarını siliniz

years.clear()
print(years)
#kullanıcıdan alınan 3 marka ile dizi oluşturalım

markalar=[]
marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

print(markalar)








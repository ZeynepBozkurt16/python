cars=["BMW","Mercedes","Opel","Mazda"]

#1.soru liste kaç elemanlıdır?
sonuc=len(cars)
print(sonuc)
#2.soru liatenin ilk ve son elemanı nedir
print(cars[0])
print(cars[3])
#3.soru mazda ve toyota yerini değiştir
cars[-1]="toyota"
print(cars)

#4.soru mercedes lsitenin bir elemanı mıdır?
result="Mercedes" in cars
print(result)
#listenin ilk 3 elemanı
sonuc=cars[0:3]
print(sonuc)
#eleman silme del ile
del cars[-1]
result=cars
print(result)
#liste elemanlarını tersten yazdır
result=cars[::-1]
print(result)



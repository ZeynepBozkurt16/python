print("zeynep")
print(8+7)
type(2)
meyveler=["elma","muz","armu","nar","çilek"]
print(meyveler+["mandaline"])
#append ile sondaan ekleme yapılabiilir
meyveler.append("incir")
print(meyveler)

#pop ile sondaki eleman silineblir

meyveler.pop()
print(meyveler)
liste=[1,"a",2,3,True,4,5,"true","1"]
#listenin son elemanını nasıl bulabiliriz
print(liste[-1])
#listenin 2. ve 4.elemanlaırnı içeren yeni nir liste oluştur
print(liste[2:6:3])#her3 de 1 al
#metot kullarak ters çevir
print(liste.reverse())
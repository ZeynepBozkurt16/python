
x=8
result=5<x<10
print(result)
#bu işlem yerine and or not kullanılır 
#iç koşullar oluşturulabilir:
a=15
result=(a>10 and a<20) and (a%2==0)
print(result)

#girilen sayı 1 ile 100 arasında mı

y=int(input("y sayısını giriniz: "))
result=y>=1 and y<=100
print(result)

#girilen sayının pozitif çift sayı olup olmadığını kontrol ediniz

k=int(input("k sayısını giriniz: "))
result=k>0 and k%2==0
print(result)

# email ve şifre ile giriş bilgileri kontrolu yapın:
email="znb@gamil.com"
password=1234

a=input("e maili girin: ")
b=int(input("sişreyi girin: "))

result=email==a and password==b
print(result)

#girilen 3 sayıyı büyüklük olarak karşılaştırın:

dizi=[]
a=int(input("a yı girin: "))
b=int(input("b yı girin: "))
c=int(input("c yı girin: "))
dizi.append(a)
dizi.append(b)
dizi.append(c)
dizi.sort()

print(dizi)

#kullanıcıdan 2 vize 1 final notu alın 50 üstünde ise geçti 50 altında ise kaldı yazın

vize1=int(input("1. vizeyi girin:"))
vize2=int(input("2.vizeyi girin: "))
final=int(input("final notunu girin: "))

result=((vize1+vize2)*0.4)+final*0.6
gecti=result>50 and final>50

print(f"dönem dersinden geçtiniz: {gecti}")

# isim boy kilo alınan bireyin indexini hesapla:
name=input("ismi girin: ")
boy=float(input("boyu m cinsinden girin"))
kg=float(input("kiloyu girin:" ))

index=kg/boy**2

zayıf=index>0 and index<18.4
orta=index>18.4 and index<24.9
kilolu=index>24.9 and index<=29.9
print(f"{name} indexiniz zayıf: {zayıf}")
print(f"{name} indexiniz orta: {orta}")
print(f"{name} indexiniz kilolu: {kilolu}")

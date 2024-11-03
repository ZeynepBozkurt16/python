#x,y,z=10,15,20
#x,y=y,x
#x=x+5 #x+=5 ile yanı ifadedir
#x=x-5 x-=5
#x=x*5 x*=5 ile aynı ıfadedir
#// tam bölmedir sadece tam kısmı alır
#tuple ile atama yapılabilir eleman sayısı çok ya da az olursa hata verir



deger=10,20,29
x,y,z=deger
print(x,y,z)
#eger ifadenin basına yıldız atılırsa kalan elemanlar o elemana dizi olarak atılır
values=10,20,30,4,7

a,b,*c=values
print(a,b,c)


#DEMO:

#
a,b,c=2,8,9
numbers=10,17,89,4,72
#kullanıcıdan aldıgınız iki sayı ile a,b,c toplamının farkı nedir?
number1=int(input("1.sayıyı girin: "))
number2=int(input("2.sayıyı girin: "))

sonuc=(number1*number2)-(a+b+c)
print(sonuc)

#bnin a ya bölümsüz kalanını hesaplayın:
result=b//a
print(result)


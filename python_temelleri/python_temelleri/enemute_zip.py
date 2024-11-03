'''

iterable=yenilebilir

'''
#range bir veri tipidir

range(10)#[start:end] oldugu gibi 0dan 9a kadar olan ifadeleri yazar
#range list veri tipine cevrilebilir ve 2 yolu vardır.
print(list(range(10))) 
print([*range(10)])

#listedeki gibi parametreler verilebilir. random ifadelerde kullanılabilir.

print(list(range(2,10,2)))

for sayi in range(10):
    print(sayi)
    
for sonuc in range(20):
    if sonuc>10:
        print(sonuc)

# enumarete kulanımı

harfler=["a","b","c","d","e"]

for harf in enumerate(harfler):
    print(harf)


harfler=["a","b","c","d","e"]

for index,harf in enumerate(harfler):
    print(index,harf)

    harfler=["a","b","c","d","e"]

for index,harf in enumerate(harfler):
    print("{0}.  harf: {1}".format(index,harf))

   #zip kullanımı uzunluklar eşit olmalı   #girintelere dikkat

ulkeler= ["TR","FR","ABD"]
siralama=range(1,4)  

for ulke in zip(ulkeler,siralama):
    print(ulke) 
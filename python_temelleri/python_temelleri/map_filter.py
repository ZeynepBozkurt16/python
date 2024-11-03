def karesini_al(x):
    return x**2

print(karesini_al(10))

sayilar=list(range(1,6))

for index in range(len(sayilar)):
    sayilar[index]=karesini_al(sayilar[index])

print(sayilar)
#map işlemi listein her lemanına uygular

print(list(map(karesini_al,[1,2,3])))
print(list(map(karesini_al,sayilar)))

def cift_filtrele(x):
    if x%2==0:
        return x
    else:
        return None
    
print(cift_filtrele(50))   

sayi=list(range(1,6))

print(list(filter(cift_filtrele,sayi)))

sayilar=list(range(1,7))

print(list(map(lambda x: x**2 ,sayilar)))
print(list(filter(lambda x : x if x%2==0 else None,sayilar )))

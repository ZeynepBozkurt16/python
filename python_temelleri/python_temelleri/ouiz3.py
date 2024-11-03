#1
def us_bul(a,b):
    return  a**b

print(us_bul(4,2))
# for ile us bul

def hesapla(a,b):
    sonuc=1
    for kuvvet in range(1,b+1):
        sonuc=sonuc*a

    return sonuc
    
print(hesapla(4,4))    
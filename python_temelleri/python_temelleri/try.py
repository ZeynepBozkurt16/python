"""
print(round(1.3))
print(round(1.7))


def yuvarla():
    girdi=input("bir sayi giriniz: ")

    print("yuvarlanan sayi {}".format(round(float(girdi))))

yuvarla()


def tam_sayiya_cevir():
    girdi=input("bir sayi giriniz:")
    try:
        girdi=float(girdi)
        print(" yuvarlanmis hali :{}".format(round(girdi)))
    except:
        print("{} girdisi tam sayiya cevrilemiyor".format(girdi))


tam_sayiya_cevir()    

#try expect kısmı else ile kullanılablir 
def tam_sayiya_cevir():
    girdi=input("bir sayi giriniz:")

    try:
        girdi=float(girdi)
        
    except:
        print("{} girdisi tam sayiya cevrilemiyor".format(girdi))
    else:
        print(" yuvarlanmis hali :{}".format(round(girdi)))
      

#finally kullanımı 

def tam_sayiya_cevir():
    girdi=input("bir sayi giriniz:")
    status=" "
    try:
        girdi=float(girdi)
        print(" yuvarlanmis hali :{}".format(round(girdi)))
        status="basarili"
    except:
        print("{} girdisi tam sayiya cevrilemiyor".format(girdi))
        status="basarisiz"
    finally:
        print("tam sayiya cevirme islemi {} tamamlandı: ".format(status))

tam_sayiya_cevir()
  """
def donustur():
    while True:
        girdi=input("sayi gir")
        try:
            girdi=float(girdi)
            print("sayi {}".format(girdi))
            break
        except:
            print("girdi donusturulemiypr")
            pass
donustur()
fruits= {"orange","apple","banana"}
print(fruits)

#indexlenemez print(fruits[0]) for döngüsü ile elemanlaraına ulaşılabilir

for y in fruits:
    print(y)

# eleman ekleme add ya da update metodu ile yapılır.
#1 eleman liatede 1 kez yazılabilir eklenemeye çalışılırsa 2 defa listelenemz
fruits.add("cherry")
fruits.update(["mango","grape"])
print(fruits)
#remove ya da discard ile eleman silme işlemi yapılabilir
#pop metodu çalışır ancak herhangi bir elemanı siler clear metodu tüm elemanları siler

list=[1,7,9,3,3,7,1]
print(list)
print(set(list))
fruits.remove("orange")
fruits.discard("apple")
print(fruits)
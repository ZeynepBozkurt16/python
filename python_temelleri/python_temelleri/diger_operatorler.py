#identity operator: is gititkleri adres önemlidir
x=y=[1,2,3]
z=[1,2,3]
print(x==y)
print(x==z)
print(x is z)
print(x is not z)

#memembership operator: içinde olup olmaddıgını sorgulayabilirsin.
name=["zeynep","ahmet"]
print("ahmet" in name)
print("zeynep" not in name)

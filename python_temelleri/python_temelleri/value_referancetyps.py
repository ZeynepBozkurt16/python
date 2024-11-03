# value types da verinin kendisi ile uğraşılır ikisi farklı alandadır string ya da float,int

x=10
y=20
x=y
y=45
print(x,y)



#referance types da listenin adresi ile uğraşılır=> list veya class olabilir değişiklikten etkilenir
list1=["apple","grape"]
list2=["apple","grape"]
list1=list2
list2[0]="orange"
print(list1,list2)
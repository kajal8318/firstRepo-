tuple1=(10,20,30,40,50,60)
print(tuple1)
count=0
for i in tuple1:
    print("tuple1[%d]=%d"%(count,i))
    count+=1

tuple2=tuple(input("enter the tuple element...."))
print(tuple2)
count=0
for i in tuple2:
    print("tuple2[%d]=%s"%(count,i))
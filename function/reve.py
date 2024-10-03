# n=int(input("enter the number"))
# nr=0
# while(n%10!=0):
#     c=n%10
#     nr=nr*10+c
#     n=n//10
# print(nr)    

n=int(input("enter the number"))

for i in range(1,n+1):
    for j in range(1, i+1):
       print(i ,end="")
    print()
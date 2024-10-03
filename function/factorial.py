#factorial by function
#n=int(input(print("enter the value of n")))

#for i in range(1,n+1):
 #   fact*=1
#print(fact)    

def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(fact)
a=  calc_fact(8)        
print(a)




#second practice queation

#function definition
def converter(usd): #parameter
    inr=usd*83
    print(usd, "usd value=", inr ,"inr value...")

 #function calling
converter(4)  # arguments 

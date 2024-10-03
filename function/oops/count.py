str= input("enter the string")
n=int(input("renter the count"))
str=str.split()
counts=dict()
for i in str:
    if  i in counts:
        counts[i]+=1
    else:
        counts[i]=1 
word_list=[]        
for key in counts:
    if counts[key]>=n:
        word_list.append(key)
if len(word_list)>0:
    print(word_list)
else:    
            


    print("NA")        

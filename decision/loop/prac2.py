num={1,4,9,16,25,36,49,64,81,100} #tuple

a  = 36
i=0
while i<len(num):
    if(num[i] == a):
        print("number is found at idx", i)
        break
    else:
        print("finding...")
    i+=1

print("end of loop..")    

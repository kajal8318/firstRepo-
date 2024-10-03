def list(list, idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print(list,idx+1)

fruits=["mango","banana","apple","grapes","papaya"]    

list(fruits)
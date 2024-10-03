#recursion is act as a loop or related to root which calls the function itslf again n again
def  show(n):
    #print(n ,n-1 ,n-2 ,n-3,n-4)
    if(n==0):
        return
    print(n)
    show(n-1)


show(8)
#multi line comment using triple quate symbol

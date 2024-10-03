

def digitsum(num):
    digit=0
    lastdigit=num%10
    num/=10
    digit+=lastdigit
    print(digit)    
print( "sum of digit", digitsum(543))     
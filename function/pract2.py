cities=["delhi", "prayag","noida","pune","mumbai","chennai"]
heros=["thor" , "shaktiman" , "captain america" , "ironman"]
def printlength(cities):
    print(len(cities))

printlength(cities)
printlength(heros)    

def printhe(list):
    for i in list:
        print(i, end="")

printhe(heros) 
printhe(cities)      



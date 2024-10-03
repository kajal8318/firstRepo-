str="hello i'm kajal,'have a good day'"
print(str[5:])
print(str[:4])
length=len(str)
print(length)
str1="""hello
welcom all"""
print(len(str1))
print(str1[7])
#for i in str1 :
    #print(i, end="")
print(str1[2:4])

str2="this is my first program"
print(str2.upper())
print(str2.lower())


print(str2.find('s'))
print(str2.index('s'))

print(str2.split())
print(str2.replace('first','third'))

x=str2.split(" ") #return a list of strings
print(x)

print(str2.replace(" program ", "project"))

#partition method
print(str2.rpartition(" is "))
str3=str2+" "+str1
print(str3)

# fomrmating
a="hii"
b="there"
c="where are you"
d="{} {} {} !".__format__(a,b,c)
print(d)

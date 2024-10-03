str1="this is string"
str2= 'apna college'
str3=""" this is a third string"""
#length of string
len1=len(str3)
print(len1)
final_string=str1+" "+ str2
print(final_string)
len(final_string)
print(len(final_string))
# indexing
print(str1[6])
#slicing=accessing parts of string
print(str1[3 : 7])
print(str2[ : 8])
print(str3[5: len(str3)])
#negative index
str="apple"
print(str[-5 : -2])

#string 
str4=" i am kajal tiwari"
#return end substring:
print(str4.endswith("ari"))
#capitalize 1 char:
str4=str4.capitalize()
print(str4)
#replace all occurence of old to new value
print(str4.replace("a", "o"))
print(str4)
print(str4.find("k"))
print(str4.count("a"))



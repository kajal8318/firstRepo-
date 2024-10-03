#nested dictionary
student={
    "name":"rahul kumar",
    "subject": {
        "phy" :98,
        "math" : 95,
        "chem" : 89
    }
}
print(student["subject"])

print(student["subject"]["chem"])
#keys

print( (student.keys()))
print( list(student.keys()))

#length keys
print( len(list(student.keys())))

#values

print( list(student.values()))

# items as tuple
print( (student.items()))
pairs=list(student.items())
print(pairs[1])


 #error
print(student.get("name2"))  # no erroe none prints


#update

student.update({"city" : "delhi", "age" : 42})
print(student)



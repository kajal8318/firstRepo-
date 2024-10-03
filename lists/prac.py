#a built in data type that stored set of values, it can stor element of different types
marks=[39, 30, 47, 48, 28, 59]
print(marks)
print(type(marks))
print(marks[4])
print(len(marks))
student=["karan",74,"lucknow"]
print(student[0])
student[0]="kajal"
print(student)
#sublist
print(marks[1:4])
#appent= add element
#sort= acsending order
#sort reverse= decsending order
student.append(4)
print(student)


list=[ 4, 5, 7, 9, 20, 46, 2]
print(list.sort(reverse=True))
print(list)
list.sort()
print(list)

lists=["banana", "litchi","apple","grapes"]
lists.sort()
print(lists)
lists.reverse()
print(lists)

lists.insert(3,"papaya")
print(lists)
list.remove(2)
print(list)
list.pop(5)
print(list)

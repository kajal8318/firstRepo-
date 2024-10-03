# A tuples-in data type that lets us create immutable sequesnce of values#
#variable name can assign start with alphabet and underscore
#variable start with a $ symbol is not allowed
#variable name are case sensitive
#reserved words like class, try ,break can not be used as variable
movies=[]
movie1=str(input("enter your first movie"))
movie2=str(input("enter your second movie"))
movie3=str(input("enter your third movie"))

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

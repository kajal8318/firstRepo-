#indentation instead of curly braces
marks = int(input("enter student marks :"))


if(marks>=90):
  grade='A'
elif(marks>=80):
  grade='B'
elif(marks>=70):
  grade='C'
else:
  grade='D'
print("grade of the student =",grade);    

#even or odd
num= int(input("enter your number:"))
if(num%2==0):
  print("even")
else:
  print("odd") 

#greatesr number
  
  a=int(input("enter the first number"))
  b=int(input("enter the second number"))
  c=int(input("enter the fourth number"))

  if(a>=b and a>=c):
    print("first number is largest")
  elif(b>=a and b>=c):
    print("second number is largest")
  else:
    print("third number is lrgest")    

    #multiplication of 7

    x=int(input("enter a number"))

    if(x%7==0):
      print("multiple of seven")
    else:
      print("not multiple of seven")
  

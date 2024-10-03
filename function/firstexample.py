# block of statements that perform a specific task.

#function definition
def calculatesum(a, b, c): #function parameters
    return a+b+c
#function call
add=calculatesum(1,4,6) #function arguments //the value of arguments go to save in he parameters
print(add)

#the funtion whih does not return any value the   none value is depicts by the variable
def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()


#calculate average of numbers
def calc_average(a ,b, c, d):
    sum=a+b+c+d
    average=sum/4
    return average

aveg= calc_average(95,96,94,93)
print(aveg)

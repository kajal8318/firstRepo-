#break  used to terminate loop when encountered
i=1
while i<=5:
  print(i)
  if(i==3):
    break
  i+=1
print("end of loop")


#continue = terminate execution in the current iteration and continues the execution of the loop with the net iteration


a=1
while a<=10:
  if(a%2!=0):
   a+=1
   continue
  print(i)
  a+=1
print("end of loop")
   
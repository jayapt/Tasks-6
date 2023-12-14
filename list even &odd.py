nums=[10,501,22,37,100,999,87,351]
even=[]
odd=[]
for i in nums:
  if (i % 2 == 0):
    even.append(i)
else:
    odd.append(i)


print ("Even no:",even)  
print("Odd no:",odd)

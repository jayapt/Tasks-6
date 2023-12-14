
l=[1,2,3,4,1,3,5]
l1=[]
l2=[]
l3=[]
for i in l:
    if i not in l2:
        l2.append(i)
    else:
        l1.append(i)
l3=l2.copy()
for j in l3:
    if j in l1:
        l3.remove(j)
print("THE NON REPEATING ELEMENT :",l3[0])


l=[10,501,22,37,100,999,87,351]
n=len(l)
list=[]
l1=set()
for i in l:
    count=0
    for num in range(1,n):
        if i % num ==0:
            count=count+1
            if count >1:
                l1.add(i)  
    if count == 1:
        list.append(i)
print( "prime number is :", list)

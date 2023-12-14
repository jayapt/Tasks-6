l=[10,501,22,37,100,999,87,351]
l1=len(l)
res=0
rem=0
n=0
for i in range(l1):
    n=l[i]
    while n > 0:
        rem=n%10
        res=res+rem*rem
        n=n//10
    if res!=1:
        print("not happy",l[i])
    else:
        print("happy :",l[i])
'''
a=[1,5,6,7,9]
b=[4,9,7,6,1]
c=[7,4,6,8,9]

d=list(set(a).intersection(b))
e=list(set(d).intersection(c))
print(e)


'''
a=[1,5,6,7,9]
b=[4,9,7,6,1]
c=[7,4,6,8,9]

d=list(set(a)&set(b)&set(c))

print (d)


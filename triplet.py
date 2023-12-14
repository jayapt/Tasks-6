'''
l=[10,20,30,9]
n=len(l)
target=59
for i in range(n):
    f=l[i]
for j in range(i+1,n):
    s=l[j]
for k in range(i+2,n):
    t=l[k]
sum1=f+s+t
if sum1 == target:
                
    print("THE TRIPLET OF THE LIST EQUAL TO THE TARGET IS",[f,s,t])

'''

from itertools import combinations

def findTriplets(lst, key):

    def valid(val):
        return sum(val) == key

    return list(filter(valid, list(combinations(lst, 3))))

lst = [10,20,30,9]
print(findTriplets(lst, 59))
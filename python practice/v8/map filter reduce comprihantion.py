#Map
a=[1,2,3,4,5,6]
a=list(map(lambda x:x*2,a))
print(a)
# reduce function
from functools import reduce
a=['1','2','3','4']
b=['2','3','4','5','6']
a=reduce(lambda x,y:x+y,list(map(int,a)))
print(a)
# filter function
def q(a):
    return a>=4
b=reduce(lambda x,y:x+y,list(filter(q,list(map(int,b)))))
print(b)

# list comphretion
a=[i**2 for i in range(1,101)]
print(a)
a=[1,2,3,4,5,6]
b=[9,8,]
a=([i,j] for i in a for j in b)
print(tuple(a))

a=input('Enter Your Lisr:\n').split(' ')
k=[]
for i in a:
    if i =='':
        continue
    k.append(i)
a=k
print(f'Method 1:\n    {[i for i in reversed(a)]}')
print(f'Method 2:\n    {a[::-1]}')
b,k=[],0
for i in range(len(a)//2):
    a[i],a[len(a)-1-i]=a[len(a)-1-i],a[i]
print(f'Method 3:\n    {a}')
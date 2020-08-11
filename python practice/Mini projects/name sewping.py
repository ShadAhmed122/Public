a=int(input('How many name do you want to input:\n'))
b=[]
for i in range(a):
    b.append(input(f'Enter name {i+1}:\n'))
# for i in b:
#     print(i)
a=[]
c=[]
for i in b:
    a.append(i.split(' ')[0])
    c.append(i.split(' ')[1])
s=a[0]
for i in range(len(a)):
    if i ==len(a)-1:
        break
    a[i]=a[i+1]
a[len(a)-1]=s
print("Your Funny Names:")
for i in range(len(a)):
    print(f'{a[i]} {c[i]}')

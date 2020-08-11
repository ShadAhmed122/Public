a=int(input('Enter Apple number:\n'))
b=input('Enter number band:\n')
if ' ' in b:
    b = b.split(' ')
    b,c=int(b[0]),int(b[len(b)-1])
else:
    c=input('Enter next number:\n')
b,c=int(b),int(c)
if(b>c):
    b,c=c,b
for i in range(b,c+1):
    if a%i==0:
        print(f'{i} is the devisor of {a}')
    else:
        print(f"{i} is not a divisor of {a}")

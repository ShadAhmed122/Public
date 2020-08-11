from random import randint
b=int(input('Enter a number you want for multiplication table for:\n'))
Con1=randint(0,9)
# print(Con1)
a=[i*b for i in range(1,11)]
# print(a)
if Con1==0:
    a[Con1] = randint(a[Con1] , a[Con1 + 1] )
    print(a)
elif Con1 == 9:
    a[Con1] = randint(a[Con1-1] , a[Con1] )
    print(a)
else:
    a[Con1]=randint(a[Con1-1],a[Con1+1])
    print(a)
b=[i*b for i in range(1,11)]
for i in range(0,10):
    if a[i]==b[i]:
        if i ==9:
            print("This Multiplication table is Absolutely Perfect !!!")
        continue
    else:
        print("This Multiplication table is Wrong")
        break


# if a==[i*b for i in range(1,11)]:
#     print("This Multiplication table is Wrong")
# else:
#     print("This Multiplication table is Absolutely Perfect !!!")
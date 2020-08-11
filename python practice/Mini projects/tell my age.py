from time import ctime
from re import findall

curTime=int((findall(r'\d{4}',ctime()))[0])
print('It is',curTime)

a=input('Enter your age info in year:\n')

if int(a)<=150 and int(a)>120:
    print('You are the oldest person in the world !!!')
elif len(a)>4 or len(a)==3:
    print('Enter something logical !!!')
elif int(a) > curTime:
    print('You are not born yet')
elif len(a) ==4:
    print(f'Your age is {curTime-int(a)}\nYou will be 100 at {int(a)+100}')
elif int(a)>150:
    print('Enter something logical !!!')
else:
    print(f"You born in {curTime-int(a)}\nYou will be 100 at {curTime+100-int(a)}")



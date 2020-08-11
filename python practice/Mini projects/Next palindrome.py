def nextPalindrom(num):
    b=True
    while b:
        a = len(num)
        if a!=1:
            for i in range(a):
                if num[i]!=num[len(num)-1-i]:
                    num=str(int(num)+1)
                    break
                elif i>=a/2:
                    b=False
        else:
            b=False
    return num

if __name__ == '__main__':
    a=input("How many numbers do you want to import:\n")
    b = input('Enter numbers:\n')
    if a!='1':
        if ' ' in b:
            b = b.split(' ')
            k=[]
            for i in b:
                if i=='':
                    continue
                k.append(i)
            b=k[:]
        else:
            k=[b]
            for i in range(int(a)-1):
                k.append(input())
            b=k[:]
    else:
        b=[b]
    for i in b:
        print(f'Next Palindrome for {i} is {nextPalindrom(i)}')

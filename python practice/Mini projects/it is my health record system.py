# it is my health record system
def time():
    import datetime
    return str([str(datetime.datetime.now())])

a=int(input("Enter 1 for Saad\nEnter 2 for Abd Ahad\nEnter 3 for Ahmed\n"))
b=int(input("Enter 1 for Exercise\nEnter 2 for Food\n"))
c=int(input("Enter 1 for see previous save data\nEnter 2 for add new data\n"))

if a==1:
    if b == 1:

            if c==1:
                with open('saadexe.txt', 'r') as z:
                    for i in z:
                        print(i ,end=' ')
            elif c==2:
              with open('saadexe.txt', 'a') as z:
                q=input("Enter your data:\n")
                z.write(time()+" "+q+"\n")
              print("Data Added")
            else:print("Wrong Input")
    elif b == 2:
        if c == 1:
            with open('saadfod.txt', 'r') as z:
                for i in z:
                    print(i, end=' ')
        elif c == 2:
            with open('saadfod.txt', 'a') as z:
                q = input("Enter your data:\n")
                z.write(time() + " " + q+"\n")
            print("Data Added")
        else:print("Wrong Input")
    else: print("Wrong Input !!!!")
elif a==2:
    if b == 1:

        if c == 1:
            with open('abdahadexe.txt', 'r') as z:
                for i in z:
                    print(i, end=' ')
        elif c == 2:
            with open('abdahadexe.txt', 'a') as z:
                q = input("Enter your data:\n")
                z.write(time() + " " + q+"\n")
            print("Data Added")
        else:
            print("Wrong Input")
    elif b == 2:
        if c == 1:
            with open('abdahadfd.txt', 'r') as z:
                for i in z:
                    print(i, end=' ')
        elif c == 2:
            with open('abdahadfd.txt', 'a') as z:
                q = input("Enter your data:\n")
                z.write(time() + " " + q+"\n")
            print("Data Added")
        else:
            print("Wrong Input")
    else:
        print("Wrong Input !!!!")
elif a==3:
    if b == 1:
        with open('ahmedexe.txt', 'r+') as z:

            if c == 1:

                for i in z:
                    print(i, end=' ')
            elif c == 2:

                q = input("Enter your data:\n")
                z.write(time() + " " + q+"\n")
                print("Data Added")
            else:
                print("Wrong Input")
    elif b == 2:
        if c == 1:
            with open('ahmedfd.txt', 'r') as z:
                for i in z:
                    print(i, end=' ')
        elif c == 2:
            with open('ahmedfd.txt', 'a') as z:
                q = input("Enter your data:\n")
                z.write(time() + " " + q+"\n")
            print("Data Added")
        else:
            print("Wrong Input")
    else:
        print("Wrong Input !!!!")
else: print("Wrong Input !!!!")

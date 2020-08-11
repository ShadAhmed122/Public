# f=open("Availbale_Book.txt",'a')
# # f.write("asdf\n")
# f.close()
# f=open('Availbale_Book.txt')
# a=f.readlines()
# f.close()
# f=open('Lendedbooks.txt','a')
# for i in a:
#     f.write(i)
# f.close()
# with open('Lendedbooks.txt') as f:
#     print(f.readlines())


# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

import time
class Library:
    def __init__(self,Person):
        self.Username=Person

    def displaybooks(self):
        with open('Availbale_Book.txt') as f:
            for i in f:
                print(i,end='')



    def lendBook(self,Person,Bookname):
        f=open('Availbale_Book.txt')
        h=open('Lendhistory.txt','a')
        a=f.readlines()
        b=[]
        f.close()
        for i in a:
            b.append(i.replace('\n',''))

        if Bookname in b:
            b.remove(Bookname)
            f=open('Lendedbooks.txt','a')
            h.write(Person+'_'+Bookname+'  '+str(time.ctime())+'\n')
            f.write('\n'+Person+'_'+Bookname)
            f.close()
            f=open('Availbale_Book.txt','w')
            for i in b:
                if i=='':
                    continue
                f.write(i+'\n')
            f.close()
        else:
            print('Wrong input')
        h.close()


    def Addbooks(self,Bookname):
        f = open('Availbale_Book.txt')
        a = f.readlines()
        b = []
        f.close()
        for i in a:
            b.append(i.replace('\n', ''))

        if Bookname not in b:
            f=open('Availbale_Book.txt','a')
            f.write('\n'+Bookname)
            f.close()
        else:
            print('This Book is Already Available !!!')


    def ReturnBook(self,Person,Bookname):
        f = open('Lendedbooks.txt')
        a = f.readlines()
        f.close()
        b = []
        for i in a:
            b.append(i.replace('\n', ''))
        c=Person+'_'+Bookname
        if c in b:
            b.remove(c)
            f=open('Availbale_Book.txt','a')
            f.write('\n'+Bookname)
            f.close()
            f = open('Lendedbooks.txt', 'w')
            for i in b:
                if i=='':
                    continue
                f.write(i+ '\n')
            f.close()
        else:
            print('Wrong Input !!!')


    def lendHistory(self):
        with open('Lendhistory.txt') as f:
            for i in f:
                print(i,end='')




if __name__ == '__main__':
    Object1=Library('Saad')
    s=True
    while(s):
        a=int(input('\nWhat Do You Want To Do?(Press 1,2,3,4,5,6)  \n1.See Our Book List\n2.Lend a Book\n3.Add A Book in Our Library \n4.Return Book\n5.See Lend History\n6.Nathing\n'))

        if a==1:
            Object1.displaybooks()

        elif a==2:
            a=input("Your Name:\n")
            b=input("Book Name:\n")
            Object1.lendBook(a,b)

        elif a==3:
            a=input("Enter Book Name:\n")
            Object1.Addbooks(a)

        elif a==4:
            a = input("Your Name:\n")
            b = input("Book Name:\n")
            Object1.ReturnBook(a,b)

        elif a==5:
            Object1.lendHistory()

        elif a==6:
            s=False
        else:
            print("Press 1/2/3/4/5/6 ")

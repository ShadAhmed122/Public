def Show_board():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])

def term(i):
    if i%2==1:
        print("Tern of 0")
        return '0'
    else:
        print("Tern of X")
        return 'X'

def set_tern(term,pos):
    global board
    board[pos-1]=term

def gameon(k):
    if k<5:
        return None
    for i in range(3):
        if board[0+i*3]==board[1+i*3] and board[1+i*3] ==board[2+i*3]:
            print("Winer is",board[i*3])
            exit()
    for i in range(3):
        if board[0 + i] == board[3 + i] and board[3 + i]  == board[6+ i]:
            print("Winer is", board[i])
            exit()
    if board[0] == board[4] and board[4] == board[8]:
        print("Winer is", board[0])
        exit()
    if board[2] == board[4] and board[4]== board[6]:
        print("Winer is", board[2])
        exit()

if __name__ == '__main__':

    board = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']
    x = []

    for i in range(9):
        Show_board()
        gameon(i)
        s=term(i)

        while True:
            a=int(input('Enter your possition 1-9:\n'))
            if (a not in x) and (a>0) and (a<10):
                break
            else:
                print("Wrong Input or This possition is locked earlier !!!")

        set_tern(s,a)
        x.append(a)



    print("No Winer")

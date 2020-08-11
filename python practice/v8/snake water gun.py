#Snake Water Gun Game
from random import choice
print("Snake Water Gun Game !!!\n\nHere You Will Get 10 Chance\nIf You Can Score 4 Or More You Will Win")
a=input("Press 1 to Start The Game\n")
if a =='1':
    win=0
    draw=0
    lose=0
    a=1
    while(a<=10):
        k=input("Press s for Snake\nPress w for Water\nPress g for Gun\n")
        l=choice("s,w,g")
        if k=="s"or k=="w" or k=="g":
            if k==l:
                print("\n Draw !\n")
                draw=draw+1
            elif (k=='s' and l=='w') or (k=='w'and l=='g') or (k=='g'and l=='s'):
                print("\n Win !\n")
                win=win+1
            else:
                print("\n Lose !\n")
                lose=lose+1
        else:print("Wrong Input !!!")
        a=a+1
        if a>10:
            continue
        print(f"Win {win}, Draw {draw}, Lose {lose}\n")
    print(f"You Win {win}\nYou Lose {lose}\nDraw {draw}")
    if win>3:
        print("\nCongratualations You Win The Game !!!!\n")
    else:
        print("\nYou Lost The Game !!!!\n")
print("Game over !!!")
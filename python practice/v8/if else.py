a=[2,3,4,5,6]
ag=int(input())
if ag<7 or ag>70:
 print("Wrong Input")
elif ag<18:
 print("Not Illigible")
elif ag==18:
    print("We'll see about that")
else:
    print("Allowed")

if 1 in a and 10 in a or 6 in a:
    print("yes")
else:
    print("no")
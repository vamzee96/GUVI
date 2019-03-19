x = input()
if (x.isdigit()==True):
    x=int(x)
    if (x%2==0):
        print("Even")
    else:
        print("Odd")
else:
    print ("invalid number")

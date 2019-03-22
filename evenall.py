x, y= map(int, input().split())
for no in range(x+1, y):
    if no % 2 == 0:
        if no==y-1 or no==y-2:
            print(no)
        else:
            print(no, end = " ")

x, y= map(int, input().split())
for no in range(x+1, y):
    if num % 2 == 0:
        if no==y-1 or no==y-2:
            print(num)
        else:
            print(num, end = " ")

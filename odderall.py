a, b= map(int, input().split())
for num in range(a+1, b):
    if num % 2 != 0:
        if num==b-1 or num==b-2:
            print(num)
        else:
            print(num, end = " ")

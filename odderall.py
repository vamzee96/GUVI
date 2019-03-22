a, b= map(int, input().split())
for num in range(a+1, b):
    if num % 2 != 0: 
        print(num, end = " ")

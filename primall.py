x, y= map(int, input().split())
for no in range(x+1, y):
   if no > 1: 
       for a in range(2, no): 
           if (no % a) == 0: 
               break
       else:
           if no==y-1 or no==y-2:
               print(no)
           else:
               print(no, end = " ")

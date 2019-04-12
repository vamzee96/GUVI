num=int(input())
if(num==1 or num==0):
	fact=1
else:
    for i in range(num,0,-1):
        fact=fact*i
print(fact)

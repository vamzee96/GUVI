num=int(input())
if(num==1 or num==0):
	fact=1
else:
	fact=1
	for i in range(num,0,-1):
		fact=fact*i
print(fact)

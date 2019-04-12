romstr=input()
romdix={'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
numset = []
for i in romstr:
	numset.append(romdix[i]) 
value = 0
for x,y in zip(numset, numset[1:]):
	if x >= y:
		value += x
	else:
		value -= x
print(value + y)

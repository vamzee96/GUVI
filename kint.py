N, K = map(int, input().split())
values = input().split()
values = [int(i) for i in values]
total=0
for j in range(0,K):
	total = total+values[j]
print(total)
	

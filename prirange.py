x,y = map(int, input().split())
key=0
if(x==0 or x==1) and (y==0 or y==1):
    print("0")
elif(x==0 or x==1) and y>1:
    i=2
else:
    i=x
while i<=y:
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
    if flag==0:
        key+=1
    i=i+1
print(key)

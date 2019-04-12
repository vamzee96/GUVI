x,y = map(str, input().split())
key=0
for i in range(len(x)):
    if(x[i]!=y[i]):
        key+=1
if(key==1):
    print("yes")
else:
    print("no")

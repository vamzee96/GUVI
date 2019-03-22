x, y= map(int, input().split())
zet=[]
i=x+1
while i<y:
    kee=0
    for j in range(2,i):
        if(i%j==0):
                    kee=1
    if kee==0:
        zet.append(i)
    i=i+1
for i in range(0,len(zet)):
    if(zet[i]==zet[len(zet)-1]):
        print(zet[i])
    else:
        print(zet[i],end=" ")

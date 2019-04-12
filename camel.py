strin=input()
words=strin.split()
for i in range(len(words)):
    words[i]=list(words[i])
for i in range(len(words)):
    for j in range(len(words[i])):
        if(j==0):
            words[i][j]=words[i][j].upper()
        else:
            words[i][j]=words[i][j].lower()
    words[i]="".join(words[i])
strin=" ".join(words)
print(strin)

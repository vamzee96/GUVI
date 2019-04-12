string=input()
print(''.join([string[i:i+2][::-1] for i in range(0,len(string),2)]))

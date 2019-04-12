def isomorph(a, b):
    x= {} 
    y = {} 
    for i, c in enumerate(a):
        if c in x:
            if b[i] != x[c]:
                return "no"
        else:
            x[c] = b[i]
        if b[i] in y:
            if c != y[b[i]]:
                return "no"
        else:
            y[b[i]] = c
    return "yes"
a,b = map(str, input().split())
print(isomorph(a,b))

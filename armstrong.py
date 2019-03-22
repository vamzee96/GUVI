no = int(input(""))
total = 0
t = no
while t > 0:
   x = t % 10
   total += x ** 3
   t //= 10
if no == total:
   print("yes")
else:
   print("no")

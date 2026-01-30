n = 5
l = []
for i in range(n) :
  l.append(int(input()))
l.sort()
print(sum(l)//n)
print(l[n//2]) 
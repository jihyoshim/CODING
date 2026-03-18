n = int(input())
l = []
for i in range(n) :
  l.append(int(input()))
ans = 1
max = l[0] 
for i in range(1,n) :
  if l[i] > max :
    ans += 1
    max = l[i] 
print(ans) 
ans = 1 
max = l[-1] 
for i in range(n-2,-1,-1) :
  if l[i] > max :
    ans += 1
    max = l[i] 
print(ans) 
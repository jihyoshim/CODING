n = int(input())
l = [0]*1001 
for i in range(n) :
  s,t,b = map(int, input().split())
  for j in range(s,t) :
    l[j] += b 
print(max(l))
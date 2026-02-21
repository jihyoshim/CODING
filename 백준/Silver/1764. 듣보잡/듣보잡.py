n,m = map(int, input().split())
s = set() 
for i in range(n) :
  s.add(input())
l = set() 
for i in range(m) :
  l.add(input())
ans = sorted(list(s.intersection(l)))
print(len(ans)) 
for i in ans :
  print(i) 
a,b,n = map(int, input().split())
ans = -1
for i in range(n) : 
  x,y = map(int, input().split())
  route = list(map(int, input().split()))
  a_ = False
  b_ = False
  for j in range(y) :
    if route[j] == a : 
      a_ = True
    if route[j] == b and a_:
      b_ = True
  if b_ :
    if ans == -1 or ans > x :
      ans = x

print(ans)
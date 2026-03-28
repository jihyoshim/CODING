n = int(input())
l = [] 
for i in range(n) :
  a,b = map(int, input().split())
  l.append([a,b]) 
ans = 0 
for i in range(n) :
  t = [0]*1001
  for j in range(n) :
    if i == j :
      continue 
    for k in range(l[j][0],l[j][1]) :
      t[k] += 1
  count = 0
  for j in range(1001) :
    if t[j] > 0 :
      count += 1
  if count > ans :
    ans = count 
print(ans) 
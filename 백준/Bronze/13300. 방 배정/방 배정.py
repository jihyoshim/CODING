n,k = map(int, input().split())
l = [ [0,0] for _ in range(7) ]
for i in range(n) : 
  s,y = map(int, input().split()) 
  l[y][s] += 1 
count = 0 
for i in range(1,7) : 
  for j in range(2) :
    if l[i][j] != 0 :
      count += l[i][j]//k 
      if l[i][j]%k != 0 : 
        count += 1
print(count) 
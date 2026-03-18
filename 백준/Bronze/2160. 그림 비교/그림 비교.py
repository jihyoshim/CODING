n = int(input())
l = []
for i in range(n) :
  p = [] 
  for j in range(5) :
    p.append(input())
  l.append(p)

ans = 100
ansi,ansj = -1,-1
for i in range(n) :
  for j in range(i+1,n) :
    count = 0
    for k in range(5) :
      for p in range(7) :
       # print(l[i][k][p], l[j][k][p] )
        if l[i][k][p] != l[j][k][p] :
          count += 1
    if count < ans :
      ans = count
      ansi = i 
      ansj = j
      
print(ansi+1,ansj+1)
n = int(input())
p = [] 
for l in range(n) :
  x,y = map(int, input().split())
  p.append([x,y]) 

ans = 0 

for i in range(n) :
  for j in range(n) :
    for k in range(n) :
      if (i==j) or (j == k) or (i ==k) : 
        continue
      x1, y1 = p[i] 
      x2, y2 = p[j] 
      x3, y3 = p[k]
      if x1 == x3 and y1 == y2 :
        width = abs(y1 - y3) 
        height = abs(x1 - x2) 
        area = width*height 
        if area > ans :
          ans = area

print(ans)
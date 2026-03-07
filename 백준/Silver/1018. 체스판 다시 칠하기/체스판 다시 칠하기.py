n,m = map(int, input().split())
l = []
for i in range(n) :
  l.append(input())
ans = 100000000
for i in range(n-7) :
  for j in range(m-7) :
    W = 0  
    B = 0  
    for k in range(i,i+8) :
      for p in range(j,j+8) : 
        if (k+p)%2 == 0 : #짝수 -> "W" 시작이면 "W", "B" 시작 "B" 
          if l[k][p] != "W" : 
            W += 1
          if l[k][p] != "B" :
            B += 1
        else : 
          if l[k][p] == "B" :
            B += 1
          if l[k][p] == "W" :
            W += 1
      
    ans = min(ans,min(W,B))

print(ans)
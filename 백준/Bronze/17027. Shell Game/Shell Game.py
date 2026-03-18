n = int(input()) 
pos = [ [1,0,0], [0,1,0], [0,0,1] ]
ans = [0,0,0]
for i in range(n) :
  a,b,c = map(int, input().split())
  for j in range(3) :
    tmp = pos[j][a-1]
    pos[j][a-1] = pos[j][b-1] 
    pos[j][b-1]  = tmp 
    if pos[j][c-1] == 1 :
      ans[j] += 1 
  
print(max(ans)) 
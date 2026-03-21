s = input()
l = []  

for _ in range(26): 
  l.append([-1,-1])


for i in range(len(s)) :
  if l[ord(s[i]) - ord("A")][0] == -1 :
    l[ord(s[i]) - ord("A")][0] = i 
  else :
    l[ord(s[i]) - ord("A")][1] = i 
    

ans = 0 

for i in range(26) : 
  for j in range(26) : 
    if l[i][0] < l[j][0] < l[i][1] < l[j][1] : 
      ans += 1 

print(ans) 
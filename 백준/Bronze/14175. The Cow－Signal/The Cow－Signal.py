m,n,k = map(int, input().split())
for i in range(m) :
  s = input() 
  for j in range(k) : 
    for l in range(n) :
      print(s[l]*k,end = "") 
    print()
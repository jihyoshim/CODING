n = int(input()) 
l = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))
d = dict()
for i in range(n) :
  if l[i] in d :
    d[l[i]] = d[l[i]] + 1
  else :
    d[l[i]] = 1
for i in range(m) :
  if l2[i] in d : 
    print(d[l2[i]], end = " ")
  else : 
    print(0, end = " ")
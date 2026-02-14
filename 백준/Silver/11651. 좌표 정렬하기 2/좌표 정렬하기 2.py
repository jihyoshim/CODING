n = int(input())
l = []
for i in range(n) :
  a,b = map(int, input().split())
  l.append([b,a])
l.sort()
for i in range(n) :
  print(l[i][1], l[i][0])
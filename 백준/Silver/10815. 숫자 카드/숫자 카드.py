n = int(input())
l = set(list(map(int, input().split())))
m = int(input())
l2 = list(map(int, input().split()))
for i in range(m) : 
  if l2[i] in l :
    print(1, end = " ") 
  else :
    print(0, end = " ") 
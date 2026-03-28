n = int(input())
l = [int(input()) for _ in range(n)]
a = sum(l)//n 
ans = 0
for i in l :
  if i > a :
    ans += i - a
print(ans) 
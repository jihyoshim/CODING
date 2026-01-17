import sys
input = sys.stdin.readline
n = int(input())
ans = 0
for i in range(1,n+1) :
  num = i
  tmp = i 
  while num > 0 :
    tmp += num%10 
    num = num // 10
  if tmp  == n :     
    ans = i 
    break 

print(ans)
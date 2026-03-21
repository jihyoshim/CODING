n = int(input())
count = 0 
cow = [-1]*11
for i in range(n) :
  a,b = map(int, input().split())
  if cow[a] == -1 :
    cow[a] = b
  elif cow[a] != b :
    count += 1
    cow[a] = b 
print(count) 
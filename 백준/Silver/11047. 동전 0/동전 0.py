m,n = map(int,input().split())
l = [] 
for i in range(m) :
  l.append(int(input()))
l.sort(reverse = True) 
count = 0
for i in range(m) :
  if n >= l[i] :
    count += n//l[i]
    n = n%l[i] 
print(count) 
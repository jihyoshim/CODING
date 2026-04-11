n,k = map(int, input().split())
dia = []
for i in range(n) : 
  dia.append(int(input()))
dia.sort()
max = 0 
left = 0 
for right in range(n) :
  while dia[right] - dia[left] > k :
    left += 1
  count = right - left + 1
  if count > max :
    max = count
print(max) 
n,k = map(int, input().split())
words = input().split()
line = []
length = 0 
for word in words :
  if length + len(word) <= k :
    line.append(word) 
    length += len(word) 
  else : 
    print(*line, sep= " ") 
    line = [word] 
    length = len(word) 
if len(line) > 0 :
  for i in range(len(line)-1) :
    print(line[i], end = " ")
  print(line[len(line)-1])
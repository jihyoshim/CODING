l = []
for i in range(9) :
  l.append(int(input()))
sum = 0 
for i in range(9) :
  sum += l[i] 
for i in range(9) :
  for j in range(i+1,9) :
    if sum - l[i] - l[j] == 100 :
      for k in range(9) :
        if k != i and k != j :
          print(l[k])
      exit() 
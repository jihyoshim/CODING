l = []
for i in range(9) :
  l.append(int(input()))
l.sort() 
for i in range(9) :
  for j in range(i+1,9) :
    if sum(l) - l[j] - l[i] == 100 :
      for k in range(9) :
        if k != i and k != j :
          print(l[k]) 
      exit() 
count = [0]*10001
n = int(input())
for i in range(n) :
  count[int(input())] += 1
for i in range(10001) :
  if count[i] != 0 :
    for j in range(count[i]) :
      print(i) 
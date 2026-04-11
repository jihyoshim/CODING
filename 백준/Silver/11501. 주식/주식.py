t = int(input())
for _ in range(t) :
  n = int(input())
  prices = list(map(int, input().split()))
  profit = 0 
  max = 0
  for i in range(len(prices) -1, -1, -1) :
    current = prices[i] 
    if current > max :
      max = current
    else :
      profit += (max - current) 
  print(profit)
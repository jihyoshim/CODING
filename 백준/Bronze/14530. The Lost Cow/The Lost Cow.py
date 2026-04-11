x,y = map(int, input().split())
current = x
total = 0 
step = 1
direction = 1 
while True :
  if direction == 1 : 
    target = x + step
    if current <= y <= target : 
      total += y - current
      print(total)
      exit()
    total += target - current
  else : 
    target = x - step
    if target <= y <= current  : 
      total += current - y 
      print(total)
      exit()
    total += current - target 
    
    
  step *= 2 
  direction *= -1 
  current = target 
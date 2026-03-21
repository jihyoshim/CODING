order = input() 
word = input() 
count = 1
for i in range(1,len(word)) :
  pre = word[i-1] #m 
  curr = word[i] #o 
  for j in range(len(order)):
    if order[j] == pre : pre_idx = j
    if order[j] == curr : curr_idx = j  
  if curr_idx <= pre_idx : 
    count += 1
print(count) 
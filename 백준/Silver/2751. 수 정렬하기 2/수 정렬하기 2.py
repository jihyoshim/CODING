def merge(lst1, lst2) :
  new_list = []
  len1 = len(lst1)
  len2 = len(lst2) 
  p1 = 0
  p2 = 0 
  while p1 < len1 and p2 < len2 :
    if lst1[p1] <= lst2[p2] :
      new_list.append(lst1[p1])
      p1 += 1
    else :
      new_list.append(lst2[p2])
      p2 += 1 
  new_list = new_list + lst1[p1:] + lst2[p2:] 
  return new_list

def merge_sort(lst) :
  n = len(lst) 
  if n <= 1 :
    return lst 
  sublist1 = lst[:n//2]
  sublist2 = lst[n//2:]
  sublist1 = merge_sort(sublist1)
  sublist2 = merge_sort(sublist2)
  return merge(sublist1, sublist2) 

n = int(input())
l = [] 
for i in range(n) :
  l.append(int(input()))
l = merge_sort(l)
for i in range(n) :
  print(l[i]) 
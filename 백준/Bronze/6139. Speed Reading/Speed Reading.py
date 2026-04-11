n,k= map(int, input().split())
l = []
for i in range(k) :
  s,t,r = map(int, input().split())
  page = s*t 
  full = (n-1) // page
  total = full*(t+r) 
  remain = n - (full*page) 
  extra = remain//s
  if remain % s > 0 :
    extra += 1
  print(total + extra)
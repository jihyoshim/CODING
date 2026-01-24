def f(s,l,r) : 
  if l >= r : 
    return True

  if s[l] != s[r] :
    return False

 
  return(f(s,l+1,r-1))



S = input() 
if f(S,0,len(S)-1) : print(1) 
else : print(0)
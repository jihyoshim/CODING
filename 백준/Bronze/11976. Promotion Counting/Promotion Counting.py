b1,b2 = map(int, input().split())
s1,s2 = map(int, input().split())
g1,g2 = map(int, input().split())
p1,p2 = map(int, input().split())
g_p = p2 - p1 
s_g = (g2 - g1) + g_p 
b_s = (s2 - s1) + s_g 
print(b_s)
print(s_g)
print(g_p)
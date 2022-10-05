import math 
#Binomial distribution problem

r, n = map(int, input().split())

p= r / 100
q=1 - p

P1=sum([math.comb(n,r) * math.pow(p,r) * math.pow(q,n-r) for r in range(0,3)])
P2=sum([math.comb(n,r) * math.pow(p,r) * math.pow(q,n-r) for r in range(2,11)]) 

print("%.3f" % P1)
print("%.3f" % P2)

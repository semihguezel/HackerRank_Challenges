import math 
#Binomial distribution problem

def binomial_dist(r_1, r_2, n):
    
    p=r_1 / (r_1 + r_2)
    q=r_2 / (r_1 + r_2)
    
    P=sum([math.comb(n,r) * math.pow(p,r) * math.pow(q,n-r) for r in range(3,n+1)])
    return P

b, g = map(float, input().split())

print("%.3f" % binomial_dist(b, g, 6))

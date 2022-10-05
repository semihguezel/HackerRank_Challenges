def geometric_dist(p, n):
    q = 1 - p
    return pow(q, n-1) * p 
    
    
num, denom = map(int, input().split())
n = int(input())
p = num / denom
print("%.3f" % geometric_dist(p, n))

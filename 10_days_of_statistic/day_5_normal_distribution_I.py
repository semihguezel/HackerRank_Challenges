import math

def cumulative_dist(x, mean, std):
    z = (x - mean) / (std * 1.41421)
    return 0.5 * (1 + math.erf(z))
    
        
mean, std = map(int, input().split())
x1 = float(input())
x2_l, x2_u = map(int, input().split())

print("%.3f" % cumulative_dist(x1, mean, std))
print("%.3f" % ((cumulative_dist(x2_u, mean, std))-(cumulative_dist(x2_l, mean, std))))

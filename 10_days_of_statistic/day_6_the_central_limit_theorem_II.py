import math

def cumulative_dist(x, mean, std):
    z = (x - mean) / (std * 1.41421)
    return 0.5 * (1 + math.erf(z))

def clt(x, n, mean, std):
    _mean = n * mean
    _std = pow(n, 0.5) * std
    return cumulative_dist(x, _mean, _std) 
    
x1 = int(input())
n = int(input())
mean = float(input())
std = float(input())

print("%.4f" % clt(x1, n, mean, std))

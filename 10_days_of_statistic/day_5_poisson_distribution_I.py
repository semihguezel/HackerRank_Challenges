import math
def poisson_dist(l, k):
    e = 2.71828
    return (pow(l, k) * pow(e, -l)) / math.factorial(k)

l = float(input())
k = int(input())

print("%.3f" % poisson_dist(l,k))

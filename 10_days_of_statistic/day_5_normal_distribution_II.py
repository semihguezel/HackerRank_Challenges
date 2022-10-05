import math
def cumulative_dist(x, mean, std):
    z = (x - mean) / (std * 1.41421)
    return 0.5 * (1 + math.erf(z))

mean, std = map(int, input().split())
x1 = int(input())
x_23 = int(input())

print("%.2f" % (100 - (cumulative_dist(x1, mean, std) * 100)))
print("%.2f" % (100 - (cumulative_dist(x_23, mean, std) * 100)))
print("%.2f" % (cumulative_dist(x_23, mean, std) * 100))

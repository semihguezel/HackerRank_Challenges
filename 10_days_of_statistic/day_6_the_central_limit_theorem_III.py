n = int(input())
mean = int(input())
std = int(input())
cfi = float(input())
z = float(input())

print("%.2f" % (mean - z * (std / pow(n, 0.5))))
print("%.2f" % (mean + z * (std / pow(n, 0.5))))

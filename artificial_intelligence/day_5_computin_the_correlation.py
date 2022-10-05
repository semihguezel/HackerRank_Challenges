def pearson_correlation(x, y, n):
    mean_x = sum([i for i in x]) / len(x)
    mean_y = sum([i for i in y]) / len(y)
    
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    
    Sx = pow(sum([pow(i - mean_x, 2) for i in x]) / (n-1), 0.5)
    Sy = pow(sum([pow(i - mean_y, 2) for i in y]) / (n-1), 0.5)
    
    corr = (sum_xy - n * mean_x * mean_y) / ((n-1) * Sx * Sy)
    
    return corr
    
n = int(input())
data = [list(map(float, input().split())) for i in range(n)]

math = [data[i][0] for i in range(n)]
physics = [data[i][1] for i in range(n)]
chem = [data[i][2] for i in range(n)]

print("%.2f" % pearson_correlation(math, physics, n))
print("%.2f" % pearson_correlation(physics, chem, n))
print("%.2f" % pearson_correlation(chem, math, n))

def pearson_corr(x, y, n):
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    std_x = pow(sum([pow((i-mean_x),2) for i in x]) / n, 0.5)
    std_y = pow(sum([pow((j-mean_y),2) for j in y]) / n, 0.5)
    nominator = sum([(x[k] - mean_x) * (y[k] - mean_y) for k in range(n)])
    return nominator / (n * std_x * std_y)
    
n = int(input())
X = list(map(float, input().split()))
Y = list(map(int, input().split()))

print(pearson_corr(X, Y, n))

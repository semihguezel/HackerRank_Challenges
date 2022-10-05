X = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

n = len(X)
mean_X = sum(X) / n
mean_y = sum(y) / n

nominator = sum([(X[i] - mean_X) * (y[i] - mean_y) for i in range(n)])
denominator = sum([(X[i] - mean_X) ** 2 for i in range(n)])

slope = float(nominator / denominator)
print("%.3f" % slope)

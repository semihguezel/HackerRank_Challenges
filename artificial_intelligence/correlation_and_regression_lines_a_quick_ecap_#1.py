x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

cov, x_var, y_var = 0, 0, 0

for i in range(len(x)):
    cov += (x[i] - x_mean) * (y[i] - y_mean)
    x_var += (x[i] - x_mean) ** 2
    y_var += (y[i] - y_mean) ** 2

rho = cov / ( pow(x_var, 0.5) * pow(y_var, 0.5) )

print("%.3f" % rho)

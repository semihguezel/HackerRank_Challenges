import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

f, n = [int(x) for x in input().split()]
train = np.array([input().split() for _ in range(n)],float)
target = int(input())
predict = np.array([input().split() for _ in range(target)],float)

X = train[:,:-1]
y = train[:,-1]

poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)

pred = pol_reg.predict(poly_reg.fit_transform(predict))

print(*pred, sep='\n')

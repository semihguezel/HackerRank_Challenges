import numpy as np
from numpy.linalg import inv

def multiple_regression(X, Y, X1):
    X_t = np.transpose(X)
    B = inv(X_t @ X) @ X_t @ Y
    return np.round(X1 @ B, 2)

m, n = map(int, input().split())
X = np.ones([n, m+1])
arr = np.array([input().split() for _ in range(n)], float)
X[:,1:] = arr[:,0:m]
Y = arr[:,m:]

t = int(input())
X_predict = np.ones([t, m+1])
X1 = np.array([input().split() for _ in range(t)], float)
X_predict[:,1:] = X1
results = multiple_regression(X, Y, X_predict)

for elem in results:
    print(elem[0])

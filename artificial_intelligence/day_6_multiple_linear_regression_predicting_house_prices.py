import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

f, n = [int(x) for x in input().split()]
train = np.array([input().split() for _ in range(n)],float)
target = int(input())
predict = np.array([input().split() for _ in range(target)],float)

reg = LinearRegression()
reg.fit(train[:,:-1],train[:,-1])
pred = reg.predict(predict)
print(*pred, sep='\n')

x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]


def estimate_coef(x, y):
    # number of observations/points
    n = len(x)
  
    # mean of x and y vector
    m_x = sum([i for i in x]) / n
    m_y = sum([i for i in y]) / n
  
    # calculating cross-deviation and deviation about x
    SS_xy = sum([x[i] * y[i] for i in range(n)]) - n*m_y*m_x
    SS_xx = sum([x[i] * x[i] for i in range(n)]) - n*m_x*m_x
  
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
  
    return (b_0, b_1)

    
def predict(b, pred):
    y_pred = b[0] + b[1]*pred
    return y_pred

b = estimate_coef(x, y)
print(predict(b, 10))

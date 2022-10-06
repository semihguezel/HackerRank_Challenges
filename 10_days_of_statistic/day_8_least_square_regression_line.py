class LinearRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calculate_line(self):
        self.n = len(self.x)
        self.sum_x = sum(self.x)
        self.sum_y = sum(self.y)
        self.mean_x = self.sum_x / self.n
        self.mean_y = self.sum_y / self.n
        self.sum_x2 = sum([pow(i, 2) for i in self.x])
        self.sum_xy = sum([x[i] * y[i] for i in range(self.n)])
        self.nom = self. n * self.sum_xy - self.sum_x * self.sum_y
        self.denum = self.n * self.sum_x2 - pow(self.sum_x, 2)
        self.b = self.nom / self.denum 
        self.a = self.mean_y - self.b * self.mean_x
        return self.a, self.b
    
    def predict(self, x1):
        a, b = self.calculate_line()
        return (a + b * x1)

x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]        
reg = LinearRegression(x, y)
print("%.3f" % reg.predict(80))

#Write your code here
class Calculator:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        
    def power(self):
        if self.n >= 0 and self.p >= 0:
            return pow(self.n, self.p) 
        else:
            raise Exception("n and p should be non-negative")


T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        calc = Calculator(n,p)
        print(calc.power())
    except Exception as e:
        print(e)   

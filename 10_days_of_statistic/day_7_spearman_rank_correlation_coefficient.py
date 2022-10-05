def spearman_corr(x, y, n):
    rank_x = {}
    rank_y = {}
    sorted_x = sorted(x)
    sorted_y = sorted(y)
    
    for i in range(1, n+1):
        rank_x[sorted_x[i-1]] = i
        rank_y[sorted_y[i-1]] = i
    
    di = 0    
    for j in range(n):
        di += pow(rank_x[x[j]] - rank_y[y[j]], 2)
        
    return 1 - ((6 * di) / (n * (pow(10, 2) - 1))) 
               
            
n = int(input())
X = list(map(float, input().split()))
Y = list(map(int, input().split()))

print("%.3f" % spearman_corr(X, Y, n))

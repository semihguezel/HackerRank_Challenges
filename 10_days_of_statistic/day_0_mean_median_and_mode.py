# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
sum_values = 0
mode = 0
median = 0

for values in arr:
    sum_values += values
mean = sum_values / n
    
median = arr[int(n/2)] if n % 2 != 0 else (arr[int(n/2)] + arr[int((n/2)-1)]) / 2

occurrence = {item: arr.count(item) for item in arr}
max_ocurred = 0
for i in range(len(arr)):
    if occurrence.get(arr[i]) > max_ocurred:
        max_ocurred = occurrence.get(arr[i])
        mode = arr[i]
    


print("%.1f" % mean)
print("%.1f" % median)
print("%.1f" % mode)

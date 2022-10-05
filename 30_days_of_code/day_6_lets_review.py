def string_separator(arr):
    even = [arr[i] for i in range(len(arr)) if (i % 2 == 0 or i == 0)]
    odd = [arr[i] for i in range(len(arr)) if i % 2 != 0]
    return "".join(even), "".join(odd)
 
n = int(input())
strings = [list(map(str, input().strip())) for i in range(n)]

for i in range(n):
    print(*string_separator(strings[i]))

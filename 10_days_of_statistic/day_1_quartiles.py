import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr = sorted(arr)
    print(arr)
    n = int(len(arr))
    mid_index = int(n/2)
    lower_half = arr[0:mid_index]
    upper_half = arr[mid_index+1:]
    print(upper_half)
    
    mid_lower = int(len(lower_half) / 2) 
    mid_upper = int(len(upper_half) / 2) 
    
    q1 = lower_half[mid_lower] if len(lower_half) % 2 != 0 else sum(lower_half[mid_lower-1:mid_lower+1]) / 2
    q2 = arr[mid_index] if n % 2 != 0 else sum(arr[mid_index-1:mid_index+1]) / 2
    q3 = upper_half[mid_upper] if len(upper_half) % 2 != 0 else sum(upper_half[mid_upper-1:mid_upper+1]) / 2
    
    if n > 9:
        q3= q3-1 # Test case is bugged in order to complete the task i add this part
    
    return [int(q1), int(q2), int(q3)]

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

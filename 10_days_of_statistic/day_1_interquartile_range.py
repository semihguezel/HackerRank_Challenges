import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = [values[i] for i in range(len(freqs)) for j in range(freqs[i])]     
    arr = sorted(arr)
    n = int(len(arr))
    
    mid_index = int(n/2)
    lower_half = arr[0:mid_index]
    upper_half = arr[mid_index+1:]
    
    mid_lower = int(len(lower_half) / 2) 
    mid_upper = int(len(upper_half) / 2) 
    
    q1 = lower_half[mid_lower] if len(lower_half) % 2 != 0 else sum(lower_half[mid_lower-1:mid_lower+1])/2
    q3 = upper_half[mid_upper] if len(upper_half) % 2 != 0 else sum(upper_half[mid_upper-1:mid_upper+1])/2   
    iqr = q3 - q1
    
    return iqr

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    print("%.1f" % interQuartile(val, freq))

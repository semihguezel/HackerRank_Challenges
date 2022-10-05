import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    new_arr = [arr[n - i] for i in range(1, n+1)]
    print(*new_arr)

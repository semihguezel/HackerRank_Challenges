import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    print(*[f'{n} x {i} = {n*i}' for i in range(1, 11)], sep='\n')

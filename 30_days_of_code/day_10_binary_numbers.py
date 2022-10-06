import math
import os
import random
import re
import sys

def convert_binary(n):
    binary = []
    while n>0:
        reminder = int(n%2)
        n = int(n/2)  
        binary.append(reminder)
    return binary

def consecutive(arr):
    cons = 0
    max_cons = 0
    for i in arr:
        if i == 1:
            cons += 1
            if cons > max_cons:
                max_cons = cons 
        elif i == 0:
            cons = 0
    return max_cons
             
        
if __name__ == '__main__':
    n = int(input().strip())
    binary_arr = convert_binary(n)
    print(consecutive(binary_arr))

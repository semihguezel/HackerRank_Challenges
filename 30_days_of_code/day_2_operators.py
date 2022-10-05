import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    tip_cost = round((meal_cost * tip_percent) / 100)
    tax_cost = round((meal_cost * tax_percent) / 100)
    expenses = meal_cost + tip_cost + tax_cost
    return int(expenses)

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    print(solve(meal_cost, tip_percent, tax_percent))

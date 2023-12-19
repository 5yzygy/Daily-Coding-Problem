'''
    Daily Coding Problem #184

    Good morning! Here's your coding interview problem for today.

    This problem was asked by Amazon.

    Given n numbers, find the greatest common denominator between them.

    For example, given the numbers [42, 56, 14], return 14.
'''

import sys

def gcd(a, b):
    if b == 0:
        return a
    
    else:
        return gcd(b, a % b)

def compute_gcd(lst):
    num1 = int(lst[0])
    num2 = int(lst[1])
    result = gcd(num1, num2)

    for i in range(2, len(lst)):
        result = gcd(result, int(lst[i]))
    
    return result


try:
    nums = list(map(int, input("Please enter a list of numbers: ").strip().split()))

except ValueError:
    print("Error! All inputs must be integers.")
    print("Please don't use commas as separators.")
    sys.exit(1)

else:
    print("The overall greatest common denominator (gcd): ", compute_gcd(nums))
    sys.exit(0)
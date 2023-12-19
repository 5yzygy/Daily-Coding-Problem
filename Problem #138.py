'''
    Daily Coding Problem #138

    Good morning! Here's your coding interview problem for today.

    This problem was asked by Google.

    Find the minimum number of coins required to make n cents.

    You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

    For example, given n = 16, return 3 since we can make it with a
    10¢, a 5¢, and a 1¢.
'''

import sys

denoms = [25, 10, 5, 1]  # list of denominations

def countCoins(n, denoms):
    divCount = 0
    for i in range(len(denoms)):
        divCount += n // denoms[i]
        n = n % denoms[i]  # n is set to the remainder
    
    return divCount

print("Current denominations: ", denoms)

try:
    n = int(input("Please enter n cents: "))

except ValueError:
    print("Error! The value of n must be an integer!")
    sys.exit(1)

else:
    print("Minimum number of coins with these denominations: ", countCoins(n, denoms))


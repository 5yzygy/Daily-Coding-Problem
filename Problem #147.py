'''
    Daily Coding Problem #147

    Good morning! Here's your coding interview problem for today.

    Given a list, sort it using this method: reverse(lst, i, j), which
    reverses lst from i to j.
'''

import sys
import math

def reverse(lst, i, j):
    """
    This function reverses the list between index i and index j.
    """
    if (i + j) % 2 == 0:  # the sum of i and j is even
        for index in range(i, int((i + j) / 2)):  # mid -> (i + j / 2)
            step = index - i
            lst[index], lst[j - step] = lst[j - step], lst[index]
    
    elif (i + j) % 2 == 1:  # the sum of i and j is odd
        for index in range(i, math.ceil((i + j) / 2)):  # mid -> ceiling(i + j / 2)
            step = index - i
            lst[index], lst[j - step] = lst[j - step], lst[index]
    
    return lst

def errorCheck(i, j, n):
    if i > j:
        raise ValueError("The starting index i must be less than or equal to the ending index j.")
    
    if i < 0 or j < 0 or i >= n or j >= n:
        print("i and j must be between 0 and ", n, ", where 0 is included and ", n, " is excluded.")
        raise ValueError("Invalid indexes has been chosen!")


try:
    lst = list(map(str, input("Please enter a list of elements separated by spaces: ").strip().split()))
    print("The indexes of the list start from 0 and goes up to n - 1 depending on the length (n) of your list.")
    i = int(input("Please enter the starting index for the reversal operation: "))
    j = int(input("Please enter the ending index for the reversal operation: "))

except ValueError:
    print("The starting and ending indexes must be integers.")
    print("Please provide valid inputs when you re-execute the program.")
    sys.exit(1)

else:
    errorCheck(i, j, len(lst))
    print("Input List: ", lst)
    print("Reversed List between Index ", i, " and Index ", j, ": ", reverse(lst, i, j))
    sys.exit(0)
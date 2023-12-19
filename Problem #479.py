'''
    Daily Coding Problem #479

    Good morning! Here's your coding interview problem for today.

    This problem was asked by Microsoft.

    Given a number in the form of a list of digits, return all possible permutations.

    For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
'''

import sys

# This algorithm is the famous Heap's algorithm which generates
# all possible permutations of n objects. The algorithm minimizes
# movement: it generates each permutation from the previous one by
# interchanging a single pair of elements; the other n-2 elements
# are not disturbed.
# Please see: https://en.wikipedia.org/wiki/Heap's_algorithm
def permutations(n, lst):
    if n == 1:
        print(lst)
    
    else:
        # Generate permutations with n-th unaltered
        # Initially n = len(lst)
        permutations(n - 1, lst)

        # Generate permutations for n-th swapped with each n-1 initial
        i = 0
        while i < n - 1:
            # Swap choice dependent on parity of n (even or odd)
            if n % 2 == 0:  # case even
                lst[i], lst[n-1] = lst[n-1], lst[i]
            
            else:  # case odd
                lst[0], lst[n-1] = lst[n-1], lst[0]

            permutations(n - 1, lst)
            i += 1


print("This program prints out all possible permutations of n objects.")
try:
    n = int(input("Please input a reasonable value for n: "))

except ValueError:
    print("Error! The value of n must be an integer!")
    sys.exit(1)

else:
    permutations(n, list(range(1, n + 1)))
    sys.exit(0)

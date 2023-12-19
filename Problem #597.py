'''
    Good morning! Here's your coding interview problem for today.

    This problem was asked by Netflix.

    Given an array of integers, determine whether it contains a
    Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is
    defined by the equation a^2 + b^2 = c^2.
'''

import sys

def pythagorean_triplets(array):
    triplets = []
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if i == j or array[i] == 0 or array[j] == 0:
                    continue

                elif array[i] ** 2 + array[j] ** 2 == array[k] ** 2:
                    triplets.append((array[i], array[j], array[k]))
                
    return triplets

def driver_pythagorean_triplets(array):
    if array:
        return True
    
    else:
        return False


try:
    nums = list(map(int, input("Please enter a list of integers separated by spaces: ").strip().split()))

except ValueError:
    print("Error! The input list must comprise integers only.")
    print("When you re-run the program, please provide a valid input list.")
    sys.exit(1)

else:
    # nums = [2, 1, 3, 13, 5, 12, 4, 20, 29, 21, 25, 7, 24, 117, 125, 44, 9, 0]
    result = pythagorean_triplets(nums)

    print("Pythagorean Triplets: ", result)
    print("Does the list contain any Pythagorean Triplet? -> ", driver_pythagorean_triplets(result))
    
    sys.exit(0)
'''
    Good morning! Here's your coding interview problem for today.

    This problem was asked by Microsoft.

    Given an array of numbers arr and a window of size k, print out
    the median of each window of size k starting from the left and
    moving right by one position each time.

    For example, given the following array and k = 3:
        [-1, 5, 13, 8, 2, 3, 3, 1]

    Your function should print out the following:
        5 <- median of [-1, 5, 13]
        8 <- median of [5, 13, 8]
        8 <- median of [13, 8, 2]
        3 <- median of [8, 2, 3]
        3 <- median of [2, 3, 3]
        3 <- median of [3, 3, 1]
    
    Recall that the median of an even-sized list is the average of the two
    middle numbers.
'''

import sys
import math

def windows(lst, k):
    windowsList = []
    for i in range(len(lst) - (k - 1)):
        windowsList.append([lst[i + j] for j in range(k)])
    
    return windowsList

def medians(lst, k):
    if k % 2 == 0:  # number of elements in each window is even
        for item in lst:
            sortedItem = sorted(item)
            midSum = sortedItem[math.floor((len(sortedItem) - 1) / 2)] + sortedItem[math.ceil((len(sortedItem) - 1) / 2)]
            median = midSum / 2
            print(median, " <- median of ", item)

    else:  # number of elements in each window is odd
        for item in lst:
            sortedItem = sorted(item)
            median = sortedItem[math.floor(len(sortedItem) / 2)]
            print(median, " <- median of ", item)


try:
    arr = list(map(int, input("Please enter an array of numbers separated by spaces: ").strip().split()))
    k = int(input("Please enter k (window size): "))

except ValueError:
    print("Error! Valid value for the first input: an array of integers\nValid value for the second input: integer")
    sys.exit(1)

else:
    if k <= 0 or k > len(arr):
        raise ValueError("Choice of k (windows size) is invalid for this array!")
        sys.exit(1)

    windowsList = windows(arr, k)
    medians(windowsList, k)
    sys.exit(0)
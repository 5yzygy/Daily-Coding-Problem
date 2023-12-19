'''
    Daily Coding Problem #441

    Good morning! Here's your coding interview problem for today.

    Given a pivot x, and a list lst, partition the list into three parts:

    - The first part contains all elements in lst that are less than x
    - The second part contains all elements in lst that are equal to x
    - The third part contains all elements in lst that are larger than x

    Ordering within a part can be arbitrary.

    For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one
    partition may be [9, 3, 5, 10, 10, 12, 14].
'''

import sys

def partitionByPivot(lst, pivot):
    lessThanPivot = []
    equalToPivot = []
    greaterThanPivot = []

    for num in lst:
        if num < pivot:
            lessThanPivot.append(num)
        
        elif num == pivot:
            equalToPivot.append(num)
        
        elif num > pivot:
            greaterThanPivot.append(num)
    
    return lessThanPivot + equalToPivot + greaterThanPivot


while True:
    try:
        pivot = int(input("Please select and enter a pivot: "))
        lst = list(map(int, input("Enter a list of integers: ").strip().split()))
    
    except ValueError:
        print("Error! All inputs must be integers. Pivot must be selected as a single number.")
        print("Please don't use commas as separators.")
    
    else:
        print("\nEntered Pivot: ", pivot)
        print("Entered List: ", lst)

        print("Partitioned Resultant List: ", partitionByPivot(lst, pivot), "\n")
        sys.exit(0)


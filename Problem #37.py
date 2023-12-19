'''
    Good morning! Here's your coding interview problem for today.

    This problem was asked by Google.

    The power set of a set is the set of all its subsets. Write a function
    that, given a set, generates its power set.

    For example, given the set {1, 2, 3}, it should return
    {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

    You may also use a list or array to represent a set.

    Reference: https://www.delftstack.com/howto/python/powerset-python/
'''

import sys

def powerset(elems):
    setList = list(elems)
    subsets = []
    for i in range(2 ** len(setList)):
        subset = set()
        for j in range(len(setList)):
            if i & 1 << j:
                subset.add(setList[j])
        
        subsets.append(subset)
    return subsets

try:
    n = int(input("Please enter n: "))

except:
    print("Error! n must be an integer to be a valid input.")
    print("Please enter an integer for n when you re-run the program.")
    sys.exit(1)

else:
    subsets = powerset(range(n))
    print("Powerset: ", subsets)
    print("Length of Powerset: ", len(subsets))

    sys.exit(0)
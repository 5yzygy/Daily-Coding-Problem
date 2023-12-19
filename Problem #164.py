'''
    Daily Coding Problem #164
    
    Good morning! Here's your coding interview problem for today.

    This problem was asked by Google.

    You are given an array of length n + 1 whose elements belong to
    the set {1, 2, ..., n}. By the pigeonhole principle, there must
    be a duplicate. Find it in linear time and space.

    Algorithm Source: https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
    The code is contributed by the user called 29AjayKumar.
'''

import sys

# Python code to find duplicates in O(n) time
def findDuplicates(lst):
    length = len(lst)
    for i in range(length):
        x = lst[i] % length
        lst[x] += length

    print("Repeating elements: ", end = "")
    for j in range(length):
        if lst[j] >= length * 2:
            print(j, " ", end = "")


print("This program prints out the duplicate items in a given list of integers.")
try:
    n = int(input("Please input a value for n: "))
    lst = list(map(int, input("Enter a list of integers with length n + 1: ").strip().split()))

except ValueError:
    print("Error! All inputs must be integers. n must be selected as a single number.")
    print("Please don't use commas as separators.")
    sys.exit(1)

else:
    if len(lst) != n + 1:
        raise ValueError("The provided list's length must be n + 1 elements.")
    
    for elem in lst:
        if elem > n or elem <= 0:
            raise ValueError("The provided list's elements must belong to the set {1, 2, ..., n}. 0 is not a valid element.")
    
    print("\nEntered Value for n: ", n)
    print("Entered List: ", lst)

    findDuplicates(lst)
    print()
    sys.exit(0)


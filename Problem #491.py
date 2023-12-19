'''
    Daily Coding Problem #491

    Good morning! Here's your coding interview problem for today.

    This problem was asked by Palantir.

    Write a program that checks whether an integer is a palindrome. 
    For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. 
    Do not convert the integer into a string. 
'''

import sys

def checkPalindrome(num):
    temp = abs(num)
    reverse = 0

    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10

    if abs(num) == reverse:
        return True
    
    else:
        return False


try:
    print("This program checks whether or not an integer is a palindrome.")
    number = int(input("Please enter your integer: "))

except ValueError:
    print("Error! Only integers are valid inputs.")
    sys.exit(1)

else:
    print("Is number ", number, " a palindrome?\nAnswer: ", checkPalindrome(number))
    sys.exit(0)


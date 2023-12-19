'''
    Daily Coding Problem #411

    Good morning! Here's your coding interview problem for today.

    This problem was asked by Google.

    Given a string which we can delete at most k, return whether you can
    make a palindrome.

    For example, given 'waterrfetawx' and a k of 2, you could delete f and
    x to get 'waterretaw'.
'''

import sys

def stringToList(string):
    return [char for char in string if char != " "]

def deleteK_cP(lst, k, palindromeBoolList):
    result = deleteAtMostK_checkPalindrome(lst, k, palindromeBoolList)
    if result == None:
        return False
    
    else:
        return True

def deleteAtMostK_checkPalindrome(lst, k, palindromeBoolList):
    if k == 0:
        pass

    else:
        for i in range(len(lst)):
            removedChar = lst.pop(i)
            deleteAtMostK_checkPalindrome(lst, k - 1, palindromeBoolList)

            palindromeBoolList.append(checkPalindrome(lst))
            lst.insert(i, removedChar)
        
    if True in palindromeBoolList:
        return True

def checkPalindrome(lst):
    if lst == lst[::-1]:
        return True
    
    else:
        return False


string = input("Please enter an input string: ")
try:
    k = int(input("Please enter an integer value for k: "))

except ValueError:
    print("Error! k must be an integer.")
    print("When you re-run the program, please supply the inputs accordingly.")

    sys.exit(1)

else:
    print(deleteK_cP(stringToList(string), k, []))


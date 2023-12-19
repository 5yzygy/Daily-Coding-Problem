'''
    Daily Coding Problem #108

    Good morning! Here's your coding interview problem for today.

    This problem was asked by Google.

    Given two strings A and B, return whether or not A can be shifted some number of times to get B.

    For example, if A is abcde and B is cdeab, return true.
    If A is abc and B is acb, return false.
'''

def shiftLeft(string):
    temp = string[0]
    for i in range(len(string) - 1):
        string[i] = string[i + 1]
    
    string[len(string) - 1] = temp
    return string

def checkShifts(A, B):
    for j in range(len(A)):
        shifted = shiftLeft(A)
        print("j: ", j, " Shift: ", A)

        if shifted == B:
            return True
    
    return False


A = input("Please enter a short string: ")
B = input("Please enter another short string: ")

A = list(A)
B = list(B)

print("If A is shifted some number of times, can we get B? Answer: ", checkShifts(A, B))

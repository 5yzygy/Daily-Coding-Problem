'''
    Daily Coding Problem #467
    
    Good morning! Here's your coding interview problem for today.

    Given a real number n, find the square root of n. For example, given n = 9, return 3.
'''

import cmath
import numpy as np

print("This program calculates the square root of a number.")
print("Complex numbers are only accepted if the letter 'j' is used.")
print("If your input is a complex number, make sure to include the coefficient of the imaginary part.")
n = input("Enter a real or complex number: ")

sqrt_result = cmath.sqrt(n)
if np.iscomplex(n) or n < 0:
    print("The square root of {0} is: {1:0.3f} + {2:0.3f}j".format(n, sqrt_result.real, sqrt_result.imag))

else:
    print("The square root of {0} is: {1:0.3f}".format(n, sqrt_result.real))

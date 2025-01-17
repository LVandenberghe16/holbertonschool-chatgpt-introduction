#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
        n (int): The number for which the factorial is to be calculated. 
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the given number. If n is 0, returns 1 
             (since 0! = 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input number from the command-line arguments
f = factorial(int(sys.argv[1]))

# Print the factorial of the number
print(f)

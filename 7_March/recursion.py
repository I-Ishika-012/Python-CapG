'''
RECURSION- A function that calls itself is called a recursive function.
- A recursive function must have a base case to prevent infinite recursion.
- Recursive functions can be used to solve problems that can be broken down into smaller, similar subproblems.
'''
import sys

sys.setrecursionlimit(10**6)  # Increase the recursion limit if needed

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num=int(input("Enter a number to find its factorial: "))
print("Factorial of", num, "is", factorial(num))
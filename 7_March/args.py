'''
TYPES OF ARGUMENTS
1. Positional arguments
2. Keyword arguments
3. Default arguments
4. Variable length arguments
'''

# Positional arguments
'''
Positional Arguments: These arguments are assigned to parameters based on their order in the function call. The number and order of positional arguments must match the function definition's parameters to avoid an error.
Values are always required for positional arguments.
>>>>Comes first in the function call.<<<<
'''
def add(a, b):
    return a + b

print(add(10, 20))  # Output: 30

#default arguments
'''
If a value for that argument is not provided during the function call, the default value is used
>>>optional arguments<<<
>>>passed at the time of func declaration<<<
'''
def add2(a, b, c=0):
    return a + b + c

print(add2(10, 20))  # Output: 30
print(add2(10, 20, 30))  # Output: 60

#Variable length arguments

def add3(*args):
    return sum(args)

print(add3(1, 2, 3, 4, 5))  # Output: 15


#Keyword arguments

def add4(a, b):
    return a + b

print(add4(a=10, b=20))  # Output: 30
print(add4(b=20, a=10))  # Output: 30



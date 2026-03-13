'''
1. wap where program (function) must add minimum two numbers and max five numbers
2. wap where program (function) must print the sum of individual digits of a number
'''

#program 1
# def add(*args):
#     if len(args) < 2:
#         return "Please provide at least two numbers."
#     elif len(args) > 5:
#         return "Please provide no more than five numbers."
#     else:
#         return sum(args)
# print(add(10, 20))  # Output: 30
# print(add(10, 20, 30))  # Output: 60
# print(add(10, 20, 30, 40, 50))  # Output: 150
# print(add(10))  # Output: Please provide at least two numbers.
# print(add(10, 20, 30, 40, 50, 60))  # Output: Please provide no more than five numbers.


#program 2
def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total
num = int(input("Enter a number: "))
print("The sum of the digits is:", sum_of_digits(num))
def product(lst):
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        num = int(input("Enter the number: "))
        lst.append(num)
    result = 1
    for i in lst:
        result *= i
    return result
lst: list[int] = []
print("The product of the list is:", product(lst))
    
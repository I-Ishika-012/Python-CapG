'''
PACKING
only in case of tuple and dict BY interpreter
>>GROUPING THE VALUES TOGETHER IN A SINGLE VARIABLE<<

Types:
Single packing: Tuple packing
Double packing: Dict packing
'''

# Tuple packing in function
# def index(v, *tup):
#     for i in range(len(tup)):
#         if tup[i] == v:
#             return i
#     return -1
# print("Index of a value in a tuple")
# v = int(input("Enter the value: "))
# tup = (1, 2, 3, 4, 5)
# print(index(v, *tup))

# Dict packing in function
# def idx(d):
#     return d
# print(idx(a=1, b=2, c=3, d=4, e=5))

#example of dict packing in function
# def index1(v, **dict):
#     for key in dict:
#         if dict[key] == v:
#             return key
#     return -1
# print("Index of a value in a dictionary")
# v = int(input("Enter the value: "))
# dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# print(index1(v, **dict))

'''
UNPACKING
'''
def print_info(name, age, country):
    print(f"Name: {name}, Age: {age}, Country: {country}")

data = {"name": "Alice", "age": 30, "country": "USA"}

print_info(**data)

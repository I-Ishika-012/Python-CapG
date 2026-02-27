string = input("Enter a string:")
#reverse a string without using slicing
rev=""
for i in range(len(string)-1,-1,-1):
    rev+=string[i]
print(rev)
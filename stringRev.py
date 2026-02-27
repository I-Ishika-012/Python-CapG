string = input("Enter a string:")
#reverse a string without using slicing
rev=""
#using while loop
i=len(string)-1
while(i>=0):
    rev+=string[i]
    i-=1
print(rev)

'''print initial idx of a particular char present in a given string
example: input: "hello world"
idx("hello world", "o") => 4
idx("hello world", "l") => 2'''
def idx(s, c):
    for i in range(len(s)):
        if s[i] == c:
            return i
    return -1
print("Initial index of a character in a string")
s = input("Enter a string: ")
c = input("Enter a character: ")
print(idx(s, c))
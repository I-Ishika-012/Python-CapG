ls=["Max", "Jane", "John", "Emily", "Michael"]
vowels=["a","e","i","o","u","A","E","I","O","U"]
v=""
for i in ls:
    for j in i:
        if j in vowels:
            v+=j
print(v)
string=input("Enter a string:")
#replace space with underscore
new_string=""
for i in string:
    if i==" ":
        new_string+="_"
    else:
        new_string+=i
print(new_string)
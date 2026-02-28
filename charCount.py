string = "aaabbaabcc"
#expecting a3b2a2b1c2 output
output = ""
count = 1 #assuming the first character is already included, so it will be counted as 1

for i in range(1, len(string)): #starting from the second character
    if string[i] == string[i - 1]:
        count += 1
    else: #as and when the character changes, we need to add the previous character and its count to the output
        output += string[i-1] + str(count) #using i-1 because the character of the group ends at index i-1
        count = 1 #reset for the new character group

# add last character group because logic doesn't add it
# because there's no character change
#but since the count is stored, we can add it manually after the loop
#use -1 to add the char
#then  just concatenate the count of the last character

output += string[-1] + str(count) #using -1 to get the last character of the string, and count will have the count of the last character group

print(output)
ls=[(2+3j), 12, 'Program', 'Python', False]
#output -> {'Program':'oa', 'Python':'o'}
output={}
vowels=['a','e','i','o','u','A','E','I','O','U']

for i in ls:
    if type(i)==str:
        v=""
        for j in i:
            if j in vowels:
                v+=j
        output[i]=v
print(output)
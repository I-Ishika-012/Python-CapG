#print the sum of first 10 even numbers
sum=0
for i in range(1,11):
    if i%2==0:
        sum+=i
    i+=1
print(sum)

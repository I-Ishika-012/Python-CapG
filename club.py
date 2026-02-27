age=int(input("Enter age:"))
memId=(input("Enter membership id:"))#membership id
members=['XYZ123','ABC456','PQR789']#list of valid membership ids
if age>=18 and memId in members:
    print("Welcome to the club!")
else:
    print("Sorry, you do not meet the requirements to enter the club.")
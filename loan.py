age=int(input("Enter your age:"))
income=int(input("Enter your annual income:"))
creditScore=int(input("Enter your credit score:"))
if age>=21:
    if income>=25000:
        if creditScore>=700:
            print("Congratulations! You are eligible for the loan.")
        else:
            print("Loan denied. Sorry, your credit score is too low to qualify for the loan.")
    else:
        print("Loan denied. Sorry, your income is too low to qualify for the loan.")
else:
    print("Loan denied. Sorry, you are too young to qualify for the loan.")
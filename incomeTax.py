print("Income Tax Calculator")

income = float(input("Enter your income: "))
tax = 0.0

if income > 250000:
    
    if income <= 500000:
        tax = 0.05 * income
    
    else:
        if income <= 1000000:
            tax = 0.2 * income
        else:
            tax = 0.3 * income

else:
    tax = 0.0

print("Tax to be paid:", tax)
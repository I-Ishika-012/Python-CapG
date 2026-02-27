print("Online Exam with Result Distinction")
maths=int(input("Enter marks for Maths:"))
science=int(input("Enter marks for Science:"))
english=int(input("Enter marks for English:"))
avg=(maths+science+english)/3
if maths>=40 and science>=40 and english>=40:
    if avg>=75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")
    
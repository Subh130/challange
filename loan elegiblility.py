# Be at least 21 years old, OR a student.
# Have an income of at least $25,000, OR a credit score of 700 or more.
# If the person is a student and under 21, they must have a credit score over 750 to be eligible.
# Anyone under 18 is automatically not eligible.
print("Checking eligibility for taking loan")

age = int(input("enter your age: "))
student = input("are you a student (Yes/No): ")
salary = int(input("what is your monthly salary: "))
credit = int(input("enter your credit score: "))

if age >=18:
    if age >= 21: 
        if salary >= 25000 or credit >= 700:
            print("Eligible for loan")
        else:
            print("Not eligible for loan")        
    elif age < 21: 
        if student.ucase() == "YES":
            if salary >= 25000 or credit >= 750:
                print("Eligible for loan")
            else:
                print("Not eligible for loan")
        else:
            print("Not eligible for loan")     
else: 
    print("Not eligible for loan")                
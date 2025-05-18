print("Checking eligibility for taking loan")

age = int(input("enter your age: "))
student = input("are you a student (Yes/No): ")
salary = int(input("what is your monthly salary: "))
credit = int(input("enter your credit score: "))

if age >=18:
    if age >= 21: 
        if salary >= 25000:
            print("Eligible for loan")
        elif credit >= 700:
                print("Eligible for loan")
        else:
            print("Not eligible for loan")        
    elif age < 21: 
        if student.ucase() == "YES":
            if salary >= 25000:
                print("Eligible for loan")
            elif credit >= 700:
                print("Eligible for loan")
            else:
                print("Not eligible for loan")
        else:
            print("Not eligible for loan")     
else: 
    print("Not eligible for loan")                
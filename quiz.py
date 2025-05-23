print("Quiz python operators and conditional statements")
print()

score = 0

answer1 = int(input("What is 5 + 3? "))
if answer1 == 8:
    score = score + 1 
    print("correct answer")
else:
    print("Incorrect answer")
print()

answer2 = int(input("What is 9 - 4? "))
if answer2 == 5:
    score = score + 1 
    print("correct answer")
else:
    print("Incorrect answer")
print()

answer3 = int(input("What is 7 × 2? "))
if answer3 == 14:
    score = score + 1 
    print("correct answer")
else:
    print("Incorrect answer")
print()

answer4 = int(input("What is 16 ÷ 4? "))
if answer4 == 4:
    score = score + 1 
    print("correct answer")
else:
    print("Incorrect answer")
print()

answer5 = int(input("What is 10 % 3? "))
if answer5 == 1:
    score = score + 1 
    print("correct answer")
else:
    print("Incorrect answer")
print()

answer6 = int(input("What is 2³ (2 to the power of 3)? "))
if answer6 == 8:
    score = score + 1 
    print("correct answer")
else:
    print("Incorrect answer")
print()

answer7 = int(input("What is (3 + 4) × 2? "))
if answer7 == 14:
    score = score + 1 
    print("correct answer")
else:
    print("Incorrect answer")
print()

answer8 = int(input("What is 100 - 25 "))
if answer8 == 75:
    score = score + 1 
    print("correct answer")
else:
    print("Incorrect answer") 
print()

answer9 = int(input("What is 81 ÷ 9 "))
if answer9 == 9:
    score = score + 1 
    print("correct answer")
else:
    print("Incorrect answer")
print()

answer10 = int(input("What is 11 + 22? "))
if answer10 == 33:
    score = score + 1 
    print("correct answer")
else:
    print("Incorrect answer")
print()

print(f"The total score is: {score}/10")

if score == 10: 
    print("excellent")
elif score <10 and score >=7:
    print("very good")
elif score <7 and score >= 5:
    print("Work harder next time")
else:
    print("Study more and work  harder you can do better next time") 
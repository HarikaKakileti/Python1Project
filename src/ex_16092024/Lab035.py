# Grade calculator
# Write a program that calculates and displays the letter grade for a given numeric score
#  A :90-100    B:80-89 C: 70-79 D:60-69 F :0-59

score = int(input("Enter the score"))
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
else :
    print("F")


# Simplified program

score = int(input("Enter the score"))
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else :
    print("F")


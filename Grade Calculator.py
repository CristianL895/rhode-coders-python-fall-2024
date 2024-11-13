# The student enters their grade from 0-100
score1 = int(input("Enter your first grade (0-100): "))
score2 = int(input("Enter your second grade (0-100): "))
score3 = int(input("Enter your third grade (0-100): "))

total_score = [score1, score2, score3]

total = 0

# You use a "for" loop in order to add up the score the student put in at the top.
for grade in total_score:
    total += grade

# We then make a new varieble called "average", and the average is the numbers in the list, added together, then divided by 3.
average = total /3

grade = ()

# This is the calculation where depending on what was your "average", it will give you your grade.
if 95 <= average == 100:
        grade = "A+"
elif 90 <= average < 95:
        grade = "A"
elif 85 <= average < 90:
        grade = "A-"
elif 80 <= average < 85:
        grade = "B+"
elif 75 <= average < 80:
        grade = "B"
elif 70 <= average < 75:
        grade = "B-"
elif 65 <= average < 70:
        grade = "C"
elif 60 <= average < 65:
        grade = "D"
elif average < 60:
        grade = "F"

# These will print out the list of your scores, the "average" AKA your final score, and your final grade
print("Your score was:", total_score)
print("Your Final score was:", average)
print("Your final grade is", grade)
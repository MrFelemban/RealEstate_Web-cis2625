# obtaining the user's raw points or percentage
raw_points = float(input("Add the percentage or raw points: "))

# use conditional flow to determine the letter grade
if raw_points >= 90:
    letter_grade = "A"
elif raw_points >= 80:
    letter_grade = "B"
elif raw_points >= 70:
    letter_grade = "C"
elif raw_points >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

#display the user's letter grade.
print(f"The letter grade is {letter_grade}")
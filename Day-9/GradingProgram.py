print("Welcome to the Grading Program")
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grade = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    score = student_scores[key]
    if score >= 90:
        student_grade[key] = "OutStanding"
    elif score >= 80:
        student_grade[key] = "Excedes Expectations"
    elif score >= 70:
        student_grade[key] = "Acceptable"
    else:
        student_grade[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grade)

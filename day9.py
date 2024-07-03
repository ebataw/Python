student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grade
for key in student_scores:
    score=student_scores[key]
    if score>91:
        student_grades[key]="outstanding"  
    elif score>81:
        student_grades[key]="Exceeds Expectations"
    elif score>71:
        student_grades[key]="acceptable"
    elif score<70:
        student_grades[key]="fail"




# 🚨 Don't change the code below 👇
print(student_grades)
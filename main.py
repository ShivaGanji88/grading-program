student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for each_student in student_scores:
    each_score = student_scores[each_student]
    
    if (each_score >= 91):
        student_grades[each_student] = "Outstanding"
        
    elif (each_score >= 81) and (each_score <= 90):
        student_grades[each_student] = "Exceeds Expectations"
        
    elif (each_score >= 71) and (each_score <= 80):
        student_grades[each_student] = "Acceptable"
        
    else:
        student_grades[each_student] = "Fail"       

    

# 🚨 Don't change the code below 👇
print(student_grades)
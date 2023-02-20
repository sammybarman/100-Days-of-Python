'''
you have access to a dictionary in the form student:scores
change scores to grades according to the following rules:
91-100 = outstanding
81-90 = exceeds expectation
71-80 = acceptable
70 or lower = fail
'''

# Solution
def grading_system():
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }
    student_grades = {}
    for students in student_scores:
        if student_scores[students] > 90:
            student_grades[students] = "Outstanding"
        elif student_scores[students] > 80:
            student_grades[students] = "Exceeds Expectations"
        elif student_scores[students] > 70:
            student_grades[students] = "Acceptable"
        else:
            student_grades[students] = "Fail"
    
    print(student_grades)

grading_system()

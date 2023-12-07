#i)
age =0
User_age = int(input('enter your age:'))
if User_age >=18:
    print(f"You are eligible")
else:
    print(f"You are not eligible")
    
    

#ii
# 90 or above: 'A'
# 80-89: 'B'
# 70-79: 'C'
# 60-69: 'D'
# Below 60: 'F'    

def grade_students(mark):
    if mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    else:
        return 'F'

student_mark = float(input("Enter the student's mark: "))
Answer = grade_students(student_mark)
print(f"The corresponding grade is: {Answer}")


#iii
#Test the function with a mark of 85.

def grade_students(mark):
    if mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    else:
        return 'F'


student_mark = 85
Answer = grade_students(student_mark)
print(f"The corresponding grade for a mark of {student_mark} is: {Answer}")


#iv)
#modify the "grade_students" function to handle the case where the input mark is not a valid number.

def grade_students(mark):
    try:
        mark = float(mark)
    except ValueError:
        return 'Invalid Input'

    if mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    else:
        return 'F'

valid_mark =  int(input("Enter your valid mark: "))
output_valid = grade_students(valid_mark)
print(f"The corresponding grade for a mark of {valid_mark} is: {output_valid}")

# Test the function with an invalid input
invalid_mark = 'xyz'
output_invalid = grade_students(invalid_mark)
print(f"The result for an invalid input '{invalid_mark}' is: {output_invalid}")


#(v)
#Enhance the "grade_students" function to also provide a message along with the grade


def grade_students(mark):
    try:
        mark = float(mark)
    except ValueError:
        return 'Invalid Input'

    if mark >= 90:
        return 'A', 'Excellent'
    elif 80 <= mark < 90:
        return 'B', 'Excellent'
    elif 70 <= mark < 80:
        return 'C', 'Good'
    elif 60 <= mark < 70:
        return 'D', 'Satisfactory'
    else:
        return 'F', 'Needs Improvement'

# Test the function with a valid mark
valid_mark = int(input("Enter your valid mark:"))
grade, message = grade_students(valid_mark)
print(f"The corresponding grade for a mark of {valid_mark} is: {grade} '' {message}")

# finding  the function with an invalid input
invalid_mark = 'abc'
answer_invalid = grade_students(invalid_mark)
print(f"The result for an invalid input '{invalid_mark}' is: {answer_invalid}")


#iv)

#test the function with a mark of 78.

def grade_students(mark):
    try:
        mark = float(mark)
    except ValueError:
        return 'Invalid Input'

    if mark >= 90:
        return 'A', 'Excellent'
    elif 80 <= mark < 90:
        return 'B', 'Excellent'
    elif 70 <= mark < 80:
        return 'C', 'Good'
    elif 60 <= mark < 70:
        return 'D', 'Satisfactory'
    else:
        return 'F', 'Needs Improvement'
valid_mark = 78
grade, message = grade_students(valid_mark)
print(f"The corresponding grade for a mark of {valid_mark} is: {grade} - {message}")

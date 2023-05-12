# finding correct grading for a student
grade_a = 99
grade_b = 98
grade_c = 87
grade_d = 85
grade_e = 80

student_name = input('Please enter the student name: ')
student_score = int(input('Please enter the student"s score: '))

# print(f'this is the data type of student_score: {type(student_score)}')

match student_score:
    case 99:
        print('Student is in grade "A"')
    case 98:
        print('Student is in grade "B"')
    case 87:
        print('Student is in grade "C"')
    case 85:
        print('Student is in grade "D"')
    case 80:
        print('Student is in grade "E"')
    case _:
        print('The student has failed')







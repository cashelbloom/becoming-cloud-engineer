import json

with open('student_scores.json') as student_scores:
    #student_scores = student_scores.read()
    #print(type(student_scores))
    student_scores = json.load(student_scores)
    print(type(student_scores))
    student_id = student_scores['students']['studentScores']
    #print(student_id)
    #first_student = student_id[0]
    #print(first_student)
    for studentId in student_id:
        #print(studentId)
        scores = studentId["scores"]
        #print(scores)
        #print(scores["math"])
        max_score = max(scores, key=scores.get)
        #print(max_score)
        print(f'The highest score for student {studentId["studentId"]} is {max(scores.values())} for the subject {max(scores, key=scores.get)}')



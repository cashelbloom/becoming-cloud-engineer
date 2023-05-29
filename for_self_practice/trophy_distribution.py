import json

with open('score_sheet.json') as scores_file:
    student_scores = json.load(scores_file)
    print(student_scores)
    print(f'the data type of student_scores: {type(student_scores)}')

students_total_score = {}
stu_cats = ['AE', 'SE', 'CP', 'SI', 'LD']
stu_total = []
for student in student_scores['scoreSheet']:
    student_id = student['studentId']
    stu_total_score = 0
    stu_scores = list(student['categoryScores'].values())
    for score in stu_scores:
        stu_total_score += score
    students_total_score.update({student_id: stu_total_score})
print(students_total_score)
print(max(list(students_total_score.values())))


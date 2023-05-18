'''
1. Create a function that will take a dictionary containing student id as the key and
its value will be subject-wise scores. The subjects are:
English, Math, Science, Social, Compscience.
Your program has to list the top scorers (using their student id) in each subject.
'''
import json
#
with open('student_scores.json') as stu_scores:
    dict_stu_scores = json.load(stu_scores)
    # print(dict_stu_scores)
#
stu_scores_list = dict_stu_scores['students']['studentScores']
#
stu_id_list = []
stu_score_list = []
#
english_scores = []
math_scores = []
science_scores = []
social_scores = []
compscience_scores = []
#
for stu_score in stu_scores_list:
    stu_id = stu_score['studentId']
    stu_id_list.append(stu_id)
    stu_scores = stu_score['scores']
    stu_score_list.append(stu_scores)
    # print(f'Student id: {stu_id}')
    print(f'For this student id {stu_id}  student scores are: {stu_scores}')
    # for each_stu_score in stu_scores:
    english_scores.append(stu_scores['english'])
    math_scores.append(stu_scores['math'])
    science_scores.append(stu_scores['science'])
    social_scores.append(stu_scores['social'])
    compscience_scores.append(stu_scores['compscience'])

max_english = max(english_scores)
max_math = max(math_scores)
max_science = max(science_scores)
max_social = max(social_scores)
max_compscience = max(compscience_scores)
#
max_english_student = stu_id_list[english_scores.index(max_english)]
max_math_student = stu_id_list[math_scores.index(max_math)]
max_science_student = stu_id_list[science_scores.index(max_science)]
max_social_student = stu_id_list[social_scores.index(max_social)]
max_compscience_student = stu_id_list[compscience_scores.index(max_compscience)]
#
print(f'This is the highest score in English: {max_english} and the student is {max_english_student}')
print(f'This is the highest score in Math: {max_math} and the student is {max_math_student}')
print(f'This is the highest score in Science: {max_science} and the student is {max_science_student}')
print(f'This is the highest score in Social: {max_social} and the student is {max_social_student}')
print(f'This is the highest score in Comp Science: {max_compscience} and the student is {max_compscience_student}')

    # print(stu_id_list)
    # print(stu_score_list)
    # print(english_scores)
    # print(math_scores)
    # print(science_scores)
    # print(social_scores)
    # print(compscience_scores)
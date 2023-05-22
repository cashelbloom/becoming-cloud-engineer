import json
#
mark_list = [100, 300,205,1000,789,345,134,289]
# print(f'This is the highest value in the list: {max(mark_list)}')
# print(f'This is the lowest value in the list: {min(mark_list)}')

# json_str = json.dumps(mark_list)
# print(json_str)
# print(f'the data type of json_str is: {type(json_str)}')

# with open('my_scratch_file', 'w') as msf:
#     json.dump("myString Hi", msf)

my_json_string = {'myList': mark_list}
print(f'Calling json.dumps on my_json_string: {json.dumps(my_json_string)}')
print(type(my_json_string))
#
my_dumps_string = json.dumps(my_json_string)
print({my_dumps_string})
my_py_dict = json.loads(my_dumps_string)
print(type(my_py_dict))
print(my_py_dict)























    # print(f'This is the score {student_scores["studentId"]["scores"]["english"]}')
    # print(f'This is the score {student_scores[1000]["scores"]["english"]}')
    # print(f'This is the score {student_scores["english"]}')
    # print(f'This is the score {student_scores["students"][10]["scores"]["english"]}')
    # print(f'This is the score (student_scores["english"])')


    # json.dump(py_dict)

# with open('scratch_2.json', 'w') as new_json_file:
#     # new_json_file.write(py_dict)
#     json.dump

# with open('../solution_for_self_practices/051723_solutions/student_scores.json') as stu_scores_2:
#     print(f'This is in raw JSON string format: {py_dict}')
#     dict_stu_scores = json.load(stu_scores_2)
#     print(f'This is post conversion to Python dict: {dict_stu_scores}')

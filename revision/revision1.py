'''
what is print = print()
what are the different ways we can send values to the built in function?
f-string
print(f'')
'''
# my_name = 'xyz'
# print(f' I would like to invoke some logic inside the f-string {True if 5 > 0 else False}')
#
# my_list = ['Hello World', {'key': 'value'}, [1, 2, 3], True, False, 1.23]
# print(f'{my_list[3]}')
# print(f'This is the last but 2nd element from the list: {my_list[-2]}')
# my_dict = {'name': 'xyz', "age": 25}
# print(f'{my_dict["age"]}')

students_dict = {'1': '123adf', '2': '45689f'}
students_list = ['a', 'b']

# new_students_dict = {key for key in students_dict.values(): value for value in students_list}
# print(new_students_dict)
new_stu_dict = {'key for key in liststudents_dict.values()': name for name in students_list}
print(new_stu_dict)

# for item in students_dict.values():
#     print(item)
# new_student_dict = {}
# for v in students_list:
#     new_student_dict[item] = v
# #
# print(new_student_dict)

# def any_name(students_dict, students_list):
#     new_students_list = {}
#     index = 0
#     for value in students_dict.values():
#         new_students_list[value] = students_list[index]
#         index += 1
#     print(new_students_list)
#     #
# any_name(students_dict,students_list)

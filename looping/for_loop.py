def assigned_seats(number,name):
    # for get_numbers in number:
    #     final_number = number.index(get_numbers)
    #     print(f'{final_number + 1}.This seat number {get_numbers} is assigned to {name[final_number]} in the Hall A')
    # # my_shortened_students_list = name[0:2]
    my_single_stu = name[5]
    print(f'this is the data type of my_single: {type(my_single_stu)}')
    my_shortened_students_list = name[4:5]
    print(f'this is the data type of my_single: {type(my_shortened_students_list)}')
    print(f'I have the first two students from the list: {my_single_stu}')
    print(f'I have the first two students from the list: {my_shortened_students_list}')


seats = ['10', '11', '12', '13', '14', '15']
students = ['Radha', 'Latha', 'Mala', 'Kala', 'Devi', 'Geetha']
assigned_seats(seats,students)
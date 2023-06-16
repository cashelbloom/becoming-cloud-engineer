# def find_sum(a, b):
#     print(f'the value of a is: {a}')
#     print(f'the value of b is: {b}')
#     return a + b
#
#
# print(f'The sum of the two numbers passed is: {find_sum(100, 200)}')

#
# def find_sum_kwargs(*, my_a_value=5000, my_b_value=500):
#     print(f'the value of my_a_value is: {my_a_value}')
#     print(f'the value of my_b_value is: {my_b_value}')
#     return my_a_value + my_b_value
#
# print(f'The sum of the two numbers passed is: {find_sum_kwargs(my_b_value=100, my_a_value=300)}')
# print(f'The sum of the two numbers passed is: {find_sum_kwargs(100)}')

def find_sum(* number_of_numbers):
    print(f'The sum of the two numbers is {find_sum(100, 1500)}')
    print(f'The sum of the two numbers is {find_sum(10000, 15000)}')




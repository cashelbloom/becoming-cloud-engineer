import json

def add_two_numbers():
    a = 5
    b = 10
    c = a + b
    return '{"firstNumber": "a", "secondNumber": "b", "theSum": "c"}'
    # return c, a, b



return_value_from_the_function = add_two_numbers()
print(return_value_from_the_function)
print(f'The data type is {type(return_value_from_the_function)}')
converted_ret_value = json.loads(return_value_from_the_function)
print(f'Now the data type is: {type(converted_ret_value)}')



# print(f'I am getting double value of what is returned: {return_value_from_the_function * 2}')
# print(f'The first number is {a}, the second number is {b}, and the sum of the 2 '
#       f'numbers is {return_value_from_the_function}')

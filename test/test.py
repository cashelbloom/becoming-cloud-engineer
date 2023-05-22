
my_custom_variable = 'Ramya'
print(f'The objective of the built-in function "type" is to get the data type of the parameter vaule passed to the "type" function: {type(my_custom_variable)}')
print(f'The objective of the built-in function "len" is to get the length of the parameter value passed to the "len" function: {len(my_custom_variable)}')

str_true = 'True'
print(f'The data type of str_true is {type(bool((str_true)))}')

flag = True
print(f'The data type of the flag variable is {type(flag)}')

def calculate(i, j):
    r = i % j
    print(f'The remainder of the division of the first number by the second number is {r}')


calculate(3, 2)

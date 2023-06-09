'''
We can define functions or methods that can accept variable number of args
As we know there are 2 broad classification of parameters:
    1. positional params / args
    2. keyword params / args
        keyword params can further  be sub-classified as:
            1. keyword params that don't have default values
            2. keyword params that are declared with default values
'''
# So, we can have variable number of positional params
# and variable number of keyword params
'''
the variable number of positional params is declared with an asterisk in front of a single variable name
for example, we have a function to sum the numbers passed to it. A user can pass any number of numbers to this function.
The function should take variable number of args passed to it and sum all of them.
    See the example implementation below: 
'''
def sum_variable_numbers_passed(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(f'The sum of 5 numbers is: {sum_variable_numbers_passed(5, 25, 100, 39, 1008)}')
print(f'The sum of 7 numbers is: {sum_variable_numbers_passed(5, 25, 100, 39, 1008, 20000, 50000, 2, 10, 100)}')

'''
The variable number of keyword params is declared with 2 asterisks. See below:
IMPORTANT: When keyword args are processed, each keyword arg name and the value are taken as a tuple.
Hence, we have to properly retrieve either the key or the value based on the business logic.
'''
def sum_variable_keyword_args_passed(**kwargs):
    sum = 0
    for item in kwargs.items():
        print(f'the data type of item is: {type(item)}')
        print(f'the data type of first element in the tuple is: {item[0]}')
        sum += int(item[1])
    return sum


print(f'The sum of 3 keyword args passed to sum_variable_keyword_args_passed() is : '
      f'{sum_variable_keyword_args_passed(first_num=10, second_num=25, third_num=50)}')


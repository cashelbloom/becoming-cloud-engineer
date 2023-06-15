def add_numbers(*numbers, **kwargs,):
    sum = 0
    for number in numbers:
        sum += number
    another_sum = 0
    for arg in kwargs:
        print(f'the name of the kwarg is: {arg}')
        print(f'the data type of arg is: {type(arg)}')
        print(f'the value from arg is: {kwargs[arg]}')
        another_sum += kwargs[arg]
    print(f'the data type of kwargs:  {type(kwargs)}')
    return sum, another_sum


print(f'this is the return value from the function: {add_numbers(900, 800, 10000, 20000, axyz=10, bmno=25)}')
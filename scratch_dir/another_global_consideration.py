my_global_var = 100

def test_global_variable_understanding():
    global my_global_var
    print(f'First call from inside the function:This is the value of the global variable my_global_var: {my_global_var}')
    my_global_var = 125
    print(f'Second call from inside the function: This is the value of the global variable my_global_var: {my_global_var}')


print(f'First call from outside the function: This is the value of the global variable my_global_var: {my_global_var}')
test_global_variable_understanding()
print(f'Second call from outside the function: This is the value of the global variable my_global_var: {my_global_var}')
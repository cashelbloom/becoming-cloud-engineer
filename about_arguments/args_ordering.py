'''
These are the order of parameters declaration in a function / method definition:
1. Default arg(s) should be declared after non-default parameters
    Example below:
'''
def specify_default_parms_last(a, b, c=10):
    return a + b + c

print(f'return value from specify_default_parms_last(): {specify_default_parms_last(5, 10, 100)}')
# in the above function definition parameter c is the parameter with a default value.
# Hence, that appears after the non-default parameters.
# The following definition will fail:
# def specify_default_params_notlast(a, b, c=10, d):
#     return a + b + c + d

'''
2. Keyword parameters should follow positional parameters:
    Example below:
'''
def specify_keyword_params_after_pos_params(a, b, third_num=25, fourth_num=50):
    print(f'The value of fourth_num is: {fourth_num}')
    return a + b + third_num + fourth_num

print(f'return value from specify_keyword_params_after_pos_params: {specify_keyword_params_after_pos_params(200, 500)}')
print(f'return value from specify_keyword_params_after_pos_params: '
      f'{specify_keyword_params_after_pos_params(200, 500, fourth_num=10000, third_num=5000)}')
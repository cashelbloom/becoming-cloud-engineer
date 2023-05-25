import json

# with open('my_json_file.txt', 'w') as my_json_file:
#     my_json = '{ "name":"John", "age": 30, "city": "New York"}'
#     my_json_file.write(my_json)

with open('my_json_file.txt') as my_json_read_file:
# with open('another_text_file.txt') as my_json_read_file:
    # my_json = my_json_read_file.read()
    # print(my_json)
    # my_dict = json.loads(my_json)
    # print(type(my_dict))
    print(f'This is the data type of the file variable: {type(my_json_read_file)}')
    my_json = json.load(my_json_read_file)
    print(f'This is the outcome from loading a file: {my_json}')

# my_py_dict = {'myKey': "myValue"}
# print(f'I am printing value from my_py_dict: {my_py_dict["myKey"]}')
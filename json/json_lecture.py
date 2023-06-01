import json
'''
In Python, the use of JSON structured data is very prevalent.
To deal with JSON data, there is a json package available - json

Now, you can read JSON data from a file into your processing program
    For the above, do this:
        get the file opened
        then, call the json.load(<<the file reference>> and assign the output to a variable.
        Now the variable that received the JSON data from the file is of 'dict' data type.
        Here is the code:'''
#############################################################################
my_test_file = open('my_json_file.txt')
data_from_file = my_test_file.read()
print(f'the data from file before any formatting: {data_from_file}')
print(f'the data type of data_from_file : {type(data_from_file)}')
my_test_file.close()
my_test_file = open('my_json_file.txt')
my_json_from_file = json.load(my_test_file)
print(my_json_from_file)
print(f'the data type of my_json_from_file is:  {type(my_json_from_file)}')
my_test_file.close()
###############################################################################
'''
Similarly, you can write JSON data from your processing program onto a file
In this case, you have to open the destination file
Then call the json.dump(<<the variable holding JSON data>>, <<the file reference variable>>)
'''
my_destination_file = open('destination_file.json', 'w')
json.dump(my_json_from_file, my_destination_file)
my_destination_file.close()
'''
On another note, you can have a JSON structured data in your processing program; but you have to get that JSON data
as a Python dictionary in your program to process the data.
In this case, you have to call json.loads(<<variable holding JSON data>> and assign to a variable.
The variable receiving the JSON data is of type 'dict'.
'''
my_json_data = {"name": "John", "age": "30", "city": "New York"}
print(f'The data type of my_json_data is: {type(my_json_data)}')
# my_dict_containing_json = json.loads(my_json_data)
my_json_data_str = '{"name": "John", "age": "30", "city": "New York"}'
print(f'The data type of my_json_data_str is: {type(my_json_data_str)}')
my_dict_containing_json = json.loads(my_json_data_str)
print(f'The data type of my_dict_containing_json is: {type(my_dict_containing_json)}')
'''
Similarly, you have JSON data in your processing program. But, you want to have that data as a string for whatever
reason.
'''

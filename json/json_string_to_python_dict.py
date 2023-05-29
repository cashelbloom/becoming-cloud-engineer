import json
#
# # my_json = "{ 'name':'John', 'age': '30', 'city': 'New York'}"
#
# # my_json = '{ "name":"John", "age": 30, "city": "New York"}'
# my_normal_string = "my name is GP"
# my_python_dict = json.loads(my_normal_string)
# # my_python_dict = json.loads(my_json)
# print(f'This is my Python dict from JSON string: {my_python_dict}')

'''
json.loads()
json.load()
json.dumps()
json.dump()
'''
my_test_file = open('my_json_file.txt')
my_json_from_file = json.load(my_test_file)
print(my_json_from_file)
my_test_file.close()

my_destination_file = open('destination_file.json', 'w')
json.dump(my_json_from_file, my_destination_file)
my_destination_file.close()

my_json_from_string = {"myFirstKey": "first value"}
my_destination_file_2 = open('destination_file_2.json', 'w')
my_json_string = json.dumps(my_json_from_string)
print(f'json data in string format: {my_json_string}')
print(f'the data type of my_json_string is: {type(my_json_string)}')
my_destination_file_2.close()

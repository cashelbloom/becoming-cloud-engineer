import json

# my_json = "{ 'name':'John', 'age': '30', 'city': 'New York'}"

# my_json = '{ "name":"John", "age": 30, "city": "New York"}'
my_normal_string = "my name is GP"
my_python_dict = json.loads(my_normal_string)
# my_python_dict = json.loads(my_json)
print(f'This is my Python dict from JSON string: {my_python_dict}')

'''
json.loads()
json.load()
json.dumps()
json.dump()
'''
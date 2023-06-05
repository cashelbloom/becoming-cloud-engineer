#Looping through Lists and Tuples:
# import json
import random

# 1. Create a python file as
# 2. Read the contestants.json file, the one in this directory into a variable.
# 3. Create a list of tuples that has 10 tuples and in each tuple, we have
    # citizens = [(1, "citizen_1"), (2, "citizen_2"), (3, "citizen_3")]
# 4. On election day, each of these people will be voting/casting the vote:
# 5. Contestants

# Casing:
#python variable - snake casing
# function names in python is snake casing

#Obtaining individual indices from inside of a list of tuples:
voters = [(1, "citizen_1", "Bangalore"), (2, "citizen_2", "majestic"), (3, "citizen_3", "J P nagar"), (4, "citizen_4", "BTM"),
          (5, "citizen_5", "VV Puram"), (6, "citizen_6", "Mekhri Circle"), (7, "citizen_7", "Ulsoor"), (8, "citizen_8", "Jayanagar"),
          (9, "citizen_9", "Chickpet"), (10, "citizen_10", "SheshadriPuram")]

for x,y,z in voters:
    # index += 1
    print(f'The citizen"s Ids are: {x}')
    print(f'The citizen"s name are: {y}')
    print(f'The citizen"s area are: {z}')
    print(f'The full details of voters are: {x}-{y}-{z}')

#When the list contains multiple data types:
voters = [(1, "citizen_1", "Bangalore"),"string"]

"""
Class - has attributes and methods. It is a blueprint of an object
Attributes are characteristics
Methods are capabilities

Function def - parameters
while calling the function, we pass arguments

Blue print/class for a lawn:
 - Length & Width attributes
 - Reduces dust
"""




my_list_items = [[1, "citizen_1"],[2, "citizen_2"],[3, "citizen_3"], "str_1"]

for count in range(0,len(my_list_items)):
    print(f'The iteration is {count}')
    # print(f'The items are : {my_list_items[count][0]}--{my_list_items[count][1]}')
    print(f'The items are : {my_list_items[count][0]}--{my_list_items[count][1]}')

stringtest = "Cloud"

print(f'The first alphabet is: {stringtest[0]}{stringtest[1]}{stringtest[2]}{stringtest[3]}{stringtest[4]}')

# for item, v in my_list_items:
#     print(f'The iteration is: {my_list_items.}')
#     print(f'V is {v}')
#     print(f'Item is {item}')
#     print(f'The list item is: {item}-{v}')
#     print(f'Index is : {iteration}')
#     iteration += 1



print(f'My list is: {my_list_items}')

# myfile = open("contestants.json", "r")
# with open("contestants.json", "r") as myFileReader:
#     my_file_handler = json.load(myFileReader)
#     # my_file_handler = myFileReader.read()
#     print(f'This is the data type of my_file_handler: {type(my_file_handler)}')
#     print(f'My file is: {my_file_handler["contestants"]}')


# index = 0













'''
Tuples are used to store multiple items in a single variable - so it is a collection data type.

Tuple is one of 4 built-in data types in Python used to store collection of data, the other 3 are
List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable. A tuple can have duplicate values.

Tuples are written with round brackets.

You can have just one item in a tuple; but, it is a must to put a comma (,) after the item.
Only then that object is considered of type tuple. Otherwise, it will be considered as a string object.
See the example below:'''

this_is_tuple = ('energy',)
this_is_string = ('energy')
print(f'the data type of this_is_tuple is: {type(this_is_tuple)}')
print(f'the data type of this_is_string is: {type(this_is_string)}')
'''
Characteristics of a tuple:
Ordered, Unchangeable , Duplicates Allowed
Like a list that can contain different types of data elements, a tuple can also have different types of data in it.
We can call built-in functions on a tuple object: type(), len()
Since tuple is a class, we can call constructor to instantiate a tuple.
See the exapmple below:
'''
my_constructed_instantiated_tuple = tuple(('energy', 'power'))
print(f'The data type of my_constructed_instantiated_tuple is: {type(my_constructed_instantiated_tuple)}')
'''
Anyone to reason why the values are placed in a set of pair of open and close parentheses?
Since a tuple is a type of collection, the methods available for other collection types such as list and
dictionary are also available in the tuple class. 
Example below:
'''
my_tuple = ('apple', 'banana', 'carrot', 'dates', 'eggplant')
for item in my_tuple:
    print(item)
my_tuple_as_list = list(my_tuple)
for i in range(0, 5):
    print(my_tuple_as_list[i])
'''
One very interesting and important info about tuple in Python is that 
it is the underlying data type in the collection when a dictionary is iterated.
What it's is explained in the following example:
'''
my_restuarant_menu = {'naan': 0.50, 'mutterPanneer': 13.50, 'coffee': 1.50,
                      'tandooriRoti': 0.75, 'kadaaiMilk': 2.00}
print(f'The data type of my_restuarant_menu is: {type(my_restuarant_menu)}')
for k,v in my_restuarant_menu.items():
    print(f'The key is: {k} and its value is: {v}')
'''
As we see in the above example, a dict type has a method 'items()'. 
Now, if we see what the return value(s) of this method, we will be sort of surprised;
it is a list of tuples. Let us see in the below example:
'''
print(f'the data type of the returned data from my_restuarant_menu.items() is: {type(my_restuarant_menu.items())}')
for dict_item in my_restuarant_menu.items():
    print(f'The data type of each item in dict_items is: {type(dict_item)}')

'''
As the returned data type is tuple, each tuple has the key and its value).
Hence, we are able to call the tuple and and take the first value in the
tuple as the key and the next and final value as value.
See in the following example:
'''
list_of_menu = {"Naan": 0.50, "Coffee": 15.0, "Cake": 1.5, "Panner Tikka Masala": 1.0}
my_order = {"Naan": 3, "Coffee": 1, "Cake": 2, "Panner Tikka Masala": 1}


def bill_before_tax_and_tip(money, menu):
    price = 0.0
    # for k, v in my_order.items():
    #     price += v * list_of_menu[k]
    # return price
    print(f'contents of my_order.items(): {my_order.items()}')
    for my_object in my_order.items():
        print(f'The data type of each object returned by my_order.items() is: {type(my_object)}')
    for k, v in my_order.items():
        price += v * list_of_menu[k]
    return price

money_available = 80.0
menu_selected = {"Naan": 3, "Coffee": 1, "Cake": 2, "Panner Tikka Masala": 1}
my_total_bill = bill_before_tax_and_tip(money_available, menu_selected)
print(f"my total bill is: {my_total_bill}")
'''
Accessing elements in a tuple:
The elements of a tuple can be accessed using index (like accessing elements of a list)
'''
my_fruits_tuple = ('apple', 'orange', 'banana', 'guava', 'melon', 'grapes', 'pears')
print(f'Let me see what the last fruit in my_fruits_tuple: {my_fruits_tuple[-1]}')
print(f'let me count the number of fruits in my_fruits_tuple: {len(my_fruits_tuple)}')
print(f'let me take the first and the last fruit from my_fruits_tuple: {my_fruits_tuple[0]}, {my_fruits_tuple[-1]}')
print(f'we can use slicing to get a subset of elements from a tuple - first 4 fruits are taken: {my_fruits_tuple[:4]}')
print(f'now taking the 4th and 5th fruits: {my_fruits_tuple[3:5]}')
'''
We can check if a specific element value exists in a tuple:
'''
print(f'checking if pineapple is included in my_fruits_tuple: {True if "pineapple" in my_fruits_tuple else False}')
print(f'checking if banana is included in my_fruits_tuple: {True if "banana" in my_fruits_tuple else False}')
'''
Adding and removing items/elements to or from a tuple not allowed.
However, there are 2 indirect methods available for adding or removing an item or items from a tuple.
first method is to type cast a tuple to a list and carry out the append or remove method on the list
next assign the list to the original tuple to refresh the items of the original tuple with elements from the list.
Here you go:
'''
# using the tuple constructor method:
second_fruit_tuple = tuple(('pineapple', 'apricot'))
print({second_fruit_tuple})
print(f'the data type of second_fruit_tuple : {type(second_fruit_tuple)}')
# knowledge check: why should we have 2 sets of parantheses for the constructor?
# adding another fruit to the second_fruit_tuple in an indirect way:
second_fruit_list = list(second_fruit_tuple)
second_fruit_list.append('apple')
second_fruit_tuple = tuple(second_fruit_list)
# second_fruit_tuple = tuple((list(second_fruit_tuple)).append('apple'))
print(f'adding a new item to tuple: {second_fruit_tuple}')
# print(f'checking a value in a list: {second_fruit_list.index("cashew")}')
print(f'checking a value - cashew in a tuple: {True if "cashew" in second_fruit_tuple else False}')
print(f'checking a value - apple in a tuple: {True if "apple" in second_fruit_tuple else False}')


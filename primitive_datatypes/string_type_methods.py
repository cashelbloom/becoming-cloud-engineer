'''
This file has implementation for important methods of String (str) type.
'''
# We are declaring a string variable and assign an initial value to it.
# Remember single = operator stands for assignment and not for testing 'EQUALITY between left and right.
my_training = 'Becoming Cloud Engineer'
# Just printing the value of the my_training variable.
print(f'this is the original value assigned to my_training variable: {my_training}\n')
# I have added to the f string \n. This \n instructs to introduce a new blank line.

# Let us convert to UPPER CASE all characters of the value assigned to my_training variable.
print(f'making all the characters in upper case: {my_training.upper()}\n')
# Now let us use a method from str class to count the number of characters in the string.
num_characters = len(my_training)
print(f'the number of characters in the value assigned to my_training variable: {num_characters}\n')
# Note: the "len" method is ONLY available for objects of str type.
# You can try for other data types and see if the program runs with or without error.

# print(lent(1000))
# stripping leading blank spaces on the left side of a string.
# New value being assigned to my_training variable
my_training = '   I have 3 blank characters on the left side'
print(f'the value printed as it is:{my_training}\n')
print(f'the value printed after the blank spaces at the beginning on the left is removed:{my_training.lstrip()}\n')

my_training = 'I have 3 blank characters on the right side   '
print(f'the value printed as it is:{my_training}\n')
print(f'the value printed after the blank spaces at the end are removed:{my_training.rstrip()}\n')

# Now let us consider 'split' method available for str type.
my_training_split_list = my_training.split(' ')
# We are going to use ' ' as the character for splitting the given string.
print(f'the split method returns a list of values after successfully splitting the given string object: {my_training_split_list}')

# Adding a dummy comment for ramya_test.

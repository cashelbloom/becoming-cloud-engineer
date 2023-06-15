'''
In this exercise, you are going to use list comprehension we went over in one of our earlier sessions:
You have a list:
    my_integers_list = [5, 8, 7, 10, 26, 21, 19, 34, 45, 89, 19, 22, 38]
Your program should return a list that contains only odd numbers.
Remember, your program should apply list comprehension for the solution.
'''

my_integers_list = [5, 8, 7, 10, 26, 21, 19, 34, 45, 89, 19, 22, 38]

my_odd_list = [n for n in my_integers_list if n%2 != 0]
print(my_odd_list)
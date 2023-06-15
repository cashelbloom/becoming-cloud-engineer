my_integers_list = [5, 8, 7, 10, 26, 21, 19, 34, 45, 89, 19, 22, 38]

print(f'The items in the original list are: {my_integers_list}')
print(f'The even list is: {[item for item in my_integers_list if item%2 == 0]}')
print(f'The odd list is: {[item for item in my_integers_list if item%2 != 0]}')


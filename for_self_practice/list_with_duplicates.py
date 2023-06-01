# from collections import Counter
# from itertools import count
#
#
# input_list = ['A', 'B', 'C', 'A', 'D', 'D', 'A', 'E']
# c = Counter(input_list)
# print(f'The contents of c: {c}')

# iters = {k: count(1) for k, v in c.items() if v > 1}
# output_list = [x+str(next(iters[x])) if x in iters else x for x in input_list]
# # ['A1', 'B', 'C', 'A2', 'D1', 'D2', 'A3', 'E']

from operator import length_hint
lst = [1, 2, 3]
iter_obj = iter(lst)
print(f'The iterator object length before iteration: {iter_obj}')
print(length_hint(iter_obj))
for i in iter_obj:
    pass
print('The iterator object length after iteration:')
print(length_hint(iter_obj))














# list_of_menu = {"Naan": 0.50, "Coffee": 15.0, "Cake": 1.5, "Panner Tikka Masala": 1.0}
# my_order = {"Naan": 3, "Coffee": 1, "Cake": 2, "Panner Tikka Masala": 1}


# def bill_before_tax_and_tip(money, menu):
#     # print(f'{type(my_order.keys())}')
#     list_of_menu_list = list(list_of_menu.values())
#     print(f'the values of list_of_menu:{list_of_menu_list}')
#     my_order_list = list(my_order.values())
#     print(f'the values of my_order is :{my_order_list}')
#     price = 0.0
#     index = 0
#     for item in my_order_list:
#         print(f'current item is:{item}')
#         print(my_order_list.index(item))
#         price = price + (item * list_of_menu_list[index])
#         index = index + 1
#     # print(f'price is:{price}')
#     return price
#
#
# money_available = 80.0
# menu_selected = {"Naan": 3, "Coffee": 1, "Cake": 2, "Panner Tikka Masala": 1}
# my_total_bill = bill_before_tax_and_tip(money_available, menu_selected)
# print(f"my total bill is: {my_total_bill}")

list_of_menu = {"Naan": 0.50, "Coffee": 15.0, "Cake": 1.5, "Panner Tikka Masala": 1.0}
my_order = {"Naan": 3, "Coffee": 1, "Cake": 2, "Panner Tikka Masala": 1}


def bill_before_tax_and_tip(money, menu):
    # print(f'the data type of just the keys of the dictionary: {type(list_of_menu.keys())}')
    # print(f'the data type of just the keys of the dictionary: {type(list_of_menu.values())}')
    # for key in list_of_menu.keys():
    #     print(f'The data type of each value in dict_keys is: {type(key)}')
    # for value in list_of_menu.values():
    #     print(f'The data type of each value in dict_values is: {type(value)}')
    list_of_menu_list = list(list_of_menu.values())
    print(f'the values of list_of_menu:{list_of_menu_list}')
    my_order_list = list(my_order.values())
    print(f'the values of my_order is :{my_order_list}')
    list_of_menu_dict_values = list_of_menu.values()
    print(f'the values of list_of_menu:{list_of_menu_dict_values}')
    my_order_dict_values = my_order.values()
    print(f'the values of list_of_menu:{my_order_dict_values}')
    # price = 0.0
    # index = 0
    # for item in my_order_list:
    #     print(f'current item is:{item}')
    #     print(my_order_list.index(item))
    #     price = price + (item * list_of_menu_list[index])
    #     index = index + 1
    # print(f'price is:{price}')
    # return price
#
#
money_available = 80.0
menu_selected = {"Naan": 3, "Coffee": 1, "Cake": 2, "Panner Tikka Masala": 1}
# my_total_bill = bill_before_tax_and_tip(money_available, menu_selected)
# print(f"my total bill is: {my_total_bill}")

bill_before_tax_and_tip(money_available, menu_selected)

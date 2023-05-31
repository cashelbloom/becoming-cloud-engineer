list_of_menu = {"Naan": 0.50, "Coffee": 15.0, "Cake": 1.5, "Panner Tikka Masala": 1.0}
my_order = {"Naan": 3, "Coffee": 1, "Cake": 2, "Panner Tikka Masala": 1}


def bill_before_tax_and_tip():
    print(f'The data type of my_order.items(): {type(my_order.items())}')
    for item in my_order.items():
        print(f'The data type of {type(item)}')
    price = 0.0
    for k,v in my_order.items():
        price += v * list_of_menu[k]

    return price


print(f'This is your price for your order: {bill_before_tax_and_tip()}')













# print(f'The data type of my_order.items(): {type(my_order.items())}')
# for item in my_order.items():
#     print(f'The data type of each item inside my_order.items() is: {type(item)}')

#
#
# money_available = 80.0
# menu_selected = {"Naan": 3, "Coffee": 1, "Cake": 2, "Panner Tikka Masala": 1}
# my_total_bill = bill_before_tax_and_tip(money_available, menu_selected)
# print(f"my total bill is: {my_total_bill}")
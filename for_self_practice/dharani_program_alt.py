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
    # for item in my_order:
    #     # price += item. * list_of_menu[k]
    #     print(f'Item is: {item}')
    return price



money_available = 80.0
menu_selected = {"Naan": 3, "Coffee": 1, "Cake": 2, "Panner Tikka Masala": 1}
my_total_bill = bill_before_tax_and_tip(money_available, menu_selected)
print(f"my total bill is: {my_total_bill}")

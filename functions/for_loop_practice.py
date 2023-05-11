price_of_items = {'apples': 0.50, 'dhaMilk': 6.00, 'proteinShake': 26.00, 'bread': 3.50, 'eggsCarton': 6.50}
# new added command
def shop_all_items(money_available, shopping_list):
    my_items = shopping_list.keys()
    total_cost_of_shopping_all_items = 0
    for item in my_items:
        cost_of_this_item = price_of_items[item] * my_shopping_list[item]
        total_cost_of_shopping_all_items += cost_of_this_item
    print(f'The total money required to buy all items in the shopping list is: ${total_cost_of_shopping_all_items}')
    balance = money_available - total_cost_of_shopping_all_items
    return balance

money_with_me = 59.50
my_shopping_list = {'apples': 5, 'dhaMilk': 2, 'proteinShake': 1, 'bread': 2, 'eggsCarton': 1}
remaining_amount = shop_all_items(money_with_me, my_shopping_list)
print(f'I have some this much left after shopping all items: ${remaining_amount}')
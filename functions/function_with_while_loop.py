price_of_items = {'apples': 0.50, 'dhaMilk': 6.00, 'proteinShake': 26.00, 'bread': 3.50, 'eggsCarton': 6.50}


def shop_while_you_have_money(money_available, shopping_list):
    my_items = list(shopping_list.keys())
    print(f'my shopping list items: {my_items}')
    total_cost_of_shopping_all_items = 0
    starting_item = 1
    purchased_items = []
    is_money_available = True
    while (is_money_available):
        index = starting_item - 1
        key = my_items[index]
        print(f'here is the current key: {key}')
        cost_of_this_item = price_of_items[key] * my_shopping_list[key]
        print(f'the current item cost is: {cost_of_this_item}')
        if money_available > cost_of_this_item:
            total_cost_of_shopping_all_items += cost_of_this_item
            print(f'total cost so far: {total_cost_of_shopping_all_items}')
            money_available -= cost_of_this_item
            purchased_items.append(my_items[index])
            print(f'purchased items so far: {purchased_items}')
        else:
            is_money_available = False
        starting_item += 1
    print(f'The total money spent to buy items in the shopping list is: ${total_cost_of_shopping_all_items}')
    return money_available, purchased_items


money_with_me = 59.50
my_shopping_list = {'apples': 5, 'dhaMilk': 2, 'proteinShake': 1, 'bread': 2, 'eggsCarton': 2}
remaining_amount, purchased_items = shop_while_you_have_money(money_with_me, my_shopping_list)
print(f'This is the left out money: ${remaining_amount}')
print(f'These are the items {purchased_items} that I could buy with ${money_with_me}')




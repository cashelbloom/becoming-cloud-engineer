
menu_with_price = {
    "Vegetable Biryani": 10.00,
    "Aallu Mutter": 13.00,
    "Naan": 0.50,
    "Tanduri": 0.75,
    "coffee": 1.00,
    "Paneer Tikka Masala": 15.00,
    "Pakkoda": 1.50,
    "cake": 4.00,
    "Almond Cashew Milk": 3.00
}

total_cost = 0
list_of_items_selected = ["Vegetable Biryani","Paneer Tikka Masala","Naan","cake"]
#list_of_items_selected = []
#list_of_items_selected.append(input('List of item:'))

def items_selected(list_of_items_selected):
    price = 0
    for item in list_of_items_selected:
        print(item)
        if item in menu_with_price.keys():
            price += menu_with_price.get(item)
            #print(f'Item: {item} price:{price}')
            print(f'The total cost is {price}')

    #total_cost = total_cost + price
    #print(f'The total cost is {total_cost}')




items_selected(list_of_items_selected)
'''
4. Read the menu card of a restuarant and select any 4 items and print the total bill.
The total bill includes 12% taxes and 15% tips.
	Vegetable Biriyani = $10.00
	Aallu Mutter = $13.00
	Naan = $0.50
	Tanduri Roti = $0.75
	Coffee = $1.00
	Panneer Tikka Masaala = $15.00
	Pakkoda = $1.50
	Cake = $4.00
	Almond Cashew Milk = $3.00

	You can come up with your own data structure for the menu card with the items and their price.
'''
import decimal
menu_card = {
    'vegetableBiriyani': 10.00,
    'aalluMutter': 13.00,
    'naan': .5,
    'tanduriRoti': .75,
    'coffee': 1.00,
    'pannerTikkaMasaala': 15.00,
    'pakkoda': 1.50,
    'cake': 4.00,
    'almondCashewMilk': 3.00
}
menu_card_keys_list = list(menu_card.keys())
menu_card_values_list = list(menu_card.values())
menu_items_list = ['Vegetable Biriyani', 'Aallu Mutter', 'Naan', 'Tanduri Roti', 'Coffe', 'Panner Tikka Masaala',
                   'Pakkoda', 'Cake', 'Almond Cashew Milk']
ordered_items = list(range(0,4))
total_cost = 0.00
iteration = ''
for i in range(0,4):
    print('Please select one of the items from the menu card:')
    count = 0
    menu_price_list = list(menu_card.values())
    for item in menu_items_list:
        print(str(count + 1) + '. ' + item + ' ' + str(menu_price_list[count]))
        count +=1
    match i:
        case 0:
            iteration = 'first'
        case 1:
            iteration = 'second'

        case 2:
            iteration = 'third'
        case 3:
            iteration = 'fourth'
    try:
        order_item = int(input('Place your ' + iteration + ' item - enter the serial number for your selection: '))-1
    except:
        print('You have to enter only a number from 1 thru 9 - both included.')
    ordered_items.append(menu_items_list[order_item])
    total_cost += menu_card[(menu_card_keys_list[order_item])]
    # menu_items_list.remove()
print(ordered_items)
print(f'This is your total price of the order: {total_cost}')
taxes = decimal.Decimal(total_cost * 10/100)
taxes = taxes.quantize(decimal.Decimal('0.00'))
print(f'This is the tax on your order: {taxes}')
tips = decimal.Decimal(total_cost * 15/100)
tips = tips.quantize(decimal.Decimal('0.00'))
print(f'This is the tip amount on your order: {tips}')
final_bill_amount = decimal.Decimal(total_cost) + taxes + tips
print(f'This is your bill amount to pay: {final_bill_amount}')



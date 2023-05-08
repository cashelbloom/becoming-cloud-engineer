def let_us_shop(shopping_list):
    print(f'These are the items I am going to buy: {shopping_list}')
    print(f'I am going to pick up the first itme from the list: {shopping_list[0]}')
    print(f'I am going to pick up the third itme from the list: {shopping_list[2]}')
    print(f'I am going to pick up the fourth itme from the list: {shopping_list[3]}')
    print(f'I am going to pick up the second itme from the list: {shopping_list[1]}')
    print('I am in Walmart')
    print('I am buying stuffs in my shopping list')
    print('I completed my shopping')
    print('I am at the registry for payment')
    print('Payment is completed')
    print('driving back to home \n\n')

let_us_shop(['Banana', 'carrot', 'milk', 'juice'])

def let_us_shop_with_loop(shopping_list):
    i = 1
    for product in shopping_list:
        print(f'This is product number {i} and the product name is: {product}')
        i += 1

print('Calling let_us_shop_with_loop() function now')
print('#############################################')
let_us_shop_with_loop(['Banana', 'carrot', 'milk', 'juice', 'Socks', 'TB', 'Tooth Paste', 'AAA', "BBB"])
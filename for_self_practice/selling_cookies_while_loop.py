def sell_cookies(number_of_cookies):
    print(f'This is the total cookies for sale: {number_of_cookies}')
    total_sales_value = 0
    while number_of_cookies != 0:
        total_sales_value += 1 * .5
        number_of_cookies -= 1
    print(f'This is the total sale amount: {total_sales_value}')


number_of_cookies_to_sell = int(input('Enter the number of cookies to sell:'))
sell_cookies(number_of_cookies_to_sell)

'''
5. You have your restuarant open at 6:00pm for dinner. Your restuarant has seating capacity for 50 diners. Your customers called earlier in the day and made the following booking for seats. Here are the break up for the customers:
	Family of John: 8 members
	Rajan as single diner
	Das with his wife and a child (needing an individual seat)
	Joe comes with his girl friend
	Gupta celebrating his son's birth day takes 12 seats
	Gopi brings his 10 friends for a treat for his promotion
	Create a suitable data structure to record the advance bookings and allow the booking
	to continue as long as seats are available. At any given point of time,
	you should know how many seats are available (if any)
'''

TOTAL_SEATS = 50
available_seats = 50
guests_list = []
number_of_guests = list(range(1,51))


def call_reservation(available_seats):
    while (available_seats > 0):
        print(f'The number of seats currently available is: {available_seats}')
        guests_count = int(input('Please enter the number of guests for booking: '))
        if guests_count == 0 or guests_count < 0:
            print('Reservation should be for 1 or more people; invalid number input for reservation')
        if guests_count > available_seats:
            print(f'Sorry, we are unable to book for {guests_count} as seats are NOT NOW AVAILABLE')
        else:
            guest_name_for_booking_ref = input('Please enter the name fo guest for  booking: ')
            guests_list.append(guest_name_for_booking_ref)
            number_of_guests[guests_list.index(guest_name_for_booking_ref)] = guests_count
            available_seats -= guests_count
            # print(f'Currently the number of seats available is: {available_seats}')
            res_continue_opt = input('Enter "y" for continue booking or "n" for end booking: ')
            if res_continue_opt == 'n':
                break
    if available_seats == 0:
        print(f'We appreciate your patronage; however there is wait time before we can take your reservation. Thank YOU')
    call_option(available_seats)


def print_booking_list(available_seats):
    remaining_seats = 50
    if len(guests_list) == 0:
        print('There are currently no reservatins appearing in the list.')
    else:
        for name in guests_list:
            print(f'Guest: {name} has {number_of_guests[guests_list.index(name)]} seats reserved')
            remaining_seats -= number_of_guests[guests_list.index(name)]
        available_seats = remaining_seats
    call_option(available_seats)


def call_option(available_seats):
    option = int(input(f'Please enter 1 for Booking List, 2 for Reservation, or 3 for Ending Program: '))
    if option == 1:
        print_booking_list(available_seats)
    elif option == 2:
        call_reservation(available_seats)
        call_option(available_seats)
    elif option == 3:
        print('Thank you for patronage; see you next time. Bye now!!!')
        quit()
    else:
        print(f'Enter either 1, 2, or 3')
        call_option(available_seats)


call_option(available_seats)

def fetch_user_name(voters_list_abb, user_selection):
    return [item[1] for item in voters_list_abb if item[0] == user_selection]

def print_voter_list(int_voters_list):
    voter_list = []
    for item in int_voters_list:
        ind_tuple = (item[0], item[1])
        voter_list.append(tuple(ind_tuple))

    return voter_list

def validate_user(voters_list_num, user_name, voter_id):
    for item in voters_list_num:
        if item[0] == voter_id:
            if user_name == item[1]:
                print(f'SUCCESS: The voter ID entered for user {user_name} matches.')
            else:
                print(f'FAILURE: The voter ID entered for user {user_name} does not match.')
            break
    else:
        print(f'FAILURE: The voter ID entered for user {user_name} does not match.')

voters_list_abb = [("a", "Rajan"), ("b", "Ravi"), ("c", "Radha"), ("d", "Ramya"),
               ("e", "Raghu"), ("f", "Rashmi"), ("g", "Rajesh"), ("h", "Rangan"),
                   ("i", "Ram"), ("j", "Manoj")]

voters_list_num = [(1, "Rajan"), (2, "Ravi"), (3, "Radha"), (4, "Ramya"),
               (5, "Raghu"), (6, "Rashmi"), (7, "Rajesh"), (8, "Rangan"),
                   (9, "Ram"), (10, "Manoj")]

print(f'Below provided is the list of voters:\n'
      f'a : Rajan\n b: Ravi\n c: Radha\n d: Ramya\n e: '
      f'Raghu\n f: Rashmi\n g: Rajesh\n h: Rangan\n i: Ram\n j: Manoj')

user_selection = input('The user selected: ')
# print(f'The user selected abbreviation is: {user_selection}')

if len(fetch_user_name(voters_list_abb, user_selection)) == 1:
    fetch_user_name(voters_list_abb, user_selection)
    print(f'The user name is : {fetch_user_name(voters_list_abb, user_selection)}')

    voter_id = int(input('The Voter ID is: '))
    # if voter_id > 0  and voter_id < 11:
    print(f'The user selected abbreviation: {user_selection}, which is the code for voter: {fetch_user_name(voters_list_abb, user_selection)[0]} and {voter_id} was entered as his voter ID.')
    print(f'The voter\'s list is: {print_voter_list(voters_list_num)}')
    validate_user(voters_list_num, fetch_user_name(voters_list_abb, user_selection)[0], voter_id)
    # else:
    #     print(f'USER INPUT INCORRECT: The voter ID the user entered is invalid.')
else:
    print(f'USER INPUT INCORRECT: Invalid abbreviation entered.')

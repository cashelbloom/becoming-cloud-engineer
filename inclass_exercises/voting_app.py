
def fetch_user_name(int_voters_list, user_selection):
    return [item[2] for item in int_voters_list if item[0] == user_selection]

def print_voter_list(int_voters_list):
    voter_list = []
    for item in int_voters_list:
        ind_tuple = (item[1], item[2])
        voter_list.append(tuple(ind_tuple))

    return voter_list

def validate_user(int_voters_list, user_selection, voter_id):
    for user_alpha, user_num, user_name in int_voters_list:
        # print(f' the Item is: {user_alpha}-{user_num}-{user_name}, user_selection is: {user_selection}')
        if user_selection == user_alpha:
            if voter_id == user_num:
                print(f'SUCCESS: The voter ID entered for user {user_name} matches.')
            else:
                print(f'FAILURE: The voter ID entered for user {user_name} does not match.')
            break

int_voters_list = [("a", 1, "Rajan"), ("b", 2, "Ravi"), ("c", 3, "Radha"), ("d", 4, "Ramya"),
               ("e", 5, "Raghu"), ("f", 6, "Rashmi"), ("g", 7, "Rajesh"), ("h", 8, "Rangan"),
                   ("i", 9, "Ram"), ("j", 10, "Manoj")]

print(f'Below provided is the list of voters:\n'
      f'a : Rajan\n b: Ravi\n c: Radha\n d: Ramya\n e: '
      f'Raghu\n f: Rashmi\n g: Rajesh\n h: Rangan\n i: Ram\n j: Manoj')

user_selection = input('The user selected: ')
# print(f'The user is: {user_selection}')

voter_id = int(input('The Voter ID is: '))
print(f'The user selected: {user_selection}, which is the code for voter: '
      f'{fetch_user_name(int_voters_list, user_selection)[0]} and {voter_id} was entered as his voter ID.')
print(f'The voter\'s list is: {print_voter_list(int_voters_list)}')
validate_user(int_voters_list, user_selection, voter_id)


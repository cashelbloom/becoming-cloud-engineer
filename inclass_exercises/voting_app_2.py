
def fetch_user_name(voters_list_abb, user_selection):
    return [item[1] for item in voters_list_abb if item[0] == user_selection]

def print_voter_list(int_voters_list):
    voter_list = []
    for item in int_voters_list:
        ind_tuple = (item[0], item[1])
        voter_list.append(tuple(ind_tuple))

    return voter_list

def validate_user(voters_list_num, user_name, voter_id):
    result = False
    for item in voters_list_num:
        if item[0] == voter_id:
            if user_name == item[1]:
                print(f'SUCCESS: The voter ID entered for user {user_name} matches.')
                result = True
            else:
                print(f'FAILURE: The voter ID entered for user {user_name} does not match.')
            break
        else:
            print(f'FAILURE: The voter ID entered for user {user_name} does not match.')
    return result

def data_structure():
    voters_list_abb = [("a", "Rajan"), ("b", "Ravi"), ("c", "Radha"), ("d", "Ramya"),
               ("e", "Raghu"), ("f", "Rashmi"), ("g", "Rajesh"), ("h", "Rangan"),
                   ("i", "Ram"), ("j", "Manoj")]

    voters_list_num = [(1, "Rajan"), (2, "Ravi"), (3, "Radha"), (4, "Ramya"),
               (5, "Raghu"), (6, "Rashmi"), (7, "Rajesh"), (8, "Rangan"),
                   (9, "Ram"), (10, "Manoj")]

    return voters_list_abb, voters_list_num

def accept_user_abbreviation():
    voters_list_abb, voters_list_num = data_structure()
    print(f'Below provided is the list of voters:\n'
          f'a : Rajan\n b: Ravi\n c: Radha\n d: Ramya\n e: '
          f'Raghu\n f: Rashmi\n g: Rajesh\n h: Rangan\n i: Ram\n j: Manoj')
    result = False
    user_attempt_abb = 0
    while user_attempt_abb < 3:
        user_selection = input('Please enter your abbreviation: ')
        # try:
        user_selection = str(user_selection)
        if len(fetch_user_name(voters_list_abb, user_selection)) == 1:
            user_name = fetch_user_name(voters_list_abb, user_selection)[0]
            print(f'The user name is : {fetch_user_name(voters_list_abb, user_selection)[0]}')
            user_attempt_abb = 10
            result = True
            return result, user_selection, user_name
        else:
            user_attempt_abb += 1
            print(f'USER INPUT INCORRECT: Invalid abbreviation entered in the previous attempt. '
                  f'You have {3 - user_attempt_abb} attempts left.')

        if user_attempt_abb == 3:
            return result, user_selection, ""


def validate_and_accept_voter_id(user_name):
    voters_list_abb, voters_list_num = data_structure()
    user_attempt_int_id = 0
    result = False
    while user_attempt_int_id < 3:
        voter_id = input('The Voter ID is: ')
        try:
            voter_id = abs(int(voter_id))
            print(f'Entered number is an int.')
            if voter_id > 0 and voter_id < 11:
                print(f'The user selected abbreviation: {user_selection}, '
                      f'which is the code for voter: {fetch_user_name(voters_list_abb, user_selection)[0]} '
                      f'and {voter_id} was entered as his voter ID.')
                print(f'The voter\'s list is: {print_voter_list(voters_list_num)}')
                user_attempt_int_id = 10
                result = validate_user(voters_list_num, fetch_user_name(voters_list_abb, user_selection)[0], voter_id)
                return result
            else:
                user_attempt_int_id += 1
                print(f'USER ERROR: Invalid voter ID entered in previous attempt. '
                      f'You have {3 - user_attempt_int_id} attempts left.')
        except ValueError:
            try:
                voter_id = str(voter_id)
                user_attempt_int_id += 1
                print(f'USER ERROR: The entered value is a string in previous attempt. '
                      f'You have {3 - user_attempt_int_id} attempts left.')
            except ValueError:
                voter_id = float(voter_id)
                user_attempt_int_id += 1
                print(f'USER ERROR: The entered value is a float in previous attempt. '
                      f'You have {3 - user_attempt_int_id} attempts left.')


        if user_attempt_int_id == 3:
            return result, user_selection, ""

def present_ballot_paper_and_accept_vote():
    print(f'BALLOT paper: \n'
          f'1. John David - People Party - Peacock\n'
          f'2. Jay Sam  - Labour Party - Donkey \n'
          f'3. Cathy Joe - Liberal Party - Book \n'
          f'4. Ray Jenson - Independent - Plane\n')
    result = False
    ballot = 0
    while ballot < 3:
        vote = input(f'Please cast your valuable vote, you have 3 attempts to input a valid valid integer:')

        try:
            vote = abs(int(vote))
            print(f'Vote entered is an integer')
            if vote > 0 and vote < 5:
                print(f'Vote casted is valid.')
                # casted_votes = {}
                # casted_votes
                result = True
                return result, vote
            else:
                ballot += 1
                print(f'USER ERROR: Invalid vote casted in previous attempt. '
                      f'You have {3 - ballot} attempts left.')

        except ValueError:
            try:
                voter_id = str(vote)
                ballot += 1
                print(f'USER ERROR: The entered value is a string in previous attempt. '
                      f'You have {3 - ballot} attempts left.')
            except ValueError:
                voter_id = float(vote)
                ballot += 1
                print(f'USER ERROR: The entered value is a float in previous attempt. '
                      f'You have {3 - ballot} attempts left.')


    return result, vote

# def validate_accept_vote(vote):
#     if vote > 0 and vote < 5:
#         print(f'')



result, user_selection, user_name = accept_user_abbreviation()
if result:
    result = validate_and_accept_voter_id(user_selection)
if result:
    result, vote = present_ballot_paper_and_accept_vote()
if result:
    # result = validate_accept_vote(vote)
    print(f'Vote entered is {vote}')
else:
    print('USER FAILURE: Incorrect entry for vote.')



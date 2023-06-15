master_voters_list = {
    "manoj": 1,
    "anu": 2,
    "sukhi": 3,
    "sanaa": 4,
    "mahesh": 5,
    "madhu": 6,
    "aathreya": 7,
    "Millie": 8,
    "Raghu": 9,
    "ramya": 10
}

remaining_voters_list = {
    "manoj": 1,
    "anu": 2,
    "sukhi": 3,
    "sanaa": 4,
    "mahesh": 5,
    "madhu": 6,
    "aathreya": 7,
    "Millie": 8,
    "Raghu": 9,
    "ramya": 10
}

def move_voter_to_voted_list(fname):
    print(f'voter to be moved is: {fname}')
    for k,v in remaining_voters_list.items():
        # print(f'key {k}, value: {v}')
        if k.upper() == fname:
            voted_voters_list[k] = v
            del remaining_voters_list[k]
            print(f'Master voters: {master_voters_list}')
            print(f'Remaining voters: {remaining_voters_list}')
            print(f'Voted voters: {voted_voters_list}')
            break

def validate_user_exists (fname):
    match = False
    for k,v in master_voters_list.items():
        if fname == k.upper():
            match = True

    return match

voters_count = 0
# user_match = False
voted_voters_list = {}
while voters_count < 5:

    name = input("Enter your name:").upper()
    print(f'The name of the voter is: {name}')
    user_match = validate_user_exists(name)
    if user_match:
        vote = input("Enter your choice of candidate ranging from 1 - 4: ")
        print(f'The candidate chosen is: {vote}')
        move_voter_to_voted_list(name)
        voters_count += 1
    else:
        print(f'Voter name entered does not match.')
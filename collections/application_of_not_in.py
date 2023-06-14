my_votes = {
    'aaa': 1000, 'bbb': 250, 'ccc':289, 'ddd': 299, 'eee': 533
}

my_votes = {k: v+50 for k,v in my_votes.items() if v <= 250}
# print(my_votes)
'''
For the eVoting System, we have the expectation to have 3 dictionaries:
    1. Original Voters List (that has all the eligible voters for a partcular voting location)
    2. Voters who have completed their voting
    3. Current outstanding voters yet to vote.
For this scenario, we can use the Dictionary Comprehension.
'''
original_voters_list = {'aaa': 1, 'bbb': 2, 'ccc': 3, 'ddd': 4, 'eee': 5, 'fff': 6, 'ggg': 7,
                        'hhh': 8, 'iii': 9, 'jjj': 10}
current_voters_list = original_voters_list
print(f'This is the start of the voters" list at the time polling commences: {current_voters_list}')
voted_voters_list = {'aaa': 1, 'bbb': 2}
remaining_voters_list = {}
for kc in current_voters_list.items():
    can_add = True
    for kv in voted_voters_list.items():
        if kc[0] == kv[0]:
            can_add = False
            break
    if can_add:
        remaining_voters_list.update({kc[0]: kc[1]})
        print(f'The value of kc: {kc}')
print(f'Currently these are the voters remaining to vote: {remaining_voters_list}')
##########################################################







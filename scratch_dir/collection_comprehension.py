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
print(f'original voters list: {original_voters_list}')
current_voters_list = original_voters_list
voted_voters_list = {'aaa': 1, 'bbb': 2}
# del {current_voters_list[k]} for k in voted_voters_list.keys()
# print(f'New dict: {new_dict}')
# print(f'original voters list {k: v for k,v in original_voters_list.items()}')
remaining_voters = del current_voters_list[k] for k in voted_voters_list.items()
# print(f'remaining voters: {remaining_voters}')
########################
# using range in list comprehension:
new_list = [i * 2 for i in range(1,5)]
print(f'new list from range: {new_list}')







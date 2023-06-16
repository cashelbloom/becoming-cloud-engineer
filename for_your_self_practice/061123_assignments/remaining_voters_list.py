'''
In this exercise, you are going to write program that will provide a dictionary of the voters who have not yet voted on
a given time on the voting day.
You will have a master voting list as a Python dictionary that will contain all the voter names
and their corresponding voter ids.
This list will NOT change at all.
You will have another dictionary that is the duplicate of the master voting list. At the beginning of the voting ,
this duplicate voter list will have the exact voter list as in the master voting list.
Call this duplicate dictionary as remaining_voters_list
You will have another voter list (a dictionary) that would hold the voters who have voted so far.
Call this dictionary as voted_voters_list.
As a voter completes voting, your program should remove the voter from the remaining_voters_list
and add the same voter to the voted_voters_list.
Have 10 voters in your master voting list and have a while loop for 5 voters to vote.
After the while loop, print the voters in the remaining_voters_list and the voted_voters_list and see if they print
as expected.
'''

master_voting_list = {
    'Ramya': 1,
    'Tharani': 2,
    'Radha': 3,
    'Manoj': 4,
    'Raghu': 5,
    'Ganesan': 6,
    'Sreya': 7,
    'Tanishi': 8,
    'Kimaya': 9,
    'Praku': 10
}

remaining_voters_list = master_voting_list.copy()
print(remaining_voters_list)

voted_voters_list = {}


count = 1

while count <= 5:
    voter = input('Voters name: ')
    for k, v in master_voting_list.items():
        if k == voter:
            voted_voters_list[k] = v
            del remaining_voters_list[k]
            count += 1
else:
    print(f'Voters voted list: {voted_voters_list}')
    print(f'Remaining voters list: {remaining_voters_list}')


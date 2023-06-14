my_votes = 3000
print(f'Print my vote count: {my_votes}')



def change_my_votes(votes_to_add):
    global my_votes
    my_votes +=votes_to_add
    print(f'Print my vote count: {my_votes}')


change_my_votes(20000)
print(f'Print my vote count: {my_votes}')
my_votes = 15000
print(f'Print my vote count: {my_votes}')




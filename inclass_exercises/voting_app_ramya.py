import json

with open('contestants.json') as contestants_file:
    contestants = json.load(contestants_file)
    print(contestants)

# voters = [(1, "a"), (2, "b"), (3, "c"), (4, "d"), (5, "e")]
# for i, j in voters:
#     print(j)


voters_name = [('a', 'Rajam'),('b','Ravi'),('c', 'Radha'),( 'd', 'Ramya'),(  'e', 'Raghu'),('f', 'Rashmi'),('g','Rajam'),('h','Rangan'),('i', 'Ram'),( 'j', 'Manoj')]

voters_id = [(1, 'Ram'), (2, 'Raghu'), (3, 'Ramya'), (4, 'Tharani'), (5, 'Manoj'), (6, 'Radha'), (7, 'Ravi'), (8, 'Rashmi'), (9, 'Rangan'), (10, 'Rajam')]

for code,name in voters_name:
    print( f'Code {code}: name {name}')

# letter = input("Enter the letter corresponding to your name: ")
# voter_id = int(input("Enter your voter id number: "))

def voter_match(letter, voter_id ):
    name = [j for i, j in voters_name if i == letter]
    print(name[0])
    flag = False

    for k, q in voters_id:
        if q == name[0] and k == voter_id:
            flag = True
            print(f'Voter Id {k} is matched for voter: {q}')
            break
    if flag:
        return True
    else:
        return False

attempts = 1
flag = False
while attempts <= 3:
    letter = input("Enter the letter corresponding to your name: ")
    voter_id = int(input("Enter your voter id number: "))
    value = voter_match(letter, voter_id)
    if value:
        print('Match')
        flag = True
        break
    else:
        print('Try again!')
        print(f'{attempts} Failed!')
        voter_match(letter, voter_id)
        attempts += 1

if flag:
    print(f'You Match. Please Vote')
else:
    print(f"Your attempts exhausted. You can't vote")
    exit()

ballot = [('Peacock', 'John David'), ('Donkey', 'Jay Sam'), ('Book', 'Cathy Joe'), ('Plane', 'Ray Jenson')]

symbol = input("Enter the symbol: ")

candidate_name = [t for s, t in ballot if s == symbol]
print(candidate_name)

candidate_count = {'John David': 0, 'Jay Sam':0,'Cathy Joe': 0,'Ray Jenson':0 }

candidate_vote = input("Do you want to vote? ")

voting = 0
count = 0

while voting <= 10:
    for s,c in ballot:
        if s == symbol and candidate_vote == 'Yes':
            print(c)
            candidate_count[c] += 1
            # candidate_count.update()
            # candidate_count[c] = count
            print(candidate_count)
    else:
        symbol = input("Enter the symbol: ")
        candidate_vote = input("Do you want to vote? ")
        voting += 1









# name = [j for i, j in voters_name if i == letter]
# print(f'This is the name {name}')
# print(name[0])
# flag = False
# attempts = 1
#
# while attempts <= 3:
#     for k, q in voters_id:
#         if q == name[0] and k == voter_id:
#             flag = True
#             print(f'Voter Id {k} is matched for voter: {q}')
#             break
#         else:
#            print(f'{attempts} Attempts failed to match the voter name')
#            print('Please Try again!')
#            attempts += 1





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

letter = input("Enter the letter corresponding to your name: ")
voter_id = int(input("Enter your voter id number: "))

name = [j for i, j in voters_name if i == letter]
print(f'This is the name {name}')
print(f'The data type of name {type(name)}')
# if len(name) == 1:
#     print(f'The name is {name}')
# else:
#     print(f'Please enter valid code')

print(name[0])
flag = False

for k, q in voters_id:
    if q == name[0] and k == voter_id:

        # if k == voter_id:
        flag = True
        break
            # print(f'Voter Id {k} is matched for voter: {q}')

if flag:
    print(f'Voter Id {k} is matched for voter: {q}')
else:
    print('No Match')



















# for i, j in voters_name:
#     if i == letter:
#         print(j)
#         for k,q in voters_id:
#             #print(q)
#             if q == j:
#                 print(f'Voter ID {voter_id} is matched for voter: {q}')
#                 print(f'This is the verification result: True')

# name = [j for i, j in voters_name if i == letter]
# print(name)
#
# id_name = [q for k, q in voters_id if q == name]
# print(id_name)
















import os
import sys
import json
# sys.path.append("/random_dir")
import random_dir.randomint as ri
import inclass_exercises.voters_list as vl


# my_randintgen = ri.RandIntGen(1,5,1)
# my_randintgen.generate_rand_int(20)

def get_voter_name(voter_selection):
    match voter_selection:
        case 'a': return 'Rajam'
        case 'b': return 'Ravi'
        case 'c': return 'Radha'
        case 'd': return 'Ramya'
        case 'e': return 'Raghu'
        case 'f': return 'Rashmi'
        case 'g': return 'Rajam'
        case 'h': return 'Rangan'
        case 'i': return 'Ram'
        case 'j': return 'Manoj'
        case _: return 'Error'


def verify_voter_id(voter_id, voter_name) -> bool:
    is_verified = False
    print(f'This is the voters list:\n {vl.voters_list}')
    for item in vl.voters_list:
        # print(f'This is the item: {item}')
        # print(f'The key is: {item[0]} The name is: {item[1]}')
        if item[0] == voter_id and item[1] == voter_name:
            print(f'Voter ID {voter_id} is matched for voter: {voter_name}')
            is_verified = True
            print(f'This is the verification result: {is_verified}')
            return is_verified
    print(f'This is the verification result: {is_verified}')
    return is_verified

def distribute_ballot():
    with open('contestants.json') as contestants:
        contestants = json.load(contestants)
        print(f'the contents of contestant: {contestants}')
        print(f'The data type of contestants: {type(contestants)}')
        for item in contestants['contestants']:
            # k for k in item:
            #     print(f'the outcome of calling list comprehension: {k}')

        # for [*item] in contestants['contestants']:
        #     print(f'Item data type is: {type(item)}')
            # print(f'the keys in this dict are: {dict(item).keys()}')
            # print(f'the values in this dict are: {dict(item).values()}')
            print(f'contestant: {list(item.keys())[0]} and symbol: {list(item.values())[0]}')
            # for k, v in item:
            # print(f'Key is: {[*item][0]}')


def display_voters_list():
    print('a : Rajam')
    print('b : Ravi')
    print('c : Radha')
    print('d : Ramya')
    print('e : Raghu')
    print('f : Rashmi')
    print('g : Rajam')
    print('h : Rangan')
    print('i : Ram')
    print('j : Manoj')

display_voters_list()
voter_selection = input('Enter the letter corresponding to your name: ')
voter_name = get_voter_name(voter_selection)

voter_id = int(input('Enter your voter id number: '))

if verify_voter_id(voter_id, voter_name):
    distribute_ballot()
else:
    print('Sorry, you couldn"t verify correctly; bring authentic proof for voting')









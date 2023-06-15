import csv
import random
import string
def random_char(y):

       return ''.join(random.choice(string.ascii_letters) for x in range(y))

def random_num():
    fixed_digits = 5
    return random.randrange(111111, 999999, fixed_digits)

def validate_user_input(fname):
    result = False
    try:
        val = int(fname)
        result = True
    except ValueError:
        print("The user entered a number!!")
        # result = False

    return result

def find_nato_alphas(fname, fnato_codes):
    # print(f'Length of dict {len(fnato_codes)}')
    nato_code_dict = {}

    for item in fname:
        counter = 0
        for key in fnato_codes:
            counter += 1
            print(f'ITEM is:{item}, counter: {counter}')
            print(f'Key is {fnato_codes[key]}')
            if item == key:
                # print(f'{item} : {fnato_codes[key]} ', end=' ')
                nato_code_dict[item] = fnato_codes[key]
                match = True
                break
            elif item != key and counter == len(fnato_codes):
                nato_code_dict[str(random_num())+random_char(5)] = str(item)

    print(f'The nato code dictionary for the name {fname} is: {nato_code_dict}')

with open('C:\\gitrepos\\becoming-cloud-engineer\\data_folder\\nato_phonetic_alphabet.csv', mode='r') as nato_file:
    data = csv.reader(nato_file)
    nato_codes = {rows[0]:rows[1] for rows in data}
print(nato_codes)
# print(f'Type of nato_codes is: {type(nato_codes)}')
name=input("Please type your name:").upper()

print(f'The name typed is : {name}')

find_nato_alphas(name, nato_codes)
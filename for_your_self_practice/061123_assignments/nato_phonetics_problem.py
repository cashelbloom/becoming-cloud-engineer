'''
In this problem, you will read a .csv file. This file will have comma (,)  separated alphabet and its word.
You are expected to write a Python program that will:
    1. Read the .csv file
    2. Create a dictionary for the contents of the file
    3. You will ask a user to input any word. The input should be converted to all upper case letters.
    4. For the input word, your program should create a Python dictionary.
        This dictionary will have the letters of the input word as key and the corresponding word as its value.
        For example, if the user inputs the word 'Becoming' then your program output should be as:
            {'B': 'Bravo', 'E': 'Echo', 'C': 'Charlie', 'O': 'Oscar', 'M': 'Mike',
            'I': 'India', 'N': 'November', 'G': 'Golf'}

The .csv file is located in the 'data_folder' and the file name is: 'nato_phonetic_alphabet.csv'
'''
#
# import os
# print(os.getcwd())
# C:\gitrepos\becoming-cloud-engineer\data_folder\nato_phonetic_alphabet.csv

import json

# with open('example.json','r') as read_nato_file:
#      j = json.load(read_nato_file)
#      print(j)
#      print(type(j))

nato_dict = {}
with open('../../data_folder/nato_phonetic_alphabet.csv', 'r') as read_nato_file:
    lines = read_nato_file.read().splitlines()
    print(type(lines))
    print(lines)
    for line in lines:
        nato = line.split(',')
        nato_dict[nato[0]] = nato[1]
print(nato_dict)

word = input("Enter any word: ").upper()
word_list = list(word)
print(word_list)

word_dict = {}

nato_dict_keys = nato_dict.keys()
print(nato_dict_keys)

for w in word_list:
     if w in nato_dict.keys():
          word_dict[w] = nato_dict[w]
print(word_dict)


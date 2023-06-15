with open('../data_folder/nato_phonetic_alphabet.csv', 'r+') as file_opening_check:
    the_contents = file_opening_check.read()
    print(f'The  contents of the file as it is read {the_contents}')
print(f'Printing the contents of the file outside of the with block: {the_contents}')
with open('../data_folder/nato_phonetic_alphabet.csv', 'a') as file_opening_check:
    file_opening_check.write('I am adding a new line.')
with open('../data_folder/nato_phonetic_alphabet.csv', 'r+') as file_opening_check:
    the_contents = file_opening_check.read()
print(f'Printing the contents of the file 2nd time after adding a new string at the end: {the_contents}')
with open('../data_folder/nato_phonetic_alphabet.csv', 'a') as file_opening_check:
    file_opening_check.write('I am adding a new line.')



# with open('../data_folder/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv') as nato_alpha:
#     print(nato_alpha.read())
with open('../data_folder/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv') as nato_alpha1:
    data_from_csv_file = nato_alpha1.read()
    print(f'printing from data_from_csv_file: {data_from_csv_file}')
print(f'The data type of data_from_csv_file: {type(data_from_csv_file)}')
letter_word_list = data_from_csv_file.split('\n')
print(f'tuple: letter_word_tuple {letter_word_list}')
new_dict = {item.split(',')[0]: item.split(',')[1] for item in letter_word_list}
new_dict_2 = {item.split(',')[1]: item.split(',')[0] for item in letter_word_list}
print(f'value of new_dict: {new_dict}')
print(f'value of new_dict: {new_dict_2}')


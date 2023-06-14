import pandas

data = pandas.read_csv('../data_folder/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv')
print(data)
alpha_word_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(f'printing from alpha_word_dict: {alpha_word_dict}')
user_input_word = input('Please enter your word for NATO phonetics: ').upper()
phonetic_dict_for_user_word = {letter: alpha_word_dict[letter] for letter in user_input_word}
print(f'for the user: {phonetic_dict_for_user_word}')
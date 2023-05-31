my_books_tuple = ('scienceBook', 'historyBook', 'mathBook', 'languageBook', 'socialStudiesBook')
print(f'Just wanted to know the data type of my_books_tuple {type(my_books_tuple)}')

my_books = ['scienceBook', 'historyBook', 'mathBook', 'languageBook', 'socialStudiesBook']
print(f'Just wanted to know the data type of my_books {type(my_books)}')
print(f'Here is the contents to start with of my_books {my_books}')
my_sports_list = ['basketball', 'hockey']
print(f'Tell me the data type of my_sports_list:  {type(my_sports_list)}')

my_sports_tuple = ('basketball',)
print(f'Tell me the data type of my_sports_tuple:  {type(my_sports_tuple)}')
my_sports_list2 = list(my_sports_tuple)
my_sports_list2.append('baseball')
my_sports_tuple = tuple(my_sports_list2)
print(f'The contents of my_sports_tuple: {my_sports_tuple}')
print(f'The contents of my_sports_list2: {my_sports_list2}')

my_books.append('litBook')
print(f'Here is the current contents of my_books {my_books}')


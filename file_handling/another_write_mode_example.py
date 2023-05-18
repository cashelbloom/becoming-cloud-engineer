'''
    In this file, we open the file in write mode - first.
    If the file doesn't exist, a new file is opened with the name and location.
    If the file exists at the specified location, the file is overwritten.
    The string 'A sample text.' is written in the file.

    In the next block, we open the same file in 'read' mode and read its contents.
    The content of the file will only be 'A sample text.'
'''

with open('../instructions/test_file.txt', 'w') as my_text_file:
    my_text_file.write('A sample text.')

with open('../instructions/test_file.txt', 'r') as my_read_text_file:
    the_contents = my_read_text_file.read()
    print(the_contents)
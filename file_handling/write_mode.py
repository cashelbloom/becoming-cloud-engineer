my_sample_file = open('../instructions/file_handling.txt', 'w')
my_sample_file.write('This is the new line I am adding to ramya_test file write')
my_sample_file.close()
my_sample_file = open('../instructions/file_handling.txt', 'r')
my_file_contents = my_sample_file.read()
print(my_file_contents)
my_sample_file.close()


with open('../instructions/test_file.txt', 'x') as sample_file:
    sample_file.write('A new line is added.')
    print(sample_file)

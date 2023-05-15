my_sample_file = open('../instructions/file_handling.txt', 'w')
my_sample_file.write('This is the new line I am adding to test file write')
my_sample_file.close()
my_sample_file = open('../instructions/file_handling.txt', 'r')
my_file_contents = my_sample_file.read()
print(my_file_contents)
my_sample_file.close()



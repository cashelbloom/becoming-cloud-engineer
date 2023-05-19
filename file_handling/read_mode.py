import io

my_file = open('../instructions/file_handling.txt')
my_file_content = my_file.read()
print(my_file_content)
my_file.close()

# with open('../instructions/settingup-sshkey.txt') as ssh_key:
#     read_content = ssh_key.read()
#     print(read_content)
import io

my_file = open('../instructions/file_handling.txt', 'r+')
my_file_content = my_file.read()
print(my_file_content)
my_file.close()


# with open('../instructions/settingup-sshkey.txt') as ssh_key:
#     read_content = ssh_key.read()
#     print(read_content)
# Use the keyword 'with' so there is no need to explicitly call file.close()
with open('D:\\gitrepos\\becoming-cloud-engineer\\instructions\\file_handling.txt') as ssh_key:
    read_content = ssh_key.read()
    print(read_content)

with open('../instructions/settingup-sshkey.txt', 'r+') as my_file:
    read_content = my_file.read()
    print(read_content)
    my_file.write('Adding a new line at the end of the current contents')
with open('../instructions/settingup-sshkey.txt', 'r') as my_file2:
    read_content2 = my_file2.read()
    print(read_content2)

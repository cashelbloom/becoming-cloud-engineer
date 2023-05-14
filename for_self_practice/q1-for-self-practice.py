# Reference for question 1 - 'for self practice'

data_types_list = ['str', 'int', 'float', 'bool', 'list', 'dict']
data_types_desc_list = ['String', 'Integer', 'Decimal', 'Boolean', 'List', 'Dictionary']
index = 0
for item in data_types_list:
    print(f'{index + 1}. {item} is for {data_types_desc_list[index]} types.')
    index += 1


def printing_data_types(type_list, desc_list):
    starting = 0
    for data_type in type_list:
        print(f'{starting + 1}. {data_type} is for {desc_list[starting]} types.')
        starting += 1


data_types = ['str', 'int', 'float', 'bool', 'list', 'dict']
data_type_descs = ['String', 'Integer', 'Decimal', 'Boolean', 'List', 'Dictionary']
printing_data_types(data_types, data_type_descs)

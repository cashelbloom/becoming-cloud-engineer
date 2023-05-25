def printing_data_types(type_list, desc_list):
    for data_type in type_list:
        curr_index = type_list.index(data_type)
        print(f'{curr_index + 1}. {data_type} is for {desc_list[curr_index]} types.')
        # starting += 1


data_types = ['str', 'int', 'float', 'bool', 'list', 'dict']
data_type_descs = ['String', 'Integer', 'Decimal', 'Boolean', 'List', 'Dictionary']
printing_data_types(data_types, data_type_descs)
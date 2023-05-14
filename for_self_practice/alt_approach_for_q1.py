def printing_data_types(type_list, desc_list):
    for data_type in type_list:
        curr_data_type = data_type
        curr_index = type_list.index(curr_data_type)
        print(f'{curr_index + 1}. {curr_data_type} is for {desc_list[curr_index]} values.')
        # starting += 1


data_types = ['str', 'int', 'float', 'bool']
data_type_descs = ['String', 'Integer', 'Decimal', 'Boolean']
printing_data_types(data_types, data_type_descs)
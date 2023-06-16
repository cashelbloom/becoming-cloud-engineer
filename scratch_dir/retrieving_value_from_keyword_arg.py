def retrieve_value_from_a_kw_arg(**names):
    print(f'The data type of names: {type(names)}')
    for item in names.items():
        print(f'The data type of item: {type(item)}')
        print(f'Key is: {item[0]} and value is: {item[1]}')
#
    for k,v in names.items():
        print(f'The data type of k {type(k)} and type v: {type(v)}')
        print(f'Key is: {k} and value is: {v}')


retrieve_value_from_a_kw_arg(name = 'Raj',  desig = 'SE', salary = '$90000', location = 'Bloomington')


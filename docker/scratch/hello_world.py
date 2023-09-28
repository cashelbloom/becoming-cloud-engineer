import json

def write_to_file(json_string):
    with open('from_container.txt', 'w') as my_cont_data:
        json.dump(json_string, my_cont_data, indent = 4)


def just_checking(event, context):
    print('Hello from Docker Container')
    print(f'This is the data from incoming event: {event}')
    print(f'This is the key in the incoming event data: {list(event.keys())[0]}')
    write_to_file(event)
    return 'All is well that ends well'


# just_checking({'greetings': 'Hello Class'}, None)
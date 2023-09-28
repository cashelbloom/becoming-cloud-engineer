import json

def just_checking(event, context):
    print('Hello from Docker Container')
    print(f'This is the data from incoming event: {event}')
    print(f'This is the key in the incoming event data: {list(event.keys())[0]}')
    print('I maded change in the volume and trying to see if container can show immediately the change made.')
    return 'All is well that ends well'


# lambda_handler({'greetings': 'Hello Class'}, None)
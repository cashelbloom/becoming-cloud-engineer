event = {"greetings": "Hello Class!"}
context = None

def say_hello(event, context):
    print('Hello from Docker Container to show this will be a new image built now')
    print(f'This is the data from incoming event: {event}')
    print(f'This is the key in the incoming event data: {list(event.keys())[0]}')
    print('I made change in the volume and trying to see if container can show immediately the change made.')
    return 'Hello Class, All is well that ends well'


say_hello(event, context)
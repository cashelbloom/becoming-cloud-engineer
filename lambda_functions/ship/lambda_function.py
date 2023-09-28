import json
import boto3
from ship import Ship

ddb_resource = boto3.resource('dynamodb')
table = ddb_resource.Table('ship-data-table')


def create_item(event_data):
    table.put_item(
        Item={'ship-id': event_data['shipId'],
              'ship-name': event_data['shipName'],
              'crew-strength': event_data['crewStrength'],
              'captain-name': event_data['captainName'],
              'current-port': event_data['currentPort'],
              'dest-port': event_data['destPort']
              }
    )


def handle_get(event_data):
    response = table.get_item(
        Key={
            'ship-id': event_data['queryStringParameters']['shipId']
        }
    )
    item = response['Item']
    print(f'This is the data returned for the GET: {item}')
    json_response = {
        'Call': 'Success',
        'ShipInfo': item['ship-name']
    }
    return {
        'statusCode': 200,
        'body': json.dumps(json_response)
    }


def handle_post(event_data):
    # my_ship = Ship(event_data['shipName'], event_data['currentPort'])
    # print(f'Right now I am at this port: {my_ship.port_anchored}')
    # my_ship.sail(event_data['destPort'])
    # my_ship.set_anchor(event_data['destPort'])
    # print(f'I have now anchored here at: {my_ship.port_anchored}')
    create_item(event_data)
    json_response = {
        "ShipName": event_data['shipName'],
        "PortAnchored": event_data['destPort']
    }
    return {
        'statusCode': 200,
        'body': json_response
    }


# def lambda_handler(event, context):
def lambda_handler():
    event = {
    "shipName": "rayalaseema",
    "destPort": "vizag",
    "currentPort": "Paris",
    "captainName": "Ramya",
    "crewStrength": 200,
    "shipId": "chennai-015"
}
    print(f'This is the data received from the event: {event}')
    # if 'queryStringParameters' in event:
    #     print('GET method invoked')
    #     return handle_get(event)
    # else:
    #     print('POST method invoked')
    return handle_post(event)

lambda_handler()


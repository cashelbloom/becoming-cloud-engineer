import json
import boto3
from ship import Ship
import os

sns_client = boto3.client('sns')
ddb_resource = boto3.resource('dynamodb')
# table = ddb_resource.Table('ship-data-table')
table = os.environ['DDB_TABLE_NAME']

def create_item(ship_data):
    table.put_item(
        Item = {'ship-id': ship_data['shipId'],
        'ship-name': ship_data['shipName'],
        'crew-strength': ship_data['crewStrength'],
        'captain-name': ship_data['captainName'],
        'current-port': ship_data['currentPort'],
        'dest-port': ship_data['destPort']
    }
)

def handle_get(event_data):
    response = table.get_item(
        Key= {
            'ship-id': event_data['queryStringParameters']['shipId']
        }
    )
    print(f'This is the full response received from DDB service: {response}')
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
    event_data_body = event_data['Records'][0]['body']
    print(f'body contents: {event_data_body} data type of body contents: {type(event_data_body)}')
    ship_data = json.loads(event_data['Records'][0]['body'])['body']
    print(f'This is ship_data contents: {ship_data}')
    print(f'The data type of ship_data is: {type(ship_data)}')
    create_item(ship_data)
    json_response = {
            "ShipName": ship_data['shipName'],
            "PortAnchored": ship_data['destPort']
    }
    return {
        'statusCode': 200,
        'body': json_response
    }

def publish_to_topic(sns_client, message):
    response = sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:126886581456:bce-async-flow-topic',
    Message=json.dumps(message),
    Subject='Message from SNS Topic',
    MessageStructure='string'
)
    return response
    


def lambda_handler(event, context):
    print(f'This is the data received from the event: {event}')
    sns_response = publish_to_topic(sns_client, event)
    print(f'This is the response from SNS: {sns_response}')
    
    # if 'queryStringParameters' in event:
    #     print('GET method invoked')
    #     return handle_get(event)
    # else:
    #     print('POST method invoked')
    #     return handle_post(event)
        
   
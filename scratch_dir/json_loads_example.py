import json

response = {
    "statusCode": 200,
    "body": "{\"Call\": \"Success\", \"ShipInfo\": \"sea-king\"}"
}

print(f'The data type of response is: {type(response)}')

body_json = response['body']
print(f'This is the data contained in the key "body": {body_json}')
print(f'This is the data type of the  "body" value: {type(body_json)}')
print(f'Now we are seeing in JSON format: {json.loads(body_json)}')
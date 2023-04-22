import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
table = dydb.Table('properties')
item={
        'str_address': '1045 S Maguire Street',
        'zip': '64093',
        'city': 'Warrensburg',
        'state': 'MO'
    }

table.put_item(Item=item)
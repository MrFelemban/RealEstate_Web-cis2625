import boto3

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Create the STUDENTS table with SID as partition key and Email as sort key
table = dynamodb.create_table(
    TableName='STUDENTS',
    KeySchema=[
        {
            'AttributeName': 'SID',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'Email',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'SID',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Email',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait for the table to be created before proceeding
table.meta.client.get_waiter('table_exists').wait(TableName='STUDENTS')

# Add 5 items to the table
table.put_item(
    Item={
        'SID': 1,
        'Email': 'john@example.com',
        'Name': 'John Doe',
        'Age': 25,
        'Gender': 'Male'
    }
)
table.put_item(
    Item={
        'SID': 2,
        'Email': 'jane@example.com',
        'Name': 'Jane Smith',
        'Age': 22,
        'Gender': 'Female'
    }
)
table.put_item(
    Item={
        'SID': 3,
        'Email': 'bob@example.com',
        'Name': 'Bob Johnson',
        'Age': 27,
        'Gender': 'Male'
    }
)
table.put_item(
    Item={
        'SID': 4,
        'Email': 'susan@example.com',
        'Name': 'Susan Lee',
        'Age': 24,
        'Gender': 'Female'
    }
)
table.put_item(
    Item={
        'SID': 5,
        'Email': 'mike@example.com',
        'Name': 'Mike Brown',
        'Age': 26,
        'Gender': 'Male'
    }
)

# Retrieve all items from the table
response = table.scan()

for item in response['Items']:
    print(item)

# Update an item in the table
table.update_item(
    Key={
        'SID': 2,
        'Email': 'jane@example.com'
    },
    UpdateExpression='SET Age = :age',
    ExpressionAttributeValues={
        ':age': 23
    }
)

# Retrieve the updated item
response = table.get_item(
    Key={
        'SID': 2,
        'Email': 'jane@example.com'
    }
)

print(response['Item'])

# Delete an item from the table
table.delete_item(
    Key={
        'SID': 5,
        'Email': 'mike@example.com'
    }
)

# Retrieve all remaining items from the table
response = table.scan()

for item in response['Items']:
    print(item)

import json
import boto3
import random

# import requests

tableName="TableContacts"
region="eu-central-1"

def list_contacts(event, context):
    dynamodb = boto3.resource('dynamodb', region_name=region)
    table = dynamodb.Table(tableName)
    scanResponse = table.scan()
    return {
        "statusCode": 200,
        "body": "{0}".format(scanResponse),
    }

def save_contact(event, context):
    dynamodb = boto3.resource('dynamodb', region_name=region)
    table = dynamodb.Table(tableName)
    
    print("Event recieved {0}".format(event['body']))

    response = table.put_item(
       Item={
            'contactId': "contact{0}".format(random.randint(1,999999)),
            'contact': event['body']
        }
    )

    print("PutItem succeeded with :{0}".format(response))
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Contact saved"
        }),
    }

def delete_contacts(event, context):
    dynamodb = boto3.resource('dynamodb', region_name=region)
    table = dynamodb.Table(tableName)
    removeContactId = event['queryStringParameters']['id']
    print("Event recieved {0}".format(event))
    print("Removing contact with ID {0}".format(removeContactId))
	
    response = table.delete_item(
        Key={
            'contactId': removeContactId
        }
    )

    print("Delete response {0}".format(response))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Contact deleted"
        }),
    }

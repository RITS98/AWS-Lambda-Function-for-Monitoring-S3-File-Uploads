import json

def lambda_handler(event, context):
    print("Response : ", event['responsePayload'])
    
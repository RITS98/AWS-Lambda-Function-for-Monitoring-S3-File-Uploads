import json

def lambda_handler(event, context):
    
    print("---------------------------------------------------------------------------------------------")
    print(f"Event : {event}")
    print(f"Context : {context}")
    print("Records : ", event['Records'][0])
    print("S3 Bucket Name : ", event['Records'][0]['s3']['bucket']['name'])
    print('File Name : ', event['Records'][0]['s3']['object']['key'])
    print('File Size : ', event['Records'][0]['s3']['object']['size'])
    
    
    if event['Records'][0]['s3']['object']['size'] <= 10**8:
        return {
            'statusCode' : 200,
            'body' : {
                'S3 Bucket Name' : event['Records'][0]['s3']['bucket']['name'],
                'S3 File Name': event['Records'][0]['s3']['object']['key'],
                'S3 File Size': event['Records'][0]['s3']['object']['size']
            }
        }
            
    else:
        return {
            'statusCode' : 413,
            'body' : 'File size greater than 100MB'
        }
   
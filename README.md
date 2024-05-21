# AWS-Lambda-Function-for-Monitoring-S3-File-Uploads

## Description
Develop an AWS Lambda function that is triggered by file upload events from an Amazon S3 bucket. The function should examine the size of the uploaded file, and if the file size exceeds 100MB, it should log an alert. This assignment aims to familiarize students with AWS
Lambda, Amazon S3, event-driven architecture, and basic logging practices.

## Steps
### S3 Bucket Creation
1. Create a new S3 bucket
   ![image](https://github.com/RITS98/Investigating-Netflix-Movies/assets/51791113/d94537df-1220-4131-b9a3-32f81a9bea7b)

### IAM Create User
1. Create IAM User
   ![image](https://github.com/RITS98/Investigating-Netflix-Movies/assets/51791113/0bd65ad2-d903-4054-8014-01fe81a7403b)
2. Create Roles (IAM -> Roles -> Create Roles)
   ![image](https://github.com/RITS98/Investigating-Netflix-Movies/assets/51791113/8f542735-aeca-4ddd-8d1a-e4408eac45a8)

### Create Lambda Function
1. Create4 a Lambda function
   ![image](https://github.com/RITS98/AWS-Lambda-Function-for-Monitoring-S3-File-Uploads/assets/51791113/04e4c2f7-e351-466f-b0e7-4ff6138cb1e4)
2. The new lambda function
   ![image](https://github.com/RITS98/AWS-Lambda-Function-for-Monitoring-S3-File-Uploads/assets/51791113/6168d2ce-8abc-4dc8-8363-929373aa5473)
3. The python code

4. Add Trigger
   ![image](https://github.com/RITS98/AWS-Lambda-Function-for-Monitoring-S3-File-Uploads/assets/51791113/f5861ee0-7611-4e8c-910f-a1412c154d79)
   ![image](https://github.com/RITS98/AWS-Lambda-Function-for-Monitoring-S3-File-Uploads/assets/51791113/b5b740ad-cfd1-4eb4-853b-a5ca13da5e3a)
6. Add Destination
   ![image](https://github.com/RITS98/AWS-Lambda-Function-for-Monitoring-S3-File-Uploads/assets/51791113/f405bbd2-e76f-4ab8-890c-c66152b8b318)
   ![image](https://github.com/RITS98/AWS-Lambda-Function-for-Monitoring-S3-File-Uploads/assets/51791113/72e413e7-5ef6-45b1-a2ad-8c2acb15c5fd)


### Test Results

1. Uploaded file less than 100 MB
![image](https://github.com/RITS98/AWS-Lambda-Function-for-Monitoring-S3-File-Uploads/assets/51791113/bbebcf65-3da1-45a8-9e04-fd298fb2b6fc)

2. Uploaded file greater than 100MB
   ![image](https://github.com/RITS98/AWS-Lambda-Function-for-Monitoring-S3-File-Uploads/assets/51791113/99b750a3-7dc1-4008-8b14-7dac1701a5d5)



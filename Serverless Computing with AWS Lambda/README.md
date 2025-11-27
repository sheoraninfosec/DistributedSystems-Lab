# Serverless Computing with AWS Lambda

## Setup AWS Account 
## Login using your credentials

## Install AWS CLI on macOS
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /

## Verify Installation 
aws --version

## Configure AWS CLI with IAM credentials
aws configure
### Enter:
### AWS Access Key ID
### AWS Secret Key
### Default region: ap-south-1 (Mumbai) recommended
### Output format: json

## Create Lambda Function Folder
mkdir lambda-exp
cd lambda-exp

nano app.py
<! def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello from AWS Lambda on macOS!"
    }
!>

## Zip the Lambda Function
zip function.zip app.py

## Create IAM Execution Role 
nano trust.json
<! {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
!>

## Create the Role
aws iam create-role \
  --role-name lambda-execution-role-exp \
  --assume-role-policy-document file://trust.json

## Attach the base execution policy
aws iam attach-role-policy \
  --role-name lambda-execution-role-exp \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

## Create Lambda fuction ( from CLI)
aws iam get-role --role-name lambda-execution-role-exp

## Create Lambda
aws lambda create-function \
  --function-name lambda-exp \
  --runtime python3.12 \
  --role arn:aws:iam::436204347274:role/lambda-execution-role-exp \
  --handler app.lambda_handler \
  --zip-file fileb://function.zip

## Check if its Delpoyed Correctly
aws lambda list-functions


## Create API Gateway Trigger ( inside the AWS Console)
### AWS Console → Lambda
### Open lambda-exp
### Click Add Trigger
### Select API Gateway
### Choose:
### Create a new API
### API Type: HTTP API
### Security: Open
### Click Add

### you will get a public HTTPS URL once you add API Gateway Trigger

## Test the API
curl " Paste URL Here "

## Cleanup
aws lambda delete-function --function-name lambda-exp

aws iam detach-role-policy \
  --role-name lambda-execution-role-exp \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

aws iam delete-role --role-name lambda-execution-role-exp

## API Gateway Cleanup
###  AWS Console → API Gateway → Your API → Delete


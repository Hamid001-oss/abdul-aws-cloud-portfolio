import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ.get("TABLE_NAME", "portfolio-app"))

def lambda_handler(event, context):
    """Handle an API Gateway request and return a serverless API response."""

    try:
        body = {
            "message": "Hello from my AWS Serverless Portfolio Application!",
            "service": "AWS Lambda",
            "status": "success"
        }

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(body)
        }

    except Exception as error:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Internal server error",
                "error": str(error)
            })
        }

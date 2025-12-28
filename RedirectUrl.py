import boto3
import os

TABLE_NAME = os.environ.get("TABLE_NAME")

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    path_params = event.get("pathParameters") or {}

    short_code = path_params.get("code")
    if not short_code:
        return {
            "statusCode": 400,
            "body": "Invalid request"
        }

    response = table.get_item(
        Key={"shortCode": short_code}
    )

    if "Item" not in response:
        return {
            "statusCode": 404,
            "body": "URL not found"
        }

    return {
        "statusCode": 302,
        "headers": {
            "Location": response["Item"]["longUrl"]
        },
        "body": ""
    }

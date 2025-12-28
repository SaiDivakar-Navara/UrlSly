import json
import boto3
import random
import string
import os

# Read table name from environment variable
TABLE_NAME = os.environ.get("TABLE_NAME")

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def lambda_handler(event, context):
    body = json.loads(event["body"])
    long_url = body["longUrl"]

    short_code = generate_short_code()

    table.put_item(
        Item={
            "shortCode": short_code,
            "longUrl": long_url
        }
    )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "shortUrl": f"<YOUR_SHORT_DOMAIN>/{short_code}"
        })
    }

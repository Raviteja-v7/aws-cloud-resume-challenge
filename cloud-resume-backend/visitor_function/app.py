import boto3
import os
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):
    # Update counter
    response = table.update_item(
        Key={"id": "site"},
        UpdateExpression="SET visits = if_not_exists(visits, :start) + :inc",
        ExpressionAttributeValues={":inc": 1, ":start": 0},
        ReturnValues="UPDATED_NEW"
    )
    
    count = int(response["Attributes"]["visits"])
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps({"count": count})
    }

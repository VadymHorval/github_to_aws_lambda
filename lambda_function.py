import json
import urllib3


def lambda_handler(event, context):

    http = urllib3.PoolManager()
    resp = http.request(
        "POST",
        "https://82js1wszcd.execute-api.eu-central-1.amazonaws.com/default/github_to_aws_lambda",
        fields={"body": "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"}  # Add custom form fields
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello World')
    }
    
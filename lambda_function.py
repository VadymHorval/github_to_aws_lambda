import json
import requests


def lambda_handler(event, context):
    r = requests.post('https://82js1wszcd.execute-api.eu-central-1.amazonaws.com/default/github_to_aws_lambda', data={'body': '!!!!!!!!!!!!!!!!!!!!!!!!!'})
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World')
    }
    
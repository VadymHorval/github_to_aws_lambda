import json

def lambda_handler(event, context):
    text = json.dumps(event, sort_keys=True, indent=3)
    print('Hello World!')
    #return 'Hello World!'
    return text
    
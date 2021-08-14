#import json
def lambda_handler(event, context):
    #text = json.dumps(event, sort_keys=True, indent=3)
    print('Hello World!')
    for i in range(10):
        print('iterator',i)
        yield i
    return 'Hello World!'
    
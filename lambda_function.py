import requests
import json
import collections
import time

def lambda_handler(event, context):
    # text = json.dumps(event, sort_keys=True, indent=3)
    # print('Hello World!')
    # #return 'Hello World!'
    # return text
    import time

    TABLE_ID = 'app3DEEwui4OTkeDI'
    API_KEY = 'keywRoiRn61Sk3nvo'
    TABLE_NAME = 'MainTable'

    table_url = f'https://api.airtable.com/v0/{TABLE_ID}/{TABLE_NAME}'
    HEADERS = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    r = requests.get(table_url, timeout=(1, 1), headers=HEADERS)  # get data from URLs file

    data = json.loads(r.content)  # convert data to dict

    d = collections.deque(maxlen=len(data['records']))  # create a ring buffer

    for i in data['records']:  # init buffer
        d.append(i['fields'].get('title'))
    try:
        while True:
            print(d[0], d[1], d[2])
            d.rotate(1)
            time.sleep(1)
    except KeyboardInterrupt:
        print('Caught KeyboardInterrupt')
        return 'Caught KeyboardInterrupt'

    
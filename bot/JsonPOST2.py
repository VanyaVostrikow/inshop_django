import requests
import json
def Post(sentname):
    url = 'http://127.0.0.1:8000/order/searchbot/'
    data = {'owner': sentname}
    json_data = json.dumps(data)
    resp = requests.post(url, json=data)
    return resp
Post("test")
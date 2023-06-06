import requests
import json
def PostCoupon(sentname):
    url = 'http://127.0.0.1:8000/coupon/searchbot/'
    data = {'owner': sentname}
    json_data = json.dumps(data)
    resp = requests.post(url, json=data)
    return resp


def PostOrder(sentname):
    url = 'http://127.0.0.1:8000/orders/searchbot/'
    data = {'owner': sentname}
    json_data = json.dumps(data)
    resp = requests.post(url, json=data)
    return resp

def PostCheck(sentname):
    url = 'http://127.0.0.1:8000/tg/check/'
    data = {'owner': sentname}
    json_data = json.dumps(data)
    resp = requests.post(url, json=data)
    return resp


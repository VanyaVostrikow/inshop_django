import json
from JSON import Create, Write, Read
import requests

def Get():
    resp = requests.get('http://127.0.0.1:8000/coupon/searchbot')
    print(resp.json())
    return resp



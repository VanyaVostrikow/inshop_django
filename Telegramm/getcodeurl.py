import requests
import json

def GetCode(url):
    resp = requests.get('url')
    print(resp.json())
    return resp
GetCode()
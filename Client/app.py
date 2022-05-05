import requests
import time
import json
import os

while True:
    time.sleep(5) 

    print(os.getlogin())
    param = {'user_name': os.getlogin()}
    json_param = json.dumps(param)
    print(json_param)

    request = requests.post('http://127.0.0.1:5000/client', json= json_param)
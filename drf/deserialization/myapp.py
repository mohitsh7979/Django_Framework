import requests
import json

URL="http://127.0.0.1:8000/mohit/"

data = {

    'name':'Mohit',
    'age':'19',
    'address':'jaipur'
}

json_data=json.dumps(data)

r=requests.post(url=URL , data=json_data)

data = r.json()

print(data)
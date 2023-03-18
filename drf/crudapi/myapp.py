import requests
import json

URL="http://127.0.0.1:8080/stu/"


# def getData(id = None):
#     data = {}
#     if id is not None:
#         data={'id':id}
#     json_data = json.dumps(data)
#     print(json_data)
#     r = requests.get(url = URL , data = json_data)
#     print(r)
#     data = r.json()
#     print(data)

# getData(1)
# getData(2)
# getData(3)
# getData()


def post_data():
    data = {
        'name':'Mohit Sharma',
        'roll':104,
        'address':'Jaipur'
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL , data = json_data)
    data = r.json()
    print(data)

post_data()
    

import requests
import json
from getpass import getpass

# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
# endpoint = 'http://localhost:8000/api/products/getlist'

password = getpass()
auth_endpoint = 'http://localhost:8000/api/auth/'
auth_response = requests.post(auth_endpoint, json={"username":'admin', 'password':password})
print(auth_response.json())



if auth_response.status_code == 200:
    token = auth_response.json()['token']
    endpoint = 'http://localhost:8000/api/products/'

    headers = {'Authorization': f"Bearer {token}"}

    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())



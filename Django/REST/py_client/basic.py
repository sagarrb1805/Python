import requests
import json

# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
endpoint = 'http://localhost:8000/api/'

get_response = requests.get(endpoint)

print(get_response.json())



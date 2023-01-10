import requests
import json

# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
# endpoint = 'http://localhost:8000/api/products/getlist'
endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': "product title",
    'price':32.99
}

get_response = requests.get(endpoint)

print(get_response.json())



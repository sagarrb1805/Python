import requests
import json

# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': "product title",
    'price':32.99,
    'content':"added content for product",
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())



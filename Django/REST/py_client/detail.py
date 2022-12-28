import requests
import json

# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
# endpoint = 'http://localhost:8000/api/products/1/update/'
# endpoint = 'http://localhost:8000/api/products/10/'
product_id = 1
endpoint = f"http://localhost:8000/api/products/{product_id}/"
# endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

data = {
    'title':"hello my friend",
    'price':129.99
}
# get_response = requests.delete(endpoint)
# print(get_response.status_code)

get_response = requests.get(endpoint)
# get_response = requests.put(endpoint, json=data)

print(get_response.json())



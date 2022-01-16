import requests
import json

response = requests.get("http://127.0.0.1:8000/user/0", headers={})
print("status_code:", response.status_code, type(response.status_code))
response_headers = response.headers
print("headers:", response_headers)
print("rate limit info:", response_headers['x-app-rate-limit'])
response_data = response.json()
print("return data:", response_data)
print("short description:", response_data["short_description"])

sample_data_to_send = {
  "name": "bob",
  "liked_posts": [
    0, 1, 2
  ],
  "short_description": "some short description",
  "long_bio": "some long bio"
}
json_data = json.dumps(sample_data_to_send)
# print("json data:", json_data, type(json_data))
# print("original data:", sample_data_to_send, type(sample_data_to_send))
post_response = requests.post("http://127.0.0.1:8000/user/", headers={}, json=sample_data_to_send) #  , data=json_data)
print("post request response:", post_response.json())
print("post status response:", post_response.status_code)
print("post response headers:", post_response.headers)


requests.delete()

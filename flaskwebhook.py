import requests
import json

url = "http://127.0.0.1:5000/webhook"

data = {"name": "john",
        "age": "18",
        "message": "This is a test"}

r = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
print("Status Code:", r.status_code)
print("Response:", r.text)
import requests
import json

url = "http://127.0.0.1:5000/webhook"

print("Welcome to the message simulation! \nPlease Enter Your Details:")

name = input("Name: ")
phoneNumber = input("Phone (+44): ")

print(f"Successfully setup your account. \nWelcome {name}!")
message = input("Message: ")

while len(message) > 100:
    message = input("Too Long! Please Try Again: ")



data = {"name": name,
        "phone": phoneNumber,
        "message": message}

r = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
print("Status Code:", r.status_code)
print("Response:", r.text)
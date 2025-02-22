import requests

url = "http://127.0.0.1:8000/api/login/"
data = {"username": "joshadmin", "password": "ajani0830"}

response = requests.post(url, json=data)
print(response.json())

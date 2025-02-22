import requests

url = "http://127.0.0.1:8000/api/protected-endpoint/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwMTc5MDUwLCJpYXQiOjE3NDAxNzg3NTAsImp0aSI6IjI1ZmJjNjNhMzQzOTQxNDlhN2UzYTQyYjcyNTdlMmE5IiwidXNlcl9pZCI6MX0.qr24ScmuqGcAqeh7es6ZLXDHrPXdKsNnTUveP7CEjAE"
}

response = requests.get(url, headers=headers)
print(response.json())

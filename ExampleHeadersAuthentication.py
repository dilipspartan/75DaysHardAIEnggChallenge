# Working with Headers and Authentication

import requests

# API Key authentication
headers = {
    'Authorization': 'Bearer your-api-key-here',
    'Content-Type': 'application/json'
}

response = requests.get(
    'https://api.example.com/data',
    headers=headers
)

# Basic authentication
response = requests.get(
    'https://api.example.com/data',
    auth=('username', 'password')
)

# Custom headers
headers = {
    'X-API-Key': 'your-key',
    'X-User-ID': 'himanshu'
}

response = requests.get(
    'https://api.example.com/data',
    headers=headers
)
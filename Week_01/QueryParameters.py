# Query Parameters


import requests

params = {
    'q': 'AI engineering',
    'category': 'machine-learning',
    'author': 'Himanshu',
    'limit': 10
}

response = requests.get(
    'https://api.example.com/posts',
    params=params
)

# This creates the URL:# https://api.example.com/posts?q=AI+engineering&category=machine-learning&author=Himanshu&limit=10
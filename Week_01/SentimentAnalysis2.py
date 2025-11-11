import requests

response = requests.post(
    'http://localhost:5000/analyze',
    json={'text': 'The 75 Hard AI Engineering Challenge is incredible!'}
)

print(response.json())
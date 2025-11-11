import requests

# Make a GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/19')

if response.status_code == 200:
    data = response.json()
    print(data['title'])
    print(response.status_code)
else:
    print(f"Error: {response.status_code}")
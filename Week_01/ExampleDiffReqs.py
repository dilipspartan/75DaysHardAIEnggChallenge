# Making Different Types of Requests

import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

new_post = {
    'title': '75 Hard AI Engineering Challenge',
    'body': 'Building AI systems for 75 days straight',
    'userId': 1
}
response = requests.post(f'{BASE_URL}/posts', json=new_post)
print(f"Created post: {response.json()}")

response = requests.get(f'{BASE_URL}/posts/1')
post = response.json()
print(f"Retrieved post: {post['title']}")

updated_post = {
    'title': 'Updated: 75 Hard AI Engineering Challenge',
    'body': 'Day 4 of building AI systems',
    'userId': 1
}
response = requests.put(f'{BASE_URL}/posts/1', json=updated_post)
print(f"Updated post: {response.json()}")

response = requests.delete(f'{BASE_URL}/posts/1')
print(f"Delete status code: {response.status_code}")
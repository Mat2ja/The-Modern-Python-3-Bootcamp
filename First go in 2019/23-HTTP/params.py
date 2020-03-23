
import requests

# https://icanhazdadjoke.com/api

url = "https://icanhazdadjoke.com/search"  # page with all the jokes

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 3}
)

data = response.json()
print(data["results"])

result = data['results']
print(result[1]['joke'])

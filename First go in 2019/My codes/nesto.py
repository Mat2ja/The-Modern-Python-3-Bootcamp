import requests
 
def jokes():
    url = input("Entre com  a URL: ")
    response = requests.get(url, headers={"Accept": "text/plain"})
    print(response.text)
 
jokes()
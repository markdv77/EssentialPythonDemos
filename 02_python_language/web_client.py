import requests

response = requests.get('http://google.com')
print(len(response.text))
print(response.text)

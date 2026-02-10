import requests


response = requests.get('https://www.example.com')

print(response.status_code)  # prints the HTTP status code (200 for success)
print(response.text)  # prints the response body as text
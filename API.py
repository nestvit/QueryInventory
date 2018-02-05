import requests

url = "https://api.icndb.com/jokes/random"

headers = {
    'accept': "application/json",
    'cache-control': "no-cache",
    'postman-token': "e7323aad-4342-6d60-fa07-ccbae8649054"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
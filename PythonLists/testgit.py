import requests

r = requests.get("https://github.com")
print(r.status_code)
print(r.headers)
print("Hey there added a new line")
print("adding 2nd line")
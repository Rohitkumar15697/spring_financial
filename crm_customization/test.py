import requests
import json

data = {'name': 'Test', 'phone': '204 556 6565', 'email': 'test@gmail.com', 'street':'125 Milross Ave', 'city': 'Vancouver', 'zip': '7VG XG8', 'state': 'BC', 'country': 'Canada'}
headers = {"Content-Type": "application/json"}
res = requests.post("http://localhost:8017/contact/create", headers=headers, data=json.dumps(data))
print(res)
print(res.text)
print(res.json())

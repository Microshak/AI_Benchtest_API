import requests
res = requests.post('http://localhost/device', json={"name":"lalala"})
if res.ok:
    print (res.json())

res = requests.post('http://localhost/device', json={"name":"lalala"})
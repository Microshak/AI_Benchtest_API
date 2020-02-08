import requests
res = requests.post('https://ai-benchtest.azurewebsites.net/device', json={"name":"lalala"})
if res.ok:
    print (res.json())


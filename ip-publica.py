import requests
ip = requests.get('http://checkip.amazonaws.com').text.strip()
print(ip)

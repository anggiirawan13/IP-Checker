import socket
import requests
import pprint
import json

hostname = input('Enter a domain name: ')
ipAddress = socket.gethostbyname(hostname)

reqURL ='https://geolocation-db.com/jsonp/' + ipAddress
resp = requests.get(reqURL)
geolocation = resp.content.decode()
geolocation = geolocation.split('(')[1].strip(')')
geolocation = json.loads(geolocation)

print(f'Domain Name: {hostname}')
print(f'IP Address: {ipAddress}')

for k, v in geolocation.items():
    pprint.pprint(str(k) + ' : ' + str(v))
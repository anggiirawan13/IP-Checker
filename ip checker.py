import socket

hostname = input('Enter a domain name: ')
ipAddress = socket.gethostbyname(hostname)

print(f'Domain Name: {hostname}')
print(f'Ip Address: {ipAddress}')
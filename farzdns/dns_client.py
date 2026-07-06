import socket

from config import HOST, PORT, BUFFER_SIZE
from protocol import FNP

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

domain = input("Enter domain: ")

request = FNP.build_request(
    "DNS_QUERY",
    domain
)

client.send(request.encode())

response = client.recv(BUFFER_SIZE).decode()

print("\nRAW RESPONSE")
print("----------------")
print(response)

parsed = FNP.parse(response)

print("\nPARSED RESPONSE")
print("----------------")
print(parsed)
print("==============================")

client.close()
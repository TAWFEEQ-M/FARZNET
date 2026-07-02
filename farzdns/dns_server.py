import socket

from config import HOST, PORT, BUFFER_SIZE, VERSION
from database import DNSDatabase
from logger import Logger

db = DNSDatabase()
logger = Logger()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("=" * 50)
print(VERSION)
print("=" * 50)
print(f"Listening on {HOST}:{PORT}")

logger.log("FarzDNS Server Started")

while True:

    client, address = server.accept()

    logger.log(f"Client Connected : {address}")

    domain = client.recv(BUFFER_SIZE).decode()

    logger.log(f"Requested : {domain}")

    reply = db.get_ip(domain)

    logger.log(f"Reply : {reply}")

    client.send(reply.encode())

    client.close()
import socket

dns_database = {
    "chat.farz": "192.168.1.2",
    "server.farz": "192.168.1.3",
    "camera.farz": "192.168.1.4",
    "home.farz": "192.168.1.5"
}

HOST = "127.0.0.1"
PORT = 5353

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("====================================")
print("      FARZNET DNS SERVER v0.2")
print("====================================")
print(f"Listening on {HOST}:{PORT}")

while True:
    client, address = server.accept()
    print(f"\nConnection from {address}")

    domain = client.recv(1024).decode().lower()

    print(f"Requested: {domain}")

    if domain in dns_database:
        reply = dns_database[domain]
    else:
        reply = "NOT FOUND"

    client.send(reply.encode())

    client.close()
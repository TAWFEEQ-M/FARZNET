import socket

from config import HOST, PORT, BUFFER_SIZE
from router import Router
from http_request import HTTPRequest

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(5)

print("=" * 50)
print("FarzServer v3.0")
print("=" * 50)
print(f"Listening on http://{HOST}:{PORT}")

while True:

    client, address = server.accept()

    print(f"\nClient Connected: {address}")

    raw_request = client.recv(BUFFER_SIZE).decode(errors="ignore")

    request = HTTPRequest(raw_request)

    print("Path:", request.path)

    status, content_type, body = Router.get_page(request.path)

    # --- Build HTTP response headers ---
    headers = (
        f"HTTP/1.1 {status}\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Connection: close\r\n"
        "\r\n"
    ).encode()

    # --- Ensure body is bytes ---
    if isinstance(body, str):
        body = body.encode("utf-8")

    response = headers + body

    client.send(response)

    client.close()
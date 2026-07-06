import socket
from farzdns.resolver import FarzDNS

BUFFER_SIZE = 4096

print("=== FARZ BROWSER ===")

while True:

    domain = input("\nEnter FARZ domain (e.g. home.farz): ")

    # Step 1: DNS resolution
    route = FarzDNS.resolve(domain)

    if not route:
        print("❌ Domain not found")
        continue

    print("DNS →", route)

    try:
        # Split DNS result
        host_port, path = route.split("/", 1)
        host, port = host_port.split(":")
        port = int(port)

        # Step 2: connect to server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        # Step 3: send HTTP request
        request = f"GET /{path} HTTP/1.1\r\nHost: {domain}\r\n\r\n"
        client.send(request.encode())

        # Step 4: receive response
        response = client.recv(BUFFER_SIZE).decode(errors="ignore")

        client.close()

        # ===== HTTP PARSER =====
        parts = response.split("\r\n\r\n", 1)

        header_part = parts[0]
        body_part = parts[1] if len(parts) > 1 else ""

        lines = header_part.split("\r\n")
        status_line = lines[0]
        headers = lines[1:]

        # ===== OUTPUT =====
        print("\n========== FARZ BROWSER ==========\n")

        print("STATUS:", status_line)

        print("\nHEADERS:")
        for h in headers:
            print(" ", h)

        print("\nBODY (preview):\n")
        print(body_part[:300])

        print("\n==================================\n")

    except Exception as e:
        print("Error:", e)
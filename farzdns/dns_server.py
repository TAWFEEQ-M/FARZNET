import socket
import threading

from config import HOST, PORT, BUFFER_SIZE, VERSION
from database import DNSDatabase
from logger import Logger
from protocol import FNP

# Initialize database and logger
db = DNSDatabase()
logger = Logger()


def handle_client(client, address):
    """Handle a single client connection."""

    logger.log(f"Client Connected: {address}")

    try:
        # Receive request
        message = client.recv(BUFFER_SIZE).decode()

        print("\n========== RAW REQUEST ==========")
        print(message)
        print("=================================\n")

        # Parse request
        data = FNP.parse(message)

        print("Parsed Data:", data)

        request_type = data.get("TYPE")
        domain = data.get("DATA")

        logger.log(f"Request Type: {request_type}")
        logger.log(f"Requested Domain: {domain}")

        # Validate request
        if request_type != "DNS_QUERY":
            response = FNP.build_response(
                "ERROR",
                "Invalid Request Type"
            )

        elif not domain:
            response = FNP.build_response(
                "ERROR",
                "No Domain Supplied"
            )

        else:
            # Lookup domain
            reply = db.get_ip(domain)

            logger.log(f"Reply: {reply}")

            if reply == "NOT FOUND":
                response = FNP.build_response(
                    "NOT_FOUND",
                    reply
                )
            else:
                response = FNP.build_response(
                    "OK",
                    reply
                )

        print("\n========== RESPONSE ==========")
        print(response)
        print("==============================\n")

        client.send(response.encode())

    except Exception as error:
        logger.log(f"ERROR: {error}")
        print(error)

    finally:
        client.close()
        logger.log(f"Client Disconnected: {address}")


# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow immediate restart
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind and listen
server.bind((HOST, PORT))
server.listen(5)

print("=" * 50)
print(VERSION)
print("=" * 50)
print(f"Server Listening on {HOST}:{PORT}")
print("=" * 50)

logger.log("FarzDNS Server Started")

# Main server loop
while True:
    client, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client, address),
        daemon=True
    )

    thread.start()
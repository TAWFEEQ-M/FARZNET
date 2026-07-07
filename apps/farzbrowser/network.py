import socket
import sys
import os

# Add FARZNET root path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from farzdns.protocol import FNP


BUFFER_SIZE = 4096

# Your PC IP where FarzDNS is running
DNS_HOST = "192.168.1.6"
DNS_PORT = 8053


class Network:

    @staticmethod
    def resolve(domain):

        try:
            # Connect to FarzDNS server
            client = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            client.connect(
                (DNS_HOST, DNS_PORT)
            )

            # Build DNS request
            request = FNP.build_request(
                "DNS_QUERY",
                domain
            )

            client.send(
                request.encode()
            )

            # Receive DNS response
            response = client.recv(
                BUFFER_SIZE
            ).decode()

            client.close()


            # Parse response
            data = FNP.parse(response)


            if data.get("STATUS") == "OK":
                return data.get("DATA")


            return None


        except Exception as error:

            print("DNS ERROR:", error)

            return None



    @staticmethod
    def fetch(domain):

        # Ask FarzDNS for address
        route = Network.resolve(domain)


        if not route:
            return "<h1>Domain Not Found</h1>"


        # Remove http://
        url = route.replace(
            "http://",
            ""
        )


        host_port, path = url.split(
            "/",
            1
        )


        host, port = host_port.split(
            ":"
        )


        port = int(port)



        try:

            # Connect to FarzServer
            client = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )


            client.connect(
                (host, port)
            )


            # HTTP request
            request = (
                f"GET /{path} HTTP/1.1\r\n"
                f"Host: {domain}\r\n"
                "Connection: close\r\n"
                "\r\n"
            )


            client.send(
                request.encode()
            )


            response = b""


            while True:

                data = client.recv(
                    BUFFER_SIZE
                )

                if not data:
                    break

                response += data


            client.close()


            response = response.decode(
                errors="ignore"
            )


            parts = response.split(
                "\r\n\r\n",
                1
            )


            if len(parts) == 2:

                return parts[1]


            return "<h1>Invalid HTTP Response</h1>"


        except Exception as error:

            print("SERVER ERROR:", error)

            return "<h1>Server Connection Failed</h1>"
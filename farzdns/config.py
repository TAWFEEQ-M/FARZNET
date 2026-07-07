import os

HOST = "0.0.0.0"
PORT = 8053

BUFFER_SIZE = 1024

VERSION = "FarzDNS v1.0"

LOG_FILE = os.path.join(
    os.path.dirname(__file__),
    "logs",
    "dns.log"
)

DATABASE_FILE = os.path.join(
    os.path.dirname(__file__),
    "dns_records.json"
)
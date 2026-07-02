print("===================================")
print("       FARZNET DNS v0.1")
print("===================================")

dns_database = {
    "chat.farz": "192.168.1.2",
    "server.farz": "192.168.1.3",
    "camera.farz": "192.168.1.4",
    "home.farz": "192.168.1.5"
}

while True:
    domain = input("\nEnter domain name (or type exit): ").lower()

    if domain == "exit":
        print("Shutting down FarzDNS...")
        break

    if domain in dns_database:
        print(f"IP Address : {dns_database[domain]}")
    else:
        print("Domain not found.")
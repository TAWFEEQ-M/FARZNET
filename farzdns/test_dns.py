from resolver import FarzDNS

domain = input("Enter domain (example home.farz): ")

result = FarzDNS.resolve(domain)

print("Resolved:", result)
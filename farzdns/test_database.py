from database import DNSDatabase

db = DNSDatabase()

print(db.get_ip("chat.farz"))
print(db.get_ip("camera.farz"))
print(db.get_ip("google.com"))
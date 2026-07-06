from protocol import FNP

request = FNP.build_request(
    "DNS_QUERY",
    "chat.farz"
)

print("REQUEST")
print("----------------")
print(request)

print()

parsed = FNP.parse(request)

print("PARSED")
print("----------------")
print(parsed)

print()

response = FNP.build_response(
    "OK",
    "192.168.1.2"
)

print("RESPONSE")
print("----------------")
print(response)
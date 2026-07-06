from farzdns.dns_records import DNS_MAP

class FarzDNS:

    @staticmethod
    def resolve(domain):

        return DNS_MAP.get(domain, None)
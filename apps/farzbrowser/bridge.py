import sys
import os

from network import Network


class Bridge:

    def resolve_domain(self, domain):

        result = Network.resolve(domain)

        if result:
            return result

        return "NOT FOUND"
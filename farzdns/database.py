import json
from config import DATABASE_FILE


class DNSDatabase:

    def __init__(self):
        self.records = {}
        self.load()

    def load(self):
        try:
            with open(DATABASE_FILE, "r") as file:
                self.records = json.load(file)
            print("[DATABASE] Records loaded successfully.")
        except FileNotFoundError:
            print("[DATABASE] Database file not found.")
            self.records = {}

    def get_ip(self, domain):
        return self.records.get(domain.lower(), "NOT FOUND")
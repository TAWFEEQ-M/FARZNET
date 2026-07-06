class HTTPRequest:

    def __init__(self, raw_request):

        self.raw = raw_request

        self.method = ""

        self.path = ""

        self.version = ""

        self.headers = {}

        self.parse()

    def parse(self):

        lines = self.raw.split("\r\n")

        if len(lines) == 0:
            return

        first = lines[0].split()

        if len(first) == 3:

            self.method = first[0]

            self.path = first[1]

            self.version = first[2]

        for line in lines[1:]:

            if ":" in line:

                key, value = line.split(":", 1)

                self.headers[key.strip()] = value.strip()
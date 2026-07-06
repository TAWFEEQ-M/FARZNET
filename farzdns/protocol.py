class FNP:

    VERSION = "FNP/1.0"

    @staticmethod
    def build_request(request_type, data):

        return (
            f"{FNP.VERSION}\n"
            f"TYPE:{request_type}\n"
            f"DATA:{data}"
        )

    @staticmethod
    def build_response(status, data):

        return (
            f"{FNP.VERSION}\n"
            f"STATUS:{status}\n"
            f"DATA:{data}"
        )

    @staticmethod
    def parse(message):

        lines = message.strip().split("\n")

        result = {}

        for line in lines[1:]:

            if ":" in line:

                key, value = line.split(":", 1)

                result[key] = value

        return result
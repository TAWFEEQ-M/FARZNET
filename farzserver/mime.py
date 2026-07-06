class MIME:

    TYPES = {
        ".html": "text/html",
        ".css": "text/css",
        ".js": "application/javascript",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".ico": "image/x-icon",
        ".txt": "text/plain"
    }

    @staticmethod
    def get(extension):

        return MIME.TYPES.get(
            extension.lower(),
            "application/octet-stream"
        )
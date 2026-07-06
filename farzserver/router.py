import os

from config import WEBSITE_FOLDER
from static_files import StaticFiles


class Router:

    @staticmethod
    def get_page(route):

        # Static files (CSS, JS, Images, etc.)
        if "." in route:

            result = StaticFiles.load(route)

            if result:

                mime, data = result

                return (
                    "200 OK",
                    mime,
                    data
                )

            return (
                "404 Not Found",
                "text/plain",
                b"File Not Found"
            )

        # Default route
        if route == "/":
            route = "/home"

        route = route.strip("/")

        file_path = os.path.join(
            WEBSITE_FOLDER,
            route,
            "index.html"
        )

        if os.path.exists(file_path):

            with open(file_path, "r", encoding="utf-8") as file:
                html = file.read()

            return (
                "200 OK",
                "text/html",
                html
            )

        html = """
<!DOCTYPE html>
<html>
<head>
<title>404</title>
</head>
<body>

<h1>404 - Page Not Found</h1>

<p>The page you requested does not exist.</p>

</body>
</html>
"""

        return (
            "404 Not Found",
            "text/html",
            html
        )
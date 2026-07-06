import os

from mime import MIME
from config import WEBSITE_FOLDER


class StaticFiles:

    @staticmethod
    def load(path):

        file_path = os.path.join(
            WEBSITE_FOLDER,
            path.strip("/")
        )

        if not os.path.exists(file_path):
            return None

        extension = os.path.splitext(file_path)[1]

        mime = MIME.get(extension)

        with open(file_path, "rb") as file:
            data = file.read()

        return (
            mime,
            data
        )
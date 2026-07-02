from datetime import datetime
from config import LOG_FILE


class Logger:

    def log(self, message):

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a") as file:
            file.write(f"[{current_time}] {message}\n")

        print(f"[LOG] {message}")
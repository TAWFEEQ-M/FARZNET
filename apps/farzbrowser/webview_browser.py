import webview


class FarzBrowser:

    def __init__(self):

        self.window = webview.create_window(
            "FarzBrowser v2.0",
            "http://127.0.0.1:8080/home",
            width=1200,
            height=800
        )


if __name__ == "__main__":

    browser = FarzBrowser()

    webview.start()
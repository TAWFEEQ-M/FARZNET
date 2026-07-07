import webview
import os

from bridge import Bridge


path = os.path.abspath("apps/farzbrowser/ui.html")


window = webview.create_window(
    "FarzBrowser",
    path,
    width=1000,
    height=700,
    js_api=Bridge()
)

webview.start()
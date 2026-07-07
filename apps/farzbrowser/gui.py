import tkinter as tk
from tkhtmlview import HTMLLabel


class BrowserGUI:

    def __init__(self):

        # Create main window
        self.window = tk.Tk()
        self.window.title("FarzBrowser v1.0")
        self.window.geometry("1000x700")

        # ---------- Top Bar ----------
        top_frame = tk.Frame(self.window)
        top_frame.pack(fill="x", padx=10, pady=10)

        # Address bar
        self.address = tk.Entry(
            top_frame,
            font=("Arial", 14)
        )

        self.address.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        # Default address
        self.address.insert(0, "home.farz")

        # Go button
        self.go = tk.Button(
            top_frame,
            text="Go",
            width=10,
            font=("Arial", 11, "bold")
        )

        self.go.pack(side="right")

        # ---------- HTML Display ----------
        self.output = HTMLLabel(
            self.window,
            html="""
            <h1 style="color:blue;">Welcome to FarzBrowser</h1>

            <p>
            This is the first graphical version of your own browser.
            </p>

            <hr>

            <h3>Current Features</h3>

            <ul>
                <li>FarzDNS ✔</li>
                <li>FarzServer ✔</li>
                <li>HTTP Parser ✔</li>
                <li>GUI Browser ✔</li>
            </ul>
            """
        )

        self.output.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def load_html(self, html):
        """
        Replace the displayed HTML.
        """
        self.output.set_html(html)

    def run(self):
        self.window.mainloop()
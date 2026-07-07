from .network import Network


class BrowserController:

    def __init__(self, gui):
        self.gui = gui

        self.history = []
        self.current_index = -1

    def navigate(self):

        domain = self.gui.address.get().strip()

        if not domain:
            return

        html = Network.fetch(domain)

        self.gui.load_html(html)

        # Save history
        if self.current_index < len(self.history) - 1:
            self.history = self.history[: self.current_index + 1]

        self.history.append(domain)
        self.current_index += 1

    def back(self):

        if self.current_index <= 0:
            return

        self.current_index -= 1

        domain = self.history[self.current_index]

        self.gui.address.delete(0, "end")
        self.gui.address.insert(0, domain)

        html = Network.fetch(domain)

        self.gui.load_html(html)

    def forward(self):

        if self.current_index >= len(self.history) - 1:
            return

        self.current_index += 1

        domain = self.history[self.current_index]

        self.gui.address.delete(0, "end")
        self.gui.address.insert(0, domain)

        html = Network.fetch(domain)

        self.gui.load_html(html)
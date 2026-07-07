from .gui import BrowserGUI
from .controller import BrowserController

browser = BrowserGUI()

controller = BrowserController(browser)

browser.go.config(command=controller.navigate)

browser.run()
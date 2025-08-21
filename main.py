from views import BaseWindow
from util import DatabaseConnector

DatabaseConnector.configure()
window = BaseWindow(width=1600, height=900)
window.run()

from views import BaseWindow
from util import DatabaseConnector, Config

Config.set_info()
DatabaseConnector.configure()
window = BaseWindow(width=1600, height=900)
window.run()

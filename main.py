from views import BaseWindow
from util import create_tables

create_tables()
window = BaseWindow(width=1200, height=900)
window.run()

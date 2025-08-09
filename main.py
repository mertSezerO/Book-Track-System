from views import BaseWindow
from util import create_tables

create_tables()
window = BaseWindow(width=1000, height=800)
window.run()

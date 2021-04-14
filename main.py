import sys
from PyQt5.QtWidgets import QApplication

from utils.window import Window
from utils.CNN import CNN_Model

# create variables for running window
app = QApplication(sys.argv)
w = Window()

# display window
w.show()
sys.exit(app.exec_())

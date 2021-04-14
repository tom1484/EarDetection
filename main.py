import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from utils.startup_window import startupWindow
from utils.choose_window import chooseWindow
from utils.main_window import mainWindow

from utils.CNN import CNN_Model

# create variables for running window
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(3300)
widget.setFixedHeight(1900)

startup = startupWindow(widget)
# choose = chooseWindow(widget)
main = mainWindow(widget)

widget.addWidget(startup)
# widget.addWidget(choose)
widget.addWidget(main)

widget.show()

try:
    sys.exit(app.exec_())
except:
    pass

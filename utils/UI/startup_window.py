from PyQt5.QtWidgets import QDialog

from utils.UI.startup_ui import Ui_Form


class startupWindow(QDialog):
    def __init__(self, widget):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.widget = widget

        self.ui.login_button.clicked.connect(self.login)

    def login(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

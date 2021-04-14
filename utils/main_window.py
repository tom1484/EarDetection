from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QTimer, QStringListModel

from utils.main_ui import Ui_Form

from utils.recognizer import Recognizer
from utils.camera import Camera
from utils.database import Database
from utils.updater import Updater


class mainWindow(QDialog):
    def __init__(self, widget):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.widget = widget

        # set records_holder
        sl_model = QStringListModel()
        self.ui.records_holder.setModel(sl_model)

        # set ear detector
        self.camera = Camera(4, self.ui.camera_holder.width(), self.ui.camera_holder.height())
        self.recognizer = Recognizer()

        # set update timer
        self.fps = 60
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 // self.fps)

        # set updater
        self.updater = Updater(self.ui,
                               Database(host='localhost', database='eardoor',
                                        user='eardoor', password='14841484', table='records'),
                               sl_model)

    def update(self):
        # get captured frame
        frame = self.camera.capture()
        if frame is None:
            return
        # run detection
        name, frame = self.recognizer.detect(frame)

        # update application
        self.updater.update(name, frame)

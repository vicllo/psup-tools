from QtObjects import *
from PySide6 import QtWidgets
from dataclasses import *
from QtObjects.waitingplotwidget import *
from QtObjects.mainpage import *
from PySide6 import QtCore


class MainWindow(QtWidgets.QMainWindow):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMainWindow.html#qt-main-window-framework
    def __init__(self, session, x0, y0, width, height, parent=None):
        """
        Defines the main window of the game
        :param session: the parcoursup session
        :param x0: initial position on screen
        :param y0: initial position on screen
        :param width: int
        :param height: int
        :param parent: parent
        """
        super(MainWindow, self).__init__(parent)
        self.setGeometry(x0, y0, width, height)
        self.setWindowTitle("Psup-Tools")
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #https://living-sun.com/fr/python/718714-how-do-i-create-a-custom-window-title-bar-using-pyqt4-python-css-user-interface-pyqt4.html

        self.currentCentralWidget = MainPage(session, width, height)
        self.setCentralWidget(self.currentCentralWidget)

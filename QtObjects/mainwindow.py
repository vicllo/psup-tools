from QtObjects import *
from PySide6 import QtWidgets
from dataclasses import *
from QtObjects.waitingplotwidget import *
from QtObjects.mainpage import *


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

        course = session.courses["St Louis"]
        #self.currentCentralWidget = WelcomePage(width, height, self)
        #self.currentCentralWidget = waiting_plot(course)
        self.currentCentralWidget = MainPage(session, width, height)
        self.setCentralWidget(self.currentCentralWidget)

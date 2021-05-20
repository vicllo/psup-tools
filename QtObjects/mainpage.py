from PySide6 import QtWidgets, QtGui
from QtObjects.waitingplotwidget import waiting_plot
from QtObjects.mainpagemenu import MenuWidget
from QtObjects import *


class MainPage(QtWidgets.QSplitter):

    def __init__(self, session, width, height, parent=None):
        """
        Defines the welcome page of the game
        :param width: int
        :param height: int
        :param parent:
        """
        super(MainPage, self).__init__(parent)
        self.width = width
        self.height = height
        self.parent = parent
        self.setFixedSize(width, height)

        self.menu = MenuWidget(parent=self)
        self.plot = waiting_plot(session.courses["St Louis"])
        self.addWidget(self.menu)
        self.addWidget(self.plot)

    def go_home(self):
        print("Go home !")
        self.plot.hide()

    def display_all_courses(self):
        print("Show all courses")
        self.plot.show()


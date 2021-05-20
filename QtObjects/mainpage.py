from PySide6 import QtWidgets, QtGui
from QtObjects.waitingplotwidget import waiting_plot

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

        self.addWidget(waiting_plot(session.courses["St Louis"]))


from PySide6 import QtWidgets, QtGui

from QtObjects import *


class MainPage(QtWidgets.QWidget):

    def __init__(self, width, height, parent=None):
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


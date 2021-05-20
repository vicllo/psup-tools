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
        self.session = session
        self.width = width
        self.height = height
        self.parent = parent
        self.setFixedSize(width, height)

        self.menu = MenuWidget(session, parent=self)
        self.plot = waiting_plot([session.courses["St Louis"]], self)
        self.addWidget(self.menu)
        self.addWidget(self.plot)

    def go_home(self):
        self.plot.hide()

    def display_all_courses(self):
        self.plot.hide()
        self.plot = waiting_plot(self.session.courses.values(), self)
        self.plot.show()

    def display_course(self):
        source = self.sender()
        self.plot.hide()
        self.plot = waiting_plot([self.session.courses[source.course_name]], self)
        self.plot.show()


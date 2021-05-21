from PySide6 import QtWidgets, QtGui
from QtObjects.waitingplotwidget import waiting_plot
from QtObjects.mainpagemenu import MenuWidget
from QtObjects.global_overview_widget import GlobalOverview
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
        self.plot = waiting_plot([session.courses["St Louis MPSI"]], self)
        self.global_overview = GlobalOverview(session, self)

        self.pannels = [self.plot, self.global_overview]

        self.plot.hide()


    def hide_all_pannels(self):
        for pannel in self.pannels:
            pannel.hide()


    def go_home(self):
        self.hide_all_pannels()
        self.global_overview.show()

    def add_event(self):
        self.hide_all_pannels()


    def display_all_courses(self):
        self.hide_all_pannels()

        self.plot = waiting_plot(self.session.courses.values(), self)
        self.plot.show()

    def display_course(self):
        self.hide_all_pannels()

        source = self.sender()
        self.plot = waiting_plot([self.session.courses[source.course_name]], self)
        self.plot.show()


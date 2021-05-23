from PySide6 import QtWidgets, QtGui
from QtObjects.customstylewidget import *

class MenuWidget(QtWidgets.QWidget):

    def __init__(self, session, parent):
        """
        Defines the menu widget of the game
        :param parent:
        """
        super(MenuWidget, self).__init__(parent)

        home_button = CustomQPushBox(text="Home", icon=QtGui.QIcon("house.png"), parent=self)
        home_button.clicked.connect(parent.go_home)

        add_course_button = CustomQPushBox(text="Add course", parent=self)
        add_course_button.move(0, home_button.height())
        add_course_button.clicked.connect(parent.add_course)

        add_event_button = CustomQPushBox(text="Add event", parent=self)
        add_event_button.move(0, add_course_button.y()+add_course_button.height())
        add_event_button.clicked.connect(parent.add_event)

        all_courses_button = CustomQPushBox(text="All courses", parent=self)
        all_courses_button.move(0, add_event_button.y()+add_event_button.height())
        all_courses_button.clicked.connect(parent.display_all_courses)

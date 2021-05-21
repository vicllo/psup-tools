from PySide6 import QtWidgets, QtGui


class MenuWidget(QtWidgets.QWidget):

    def __init__(self, session, parent):
        """
        Defines the menu widget of the game
        :param parent:
        """
        super(MenuWidget, self).__init__(parent)

        home_button = QtWidgets.QPushButton(text="Home", icon=QtGui.QIcon("house.png"), parent=self)
        home_button.clicked.connect(parent.go_home)

        add_event_button = QtWidgets.QPushButton(text="Add event", parent=self)
        add_event_button.move(0,40)
        add_event_button.clicked.connect(parent.add_event)

        all_courses_button = QtWidgets.QPushButton(text="All courses", parent=self)
        all_courses_button.move(0, 20)
        all_courses_button.clicked.connect(parent.display_all_courses)

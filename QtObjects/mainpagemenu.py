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

        courses_buttons = []
        i = 1
        for course in session.courses:
            new_course_button = QtWidgets.QPushButton(text=course, parent=self)
            new_course_button.move(0, 20*i)
            new_course_button.course_name = course
            i += 1
            new_course_button.clicked.connect(parent.display_course)
            courses_buttons.append(new_course_button)

        all_courses_button = QtWidgets.QPushButton(text="Courses", parent=self)
        all_courses_button.move(0, 80)
        all_courses_button.clicked.connect(parent.display_all_courses)

from PySide6 import QtWidgets, QtGui


class CourseTile(QtWidgets.QAbstractButton):
    def __init__(self, course, parent):
        super(CourseTile, self).__init__(parent)

        if course.last_event:
            event_shown = course.last_event.kind
        else:
            event_shown = ""

        test_button = QtWidgets.QPushButton(course)
        self.clicked.connect(parent.display_course)

class GlobalOverview(QtWidgets.QWidget):

    def __init__(self, session, parent):
        """
        Defines the menu widget of the game
        :param parent:
        """
        super(GlobalOverview, self).__init__(parent)

        #test_button = QtWidgets.QPushButton("Hey", self)

        top_to_bottom = QtWidgets.QBoxLayout.TopToBottom
        left_to_right = QtWidgets.QBoxLayout.LeftToRight

        vertical_layout = QtWidgets.QBoxLayout(top_to_bottom, parent=self)

        courses_list = [session.courses.values()]

        for line_index in range(len(session.courses)//3 + 1):
            horizontal_layout = QtWidgets.QBoxLayout(left_to_right, parent=self)

            for column_index in range(len(list(session.courses)[3*line_index:3*line_index+3])):
                course_name = list(session.courses)[3*line_index+column_index]
                course = session.courses[course_name]
                if course.last_event:
                    event_shown = course.last_event.kind
                else:
                    event_shown = ""
                new_button = QtWidgets.QPushButton(
                    text=course_name+"\n"+event_shown,
                    parent=self)
                new_button.course_name = course_name

                new_button.clicked.connect(parent.display_course)

                horizontal_layout.addWidget(new_button)


            vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addStretch()

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from dataclasses import *
from constants import *


class AddCourse(QWidget):
    def __init__(self, session, parent):
        super(AddCourse, self).__init__(parent)

        self.session = session

        self.form_layout = QFormLayout(self)

        self.course_name = QTextEdit()
        self.form_layout.addRow("Name (name + subdivision + internship", self.course_name)

        self.list_of_courses = QComboBox()
        self.list_of_courses.addItems([course_kind for course_kind in session.possible_courses_kinds])
        self.form_layout.addRow("Course", self.list_of_courses)

        self.list_of_events = QComboBox()
        self.list_of_events.addItems([event_name for event_name in session.possible_events])
        self.form_layout.addRow("Event type", self.list_of_events)
        self.list_of_events.currentIndexChanged.connect(self.new_current_event)
        self.waiting_position = None

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.prepare_add_course)
        self.form_layout.addRow("", self.save_button)


    def new_current_event(self):
        source = self.sender()
        if source.currentText() == "Waiting":
            self.waiting_position = QSpinBox()
            self.waiting_position.setRange(0, 1000000)
            self.form_layout.insertRow(3, "Position", self.waiting_position)
        else:
            if self.waiting_position:
                self.form_layout.removeRow(self.waiting_position)
                self.waiting_position = None

    def prepare_add_course(self):
        course_name = self.list_of_courses.currentText()
        event_name = self.list_of_events.currentText()
        date = self.calendar.dateTime()

        course = self.session.courses[course_name]

        event_kind = all_event_kinds[event_name]
        if event_kind == WaitingListEvent:
            place = self.waiting_position.value()
            event = WaitingListEvent(date, course, place)
        else:
            event = event_kind(date, course)
        self.session.add_event(course, event)


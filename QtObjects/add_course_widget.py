from PySide6.QtWidgets import *
from PySide6.QtCore import *
from dataclasses import *
from constants import *
from QtObjects.customstylewidget import *

class AddCourse(QWidget):
    def __init__(self, session, parent):
        super(AddCourse, self).__init__(parent)

        self.session = session

        self.form_layout = QFormLayout(self)

        self.course_name = QTextEdit()
        self.course_name.setMaximumHeight(40)
        self.form_layout.addRow("Name (name + subdivision + internship)", self.course_name)

        self.list_of_courses = QComboBox()
        self.list_of_courses.addItems([course_kind for course_kind in session.possible_courses_kinds])
        self.form_layout.addRow("Course type", self.list_of_courses)

        self.internship = QCheckBox()
        self.form_layout.addRow("Internship", self.internship)

        self.places_available = QSpinBox()
        self.places_available.setRange(0,1000000)
        self.form_layout.addRow("Places available", self.places_available)

        self.previous_last_entry = QSpinBox()
        self.previous_last_entry.setRange(0,100000)
        self.form_layout.addRow("Last year last entry", self.previous_last_entry)

        self.save_button = CustomQPushBox("Save", width=300)
        self.save_button.clicked.connect(self.prepare_add_course)
        self.form_layout.addRow("", self.save_button)




    def prepare_add_course(self):
        name = self.course_name.toPlainText()
        kind = self.list_of_courses.currentText()
        internship = self.internship.isChecked()
        selectivity = Selectivity(self.places_available.value(), self.previous_last_entry.value())
        course = Course(name, kind, internship, selectivity)
        self.session.add_course(course)

        self.parent().reload()
from PySide6.QtWidgets import *


class AddEvent(QWidget):
    def __init__(self, session, parent):
        super(AddEvent, self).__init__(parent)

        vertical_layout = QVBoxLayout(parent=self)

        calendar = QCalendarWidget(parent=self)
        vertical_layout.addWidget(calendar)
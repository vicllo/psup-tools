import random

from dataclasses import *
from QtObjects import *
from pathlib import Path
from datetime import datetime

from PySide6 import QtWidgets

import sys


if __name__ == '__main__':

    event_file_name = "event_database.csv"
    courses_file_name = "courses_database.csv"

    if not Path(event_file_name).is_file():
        with open(event_file_name,"x") as new_event_file:
            pass

    if not Path(courses_file_name).is_file():
        with open(courses_file_name,"x") as new_course_file:
            pass

    session = Session(courses_file_name, event_file_name)

    session.read()

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("fusion"))

    main_window = MainWindow(session, 300, 100, 640, 480)
    main_window.show()

    exit_code = app.exec()
    session.write()

    sys.exit()


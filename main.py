import random

from dataclasses import *
from QtObjects import *

from datetime import datetime

from PySide6 import QtWidgets

import sys


if __name__ == '__main__':
    print("Hello World")

    file_name = "database.csv"
    session = Session(file_name)

    session.read()

    date = datetime(2021, 5, 28, 19, 20, 00)
    selectivity = Selectivity(370, 500)
    course = Course("St Louis", Prepa(), False, selectivity)
    event = WaitingListEvent(date, course, random.randint(1,100))

    session.add_event(course, event)

    event = SchoolRefuseEvent(date, course)

    session.add_event(course, event)

    session.write()

    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow(session, 300, 100, 640, 480)
    main_window.show()

    sys.exit(app.exec())


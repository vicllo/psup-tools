import random

from dataclasses import *
from QtObjects import *
from pathlib import Path
from datetime import datetime
from PySide6.QtGui import *

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

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    app.setWindowIcon(QIcon("icon.ico"))

    main_window = MainWindow(session, 0, 0, 1920, 1000)
    main_window.show()

    exit_code = app.exec()
    session.write()

    sys.exit()


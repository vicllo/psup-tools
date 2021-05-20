import random

from dataclasses import *
from QtObjects import *

from datetime import datetime

from PySide6 import QtWidgets

import sys


if __name__ == '__main__':

    file_name = "database.csv"
    session = Session(file_name)

    session.read()

    session.write()

    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow(session, 300, 100, 640, 480)
    main_window.show()

    sys.exit(app.exec())


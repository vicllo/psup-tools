import DB_manager
from dataclasses import *

from datetime import datetime

if __name__ == '__main__':
    print("Hello World")

    file_name = "database.csv"

    date = datetime(2021, 5, 27, 19, 20, 00)
    selectivity = Selectivity(370, 500)
    course = Course("St Louis", Prepa(), False, selectivity)
    event = WaitingListEvent(date, course, 78)

    DB_manager.add_event(file_name, event)
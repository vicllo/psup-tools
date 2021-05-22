from PySide6.QtCore import Qt

class Event:
    def __init__(self, date, course):
        """
        The standard event class
        :param date: QDateTime
        :param course: Course
        """
        self.date = date
        self.course = course

    def __str__(self):
        return ",".join([self.date.toString(Qt.DateFormat.ISODate), str(self.course.name)])


class AcceptEvent(Event):
    def __init__(self, date, course):
        super(AcceptEvent, self).__init__(date, course)
        self.kind = "Accepted"

    def __str__(self):
        return super().__str__()+",Accepted,-1"


class UserRefuseEvent(Event):
    def __init__(self, date, course):
        super(UserRefuseEvent, self).__init__(date, course)
        self.kind = "UserRefused"

    def __str__(self):
        return super().__str__()+",UserRefused,-1"


class SchoolRefuseEvent(Event):
    def __init__(self, date, course):
        super(SchoolRefuseEvent, self).__init__(date, course)
        self.kind = "SchoolRefused"
    def __str__(self):
        return super().__str__()+",SchoolRefused,-1"


class WaitingListEvent(Event):
    def __init__(self, date, course, place):
        super(WaitingListEvent, self).__init__(date, course)
        self.place = place
        self.kind = "Waiting"

    def __str__(self):
        return super().__str__()+","+",".join(["Waiting", str(self.place)])


class PropositionEvent(Event):
    def __init__(self, date, course):
        super(PropositionEvent, self).__init__(date, course)
        self.kind = "Proposition"

    def __str__(self):
        return super().__str__()+",Proposition,-1"

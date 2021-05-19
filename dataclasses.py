

class Event:
    def __init__(self, date, course):
        """
        The standard event class
        :param date: datetime
        :param course: Course
        """
        self.date = date
        self.course = course


class AcceptEvent(Event):
    def __init__(self, date, course):
        super(AcceptEvent, self).__init__(date, course)


class UserRefuseEvent(Event):
    def __init__(self, date, course):
        super(UserRefuseEvent, self).__init__(date, course)


class ServerRefuseEvent(Event):
    def __init__(self, date, course):
        super(ServerRefuseEvent, self).__init__(date, course)


class WaitingListEvent(Event):
    def __init__(self, date, course, place):
        super(WaitingListEvent, self).__init__(date, course)
        self.place = place


class PropositionEvent(Event):
    def __init__(self, date, course):
        super(PropositionEvent, self).__init__(date, course)


class Selectivity:
    def __init__(self, places_available, previous_last_entry):
        self.places_available = places_available
        self.previous_last_entry = previous_last_entry


class Course:
    def __init__(self, name, kind, internship, selectivity):
        self.name = name
        self.kind = kind
        self.internship = internship
        self.selectivity = selectivity


class CourseKind:
    def __init__(self, is_selective):
        self.is_selective = is_selective


class Prepa(CourseKind):
    def __init__(self):
        super(Prepa, self).__init__(True)


class Licence(CourseKind):
    def __init__(self, is_selective):
        super(Licence, self).__init__(is_selective)


class SimpleLicence(Licence):
    def __init__(self):
        super(SimpleLicence, self).__init__(False)


class DoubleLicence(Licence):
    def __init__(self):
        super(DoubleLicence, self).__init__(True)
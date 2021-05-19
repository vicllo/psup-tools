

class Event:
    def __init__(self, date, course):
        """
        The standard event class
        :param date: datetime
        :param course: Course
        """
        self.date = date
        self.course = course

    def __str__(self):
        return ",".join([str(self.date), str(self.course)])


class AcceptEvent(Event):
    def __init__(self, date, course):
        super(AcceptEvent, self).__init__(date, course)

    def __str__(self):
        return super().__str__()+"Accepted"


class UserRefuseEvent(Event):
    def __init__(self, date, course):
        super(UserRefuseEvent, self).__init__(date, course)

    def __str__(self):
        return super().__str__()+",UserRefused"


class ServerRefuseEvent(Event):
    def __init__(self, date, course):
        super(ServerRefuseEvent, self).__init__(date, course)

    def __str__(self):
        return super().__str__()+",ServerRefused"


class WaitingListEvent(Event):
    def __init__(self, date, course, place):
        super(WaitingListEvent, self).__init__(date, course)
        self.place = place

    def __str__(self):
        return super().__str__()+","+",".join(["Waiting", str(self.place)])


class PropositionEvent(Event):
    def __init__(self, date, course):
        super(PropositionEvent, self).__init__(date, course)

    def __str__(self):
        return super().__str__()+",Proposition"


class Selectivity:
    def __init__(self, places_available, previous_last_entry):
        self.places_available = places_available
        self.previous_last_entry = previous_last_entry

    def __str__(self):
        return "Available places : "+str(self.places_available)+",Last entry last year : "+str(self.previous_last_entry)


class Course:
    def __init__(self, name, kind, internship, selectivity):
        self.name = name
        self.kind = kind
        self.internship = internship
        self.selectivity = selectivity

    def __str__(self):
        return ",".join([self.name, str(self.kind), str(self.internship), str(self.selectivity)])


class CourseKind:
    def __init__(self, is_selective):
        self.is_selective = is_selective


class Prepa(CourseKind):
    def __init__(self):
        super(Prepa, self).__init__(True)

    def __str__(self):
        return "Prepa"


class Licence(CourseKind):
    def __init__(self, is_selective):
        super(Licence, self).__init__(is_selective)


class SimpleLicence(Licence):
    def __init__(self):
        super(SimpleLicence, self).__init__(False)


class DoubleLicence(Licence):
    def __init__(self):
        super(DoubleLicence, self).__init__(True)
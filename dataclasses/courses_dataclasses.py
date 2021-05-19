

class Course:
    def __init__(self, name, kind, internship, selectivity, events = []):
        self.name = name
        self.kind = kind
        self.internship = internship
        self.selectivity = selectivity
        self.events = []

    def __str__(self):
        return ",".join([self.name, str(self.kind), str(self.internship), str(self.selectivity)])

    def add_event(self, event):
        self.events.append(event)


class Selectivity:
    def __init__(self, places_available, previous_last_entry):
        self.places_available = places_available
        self.previous_last_entry = previous_last_entry

    def __str__(self):
        return str(self.places_available)+","+str(self.previous_last_entry)


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

    def __str__(self):
        return "Simple licence"


class DoubleLicence(Licence):
    def __init__(self):
        super(DoubleLicence, self).__init__(True)

    def __str__(self):
        return "Double licence"
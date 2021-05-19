

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

    def __str__(self):
        return "Simple licence"


class DoubleLicence(Licence):
    def __init__(self):
        super(DoubleLicence, self).__init__(True)

    def __str__(self):
        return "Double licence"
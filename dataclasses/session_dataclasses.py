from dataclasses import *
from constants import *
from PySide6.QtCore import QDateTime, Qt

class Session:
    def __init__(self, course_file_name, event_file_name, courses=None):
        if courses is None:
            courses = {}

        self.course_file_name = course_file_name
        self.event_file_name = event_file_name
        self.courses = courses
        self.course_lines_read = 0
        self.event_lines_read = 0
        self.possible_events = {"Accepted": AcceptEvent,
                                "UserRefused": UserRefuseEvent,
                                "SchoolRefused": SchoolRefuseEvent,
                                "Waiting": WaitingListEvent,
                                "Proposition": PropositionEvent}
        self.possible_courses_kinds = {"Prepa": Prepa,
                                       "Simple licence": SimpleLicence,
                                       "Double licence": DoubleLicence}

    def add_course(self, new_course):
        self.courses[new_course.name] = new_course

    def add_event(self, course, event):
        if course.name in self.courses:  # TODO : Check si le in renvoie la clé ou la valeur
            self.courses[course.name].add_event(event)
        else:
            self.add_course(course)
            self.courses[course.name].add_event(event)

    def read(self):
        with open(self.course_file_name, "r") as reading_file:
            read = reading_file.read()
        for raw_event in read.split("\n"):
            if raw_event:
                self.course_lines_read += 1
                selectivity = [None, None]
                name, kind, internship, selectivity[0], selectivity[1] = raw_event.split(",")
                course = Course(name, kind, internship, selectivity)
                if not name in self.courses.values():
                    self.add_course(course)

        with open(self.event_file_name, "r") as reading_file:
            read = reading_file.read()
        for raw_event in read.split("\n"):
            if raw_event:
                self.event_lines_read += 1
                date, name, event_type, place = raw_event.split(",")
                date = QDateTime.fromString(date, Qt.DateFormat.ISODate)

                if name in self.courses:
                    course = self.courses[name]
                else:
                    raise ValueError("Course not found")
                if event_type == "Waiting":
                    event = all_event_kinds[event_type](date, course, place)
                else:
                    event = all_event_kinds[event_type](date, course)
                self.add_event(course, event)

    def write(self):
        events = []
        for course in self.courses.values():
            for event in course.events:
                events.append([event.date, event])
        lines_to_write = [x[1] for x in sorted(events, key=lambda x:x[0])]
        if self.event_lines_read <= len(lines_to_write):
            with open(self.event_file_name, "w") as writing_file:
                for line_to_write in lines_to_write:
                    writing_file.write(str(line_to_write)+"\n")
        else:
            print(self.event_lines_read, len(lines_to_write))
            raise MemoryError("The writing output smaller then the input. Check the logfiles if it is still complete")
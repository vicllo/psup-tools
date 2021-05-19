from dataclasses import *
from constants import *


class Session:
    def __init__(self, file_name, courses=None):
        if courses is None:
            courses = {}
        self.file_name = file_name
        self.courses = courses

    def add_course(self, new_course):
        self.courses[new_course.name] = new_course

    def add_event(self, course, event):
        if course.name in self.courses:  # TODO : Check si le in renvoie la clé ou la valeur
            course.add_event(event)
        else:
            self.add_course(course)
            course.add_event(event)

    def read(self):
        with open(self.file_name, "r") as reading_file:
            read = reading_file.read()
        for raw_event in read.split("\n"):
            if raw_event:
                selectivity = [None, None]
                date, name, kind, internship, selectivity[0], selectivity[1], event_type = raw_event.split(",")[:7]
                selectivity = Selectivity(int(selectivity[0]), int(selectivity[1]))
                print(selectivity)
                course = Course(name, kind, internship, selectivity)
                if event_type == "Waiting":
                    place = raw_event.split(",")[-2]
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
        with open(self.file_name, "w") as writing_file:
            for line_to_write in lines_to_write:
                writing_file.write(str(line_to_write)+"\n")
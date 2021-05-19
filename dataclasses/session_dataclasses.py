class Session:
    def __init__(self, file_name, courses=None):
        if courses is None:
            courses = []
        self.file_name = file_name
        self.courses = courses

    def add_course(self, new_course):
        self.courses.append(new_course)

    def add_event(self, course, event):
        if course in self.courses:
            course.add_event(event)
        else:
            self.add_course(course)
            course.add_event(event)

    def write(self):
        events = []
        for course in self.courses:
            for event in course.events:
                events.append([event.date, event])
        lines_to_write = [x[1] for x in sorted(events, key =lambda x :x[0])]
        with open(self.file_name, "w") as writing_file:
            for line_to_write in lines_to_write:
                writing_file.write(str(line_to_write)+"\n")


def add_event(file_name, event):
    with open(file_name, "a") as event_file:
        event_file.write(str(event)+"\n")


def read(file_name, session):
    with open(file_name, "r") as event_file:
        event_lines = event_file.read()
        for event in event_lines:
            treat_event(event, session)


def treat_event(event, session):
    pass



def add_event(file_name, event):
    with open(file_name, "a") as event_file:
        event_file.write(str(event)+"\n")
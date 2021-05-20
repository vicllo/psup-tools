from dataclasses import *


def waiting_list_plot(course):
    dates = []
    positions = []
    for event in course.events:
        if type(event) == WaitingListEvent:
            dates.append(event.date)
            positions.append(event.place)

    if dates:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(dates, positions, color='tab:blue')

        ax.set_title("Waiting list")

        plt.show()
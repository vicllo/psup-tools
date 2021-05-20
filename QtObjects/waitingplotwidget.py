from PySide6.QtGui import QPainter
from PySide6.QtWidgets import *
from PySide6.QtCharts import *
from dataclasses import *


def waiting_plot(course, parent):

    series = QLineSeries()

    for event in course.events:
        if type(event) == WaitingListEvent:
            series.append(event.date.day, int(event.place))

    chart = QChart()
    chart.legend().hide()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setTitle("Waiting list plot of "+course.name)
    chart_view = QChartView(chart, parent)

    return chart_view
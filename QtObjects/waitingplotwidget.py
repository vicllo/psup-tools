from PySide6.QtGui import QPainter
from PySide6.QtWidgets import *
from PySide6.QtCharts import *
from dataclasses import *


def waiting_plot(courses, parent):
    series = []
    for course in courses:
        serie = QLineSeries()
        for event in course.events:
            if type(event) == WaitingListEvent:
                serie.append(event.date.date().day(), int(event.place))
        series.append(serie)

    chart = QChart()
    chart.legend().hide()
    for serie in series:
        chart.addSeries(serie)
    chart.createDefaultAxes()
    chart.setTitle("Waiting list plot of "+", ".join([course.name for course in courses]))
    chart_view = QChartView(chart, parent)

    return chart_view
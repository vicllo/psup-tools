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
                serie.append(event.date.toSecsSinceEpoch(), int(event.place))
            serie.setName(course.name)
        series.append(serie)

    x_axis = QDateTimeAxis()
    x_axis.setTickCount(10)
    x_axis.setFormat("dd MMM")
    x_axis.setTitleText("Date")
    x_axis.setRange(QDateTime(2021, 5, 20, 0, 0, 0), QDateTime(2021, 7, 1, 0, 0, 0))

    y_axis = QValueAxis()
    y_axis.setTickCount(10)
    y_axis.setLabelFormat("%i")
    y_axis.setTitleText("Waiting position")
    y_axis.setRange(0, 1000)

    chart = QChart()

    # STYLE
    chart.setTheme(QChart.ChartThemeDark)

    for serie in series:
        serie.attachAxis(x_axis)
        serie.attachAxis(y_axis)
        chart.addSeries(serie)


    chart.addAxis(x_axis, Qt.AlignBottom)
    chart.addAxis(y_axis, Qt.AlignLeft)


    chart.setTitle("Waiting list plot of "+", ".join([course.name for course in courses]))
    chart_view = QChartView(chart, parent)
    chart_view.setRenderHint(QPainter.Antialiasing)

    return chart_view
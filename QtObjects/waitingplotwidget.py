from PySide6.QtGui import QPainter
from PySide6.QtWidgets import *
from PySide6.QtCharts import *
from dataclasses import *



def waiting_plot(course):

    series = QLineSeries()

    for event in course.events:
        if type(event) == WaitingListEvent:
            series.append(event.date.day, int(event.place))

    chart = QChart()
    chart.legend().hide()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setTitle("Waiting list plot of "+course.name)
    chart_view = QChartView(chart)

    return chart_view


class WaitingPlot(QChartView):

    def __init__(self, width, height, course, parent=None):
        super(WaitingPlot, self).__init__(parent)

        self.width = width
        self.height = height
        self.parent = parent
        #self.setFixedSize(width, height)

        self.series = QLineSeries()
        self.series.append(0, 6)
        self.series.append(6, 4)
        self.series.append(3, 8)
        self.series.append(7, 4)
        self.series.append(10, 5)

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)

        self.chart.createDefaultAxes()
        self.chart.setTitle("Waiting plot")

        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

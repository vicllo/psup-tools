from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
from dataclasses import *


def waiting_plot(courses, parent):

    all_colors = ["#3bb9eb", "#f2622a", "#95c551", "#98ffd5", "#d3e7c1", "#ff98c2", "#bdb5d5", "#8d6c9f"]
    graphWidget = pg.PlotWidget(parent)

    #Add Background colour to dark
    graphWidget.setBackground('#474747')

    x_series = []
    y_series = []
    name_series = []
    for course in courses:
        x_serie = []
        y_serie = []
        for event in course.events:
            if type(event) == WaitingListEvent:
                x_serie.append(event.date.toSecsSinceEpoch())
                y_serie.append(int(event.place))
        name_series.append(course.name)
        x_series.append(x_serie)
        y_series.append(y_serie)

    # Add Title
    if len(courses) == 1:
        graphWidget.setTitle("Waiting list plot of "+", ".join([course.name for course in courses]), color="w", size="10pt")
    else:
        graphWidget.setTitle("Waiting list plots", color="w", size="10pt")
    # Add Axis Labels
    styles = {"color": "#fffff", "font-size": "20px"}
    graphWidget.setLabel("left", "Place", **styles)
    graphWidget.setAxisItems({'bottom' : pg.DateAxisItem('bottom')})
    #Add legend
    graphWidget.addLegend()
    #Add grid
    graphWidget.showGrid(x=True, y=True)
    #Set Range
    graphWidget.setXRange(QDateTime(2021,5,1,0,0,0).toSecsSinceEpoch(), QDateTime(2021,7,1,0,0,0).toSecsSinceEpoch())
    graphWidget.setYRange(0, 1000)

    for i in range(len(courses)):
        pen = pg.mkPen(color=all_colors[i%len(all_colors)])
        graphWidget.plot(x_series[i], y_series[i], name=name_series[i], pen=pen, symbol="o", symbolSize=10, symbolBrush=all_colors[i%len(all_colors)])

    return graphWidget


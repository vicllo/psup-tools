from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class CustomQPushBox(QPushButton):
    def __init__(self,
                 text="",
                 icon=None,
                 parent=None,
                 width=60,
                 bg_color="#777",
                 circle_color="#DDD",
                 active_color="#00BCff",
                 writing_color="ffffff"):

        super(CustomQPushBox, self).__init__(text, parent)

        #SET DEFAULT PARAMETERS
        self.setCursor(Qt.PointingHandCursor)

        #SET SIZE
        self.setMinimumWidth(width)
        self.setMinimumHeight(width*0.3)

        #COLORS
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color
        self._writing_color = writing_color


    def paintEvent(self, e):
        # SET PAINTER
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        # SET AS NO PEN
        old_pen = p.pen()
        p.setPen(Qt.NoPen)

        # DRAW RECTANGLE
        rect = QRect(0, 0, self.width(), self.height())

        # DRAW BG
        p.setBrush(QColor(self._bg_color))
        p.drawRoundedRect(0, 0, rect.width(), self.height(), 0*self.height()/3, 0*self.height()/3)

        #DRAW TEXT
        p.setPen(Qt.white)
        new_font = p.font()
        new_font.setPixelSize(self.height()//5)
        p.setFont(new_font)
        p.drawText(rect, Qt.AlignCenter, self.text())

        # END DRAW
        p.end()

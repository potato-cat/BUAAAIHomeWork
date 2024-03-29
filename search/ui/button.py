import math
import sys

from PyQt5.QtGui import QPainterPath, QPolygonF, QPen, QFont, QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt, QRectF, QSequentialAnimationGroup, QPropertyAnimation, QPointF

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50


class Button(QGraphicsObject):
    clicked = pyqtSignal()

    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)
        self.text = text
        self.color = QColor(255, 0, 128)
        self.font = QFont()
        self.font.setWeight(QFont.Bold)
        self.font.setPixelSize(BUTTON_HEIGHT / 2)

    def paint(self, painter, option, widget):
        painter.setBrush(Qt.yellow)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT,
                                10, 10)
        painter.setPen(self.color)

        painter.setFont(self.font)
        text_width = painter.fontMetrics().width(self.text)
        text_height = painter.fontMetrics().height()
        painter.drawText((BUTTON_WIDTH - text_width) / 2,
                         (BUTTON_HEIGHT + text_height) / 2 - BUTTON_HEIGHT / 10,
                         self.text)

    def boundingRect(self):
        return QRectF(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)

    def mousePressEvent(self, event):
        self.color = Qt.black
        self.update()

    def mouseReleaseEvent(self, event):
        self.color = QColor(255, 0, 128)
        self.clicked.emit()
        self.update()

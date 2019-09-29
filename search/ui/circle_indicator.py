import sys

from PyQt5.QtCore import pyqtSignal, Qt, QRectF
from PyQt5.QtGui import QColor, QPixmap, QFont, QFontMetrics
from PyQt5.QtWidgets import *


class CircleIndicator(QGraphicsObject):
    changed = pyqtSignal(int)

    def __init__(self, size, num, parent=None):
        super(CircleIndicator, self).__init__(parent)
        self.size = size
        self.num = num
        self.max = 15
        self.min = 1
        self.font = QFont()
        self.font.setWeight(QFont.Bold)
        self.font.setPixelSize(self.size / 3)
        self.color = QColor(255, 192, 203)
        self.bubble = QPixmap('../resources/气泡.png').scaled(size, size)

    def paint(self, painter, option, widget):
        painter.setPen(self.color)
        painter.setFont(self.font)
        fontMetrics = QFontMetrics(self.font)
        painter.drawPixmap(0, 0, self.bubble)
        painter.drawText((self.size - fontMetrics.
                          width(str(self.num))) / 2,
                         (self.size + fontMetrics.
                          height()) / 2 - self.size / 10, str(self.num))

    def boundingRect(self):
        return QRectF(0, 0, self.size, self.size)

    def wheelEvent(self, event):
        delta = event.delta()
        self.prepareGeometryChange()
        if delta > 0:
            self.num += 1
        elif delta < 0:
            self.num -= 1
        self.num = self.max if self.num > self.max else self.num
        self.num = self.min if self.num < self.min else self.num
        self.changed.emit(self.num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene(0, 0, 500, 500)
    scene.setBackgroundBrush(QColor(87, 250, 255))
    scene.addItem(CircleIndicator(100, 12))
    view.setScene(scene)
    view.show()
    app.exec_()

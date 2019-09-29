import math
import sys

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsObject, QApplication, QGraphicsView, QGraphicsScene

MONK_THINK_SIZE = 300


class MonkThink(QGraphicsObject):
    def __init__(self, size=300, parent=None):
        super(MonkThink, self).__init__(parent)
        self.pixmap = QPixmap('../resources/小和尚.png')
        self.monk1 = self.pixmap.copy(50, 70, 320, 300).scaled(size, size)
        self.monk2 = self.pixmap.copy(445, 60, 300, 310).scaled(size, size)
        self.monk3 = self.pixmap.copy(800, 70, 320, 300).scaled(size, size)
        self.monk4 = self.pixmap.copy(50, 460, 300, 290).scaled(size, size)
        self.monk5 = self.pixmap.copy(445, 460, 305, 290).scaled(size, size)
        self.monk6 = self.pixmap.copy(820, 460, 285, 290).scaled(size, size)
        self.monk7 = self.pixmap.copy(55, 820, 330, 280).scaled(size, size)
        self.monk8 = self.pixmap.copy(450, 810, 290, 290).scaled(size, size)
        self.monk9 = self.pixmap.copy(770, 810, 380, 300).scaled(size, size)
        self.monks = [self.monk1, self.monk2,
                      self.monk6, self.monk7, self.monk8]
        self.angle = math.pi / 2
        self.size = size

    def startThink(self):
        self.timer = self.startTimer(50)

    def stopThink(self):
        self.killTimer(self.timer)

    def paint(self, painter, option, widget):
        angle = self.angle
        step = 2 * math.pi / 5
        for i in range(5):
            painter.drawPixmap(self.size * (1 + math.cos(angle)),
                               self.size * (1 - math.sin(angle)),
                               self.monks[i])
            angle += step

    def boundingRect(self):
        return QRectF(0, 0, self.size * 2,
                      self.size * 2).adjusted(0, 0, self.size,
                                              self.size)

    def timerEvent(self, a0):
        self.angle += math.pi / 20
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene()
    monkThink = MonkThink(50)
    scene.addItem(monkThink)
    monkThink.startThink()
    view.setScene(scene)
    view.show()
    app.exec_()

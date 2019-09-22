import math
import sys

from PyQt5.QtGui import QPainterPath, QPolygonF, QPen
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRectF, QSequentialAnimationGroup, QPropertyAnimation, QPointF

SMALL_ARROW_WIDTH = 20


class SmallArrow(QGraphicsObject):
    def __init__(self, start, end, color=Qt.black, parent=None):
        super(SmallArrow, self).__init__(parent)
        self.start = start
        self.end = end
        self.color = color

    def paint(self, painter, option, widget):
        path = QPainterPath()
        l_arrow = self.end - self.start
        path.moveTo(self.start)
        path.lineTo(self.end)

        length = math.sqrt(l_arrow.x() ** 2 + l_arrow.y() ** 2)
        sita = math.atan2(l_arrow.y(), l_arrow.x())
        p1 = self.end - QPointF(SMALL_ARROW_WIDTH * math.cos(sita),
                                SMALL_ARROW_WIDTH * math.sin(sita))
        p2 = p1 - QPointF(-(SMALL_ARROW_WIDTH / 2) * math.sin(sita),
                          (SMALL_ARROW_WIDTH / 2) * math.cos(sita))
        p3 = p1 + QPointF(-SMALL_ARROW_WIDTH / 2 * math.sin(sita),
                          SMALL_ARROW_WIDTH / 2 * math.cos(sita))
        path.addPolygon(QPolygonF([p2, p3, self.end, p2]))
        # path = path.simplified()
        painter.setPen(QPen(self.color, 2))
        painter.setBrush(self.color)
        painter.drawPath(path)
        painter.setPen(Qt.red)
        painter.drawPoint(p1)

    def boundingRect(self):
        rect = QRectF()
        rect.setBottomLeft(self.start)
        rect.setTopRight(self.end)
        rect = rect.normalized().adjusted(0, SMALL_ARROW_WIDTH, SMALL_ARROW_WIDTH, 0)
        return rect


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene(0, 0, 500, 500)
    eightFig = SmallArrow(QPointF(200, 200), QPointF(10, 10), Qt.red)
    scene.addItem(eightFig)
    view.setScene(scene)
    view.show()
    app.exec_()

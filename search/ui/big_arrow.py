import math
import sys

from PyQt5.QtGui import QPainterPath, QPolygonF
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRectF, QSequentialAnimationGroup, QPropertyAnimation, QPointF

BIG_ARROW_WIDTH = 20.0


class BigArrow(QGraphicsObject):
    def __init__(self, start, end, parent=None):
        super(BigArrow, self).__init__(parent)
        self.start = start
        self.end = end

    def paint(self, painter, option, widget):
        path = QPainterPath()
        l_arrow = self.end - self.start
        length = math.sqrt(l_arrow.x() ** 2 + l_arrow.y() ** 2)
        sita = math.atan2(l_arrow.y(), l_arrow.x())
        p1 = self.start + QPointF(-(BIG_ARROW_WIDTH / 2) * math.sin(sita),
                                  (BIG_ARROW_WIDTH / 2) * math.cos(sita))
        p2 = self.start - QPointF(-(BIG_ARROW_WIDTH / 2) * math.sin(sita),
                                  (BIG_ARROW_WIDTH / 2) * math.cos(sita))
        p3 = p2 + QPointF((length - BIG_ARROW_WIDTH) * math.cos(sita),
                          (length - BIG_ARROW_WIDTH) * math.sin(sita))
        p4 = p3 - QPointF(-BIG_ARROW_WIDTH / 2 * math.sin(sita),
                          BIG_ARROW_WIDTH / 2 * math.cos(sita))
        p5 = self.end
        p7 = p1 + QPointF((length - BIG_ARROW_WIDTH) * math.cos(sita),
                          (length - BIG_ARROW_WIDTH) * math.sin(sita))
        p6 = p7 + QPointF(-BIG_ARROW_WIDTH / 2 * math.sin(sita),
                          BIG_ARROW_WIDTH / 2 * math.cos(sita))
        path.addPolygon(QPolygonF([p1, p2, p3, p4, p5, p6, p7, p1]))
        # path = path.simplified()
        painter.setPen(Qt.black)
        painter.setBrush(Qt.yellow)
        painter.drawPath(path)

    def boundingRect(self):
        rect = QRectF()
        rect.setBottomLeft(self.start)
        rect.setTopRight(self.end)
        rect = rect.normalized().adjusted(BIG_ARROW_WIDTH / 2,
                                          BIG_ARROW_WIDTH / 2,
                                          BIG_ARROW_WIDTH / 2,
                                          BIG_ARROW_WIDTH / 2)
        return rect


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene(0, 0, 500, 500)
    eightFig = BigArrow(QPointF(200, 200), QPointF(10, 10))
    scene.addItem(eightFig)
    view.setScene(scene)
    view.show()
    app.exec_()

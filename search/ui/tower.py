import sys

from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtWidgets import *

TOWER_HEIGHT = 300
TOWER_BASE_HEIGHT = 50
TOWER_BASE_WIDTH = 900


class Tower(QGraphicsObject):
    def __init__(self, parent=None):
        super(Tower, self).__init__(parent)

    def paint(self, painter, option, widget):
        painter.setBrush(QColor(237, 189, 101))
        painter.setPen(Qt.NoPen)
        painter.drawRect(0, TOWER_HEIGHT, TOWER_BASE_WIDTH,
                         TOWER_BASE_HEIGHT)
        painter.setPen(QPen(QColor(128, 0, 128), 3))
        painter.setBrush(Qt.NoBrush)
        painter.drawLine(TOWER_BASE_WIDTH / 6, 0, 150, TOWER_HEIGHT)
        painter.drawLine(TOWER_BASE_WIDTH / 2, 0, 450, TOWER_HEIGHT)
        painter.drawLine(TOWER_BASE_WIDTH * 5 / 6, 0, 750, TOWER_HEIGHT)

    def boundingRect(self):
        return QRectF(0, 0, TOWER_BASE_WIDTH,
                      TOWER_BASE_HEIGHT + TOWER_HEIGHT)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene()
    view.setScene(scene)
    scene.addItem(Tower())
    view.show()
    app.exec_()

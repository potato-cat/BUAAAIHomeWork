import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRectF, Qt

FIGURE_WIDTH = 50
FIGURE_HEIGHT = 50


class Figure(QGraphicsObject):
    def __init__(self, n, parent=None):
        super().__init__(parent)
        self.n = n

    def paint(self, painter, option, widget):
        painter.setBrush(Qt.yellow)
        painter.drawRoundedRect(0, 0, FIGURE_WIDTH,
                                FIGURE_HEIGHT, 10, 10)
        painter.setPen(Qt.black)
        t_h = painter.fontMetrics().height()
        t_w = painter.fontMetrics().width(str(self.n))
        painter.drawText((FIGURE_HEIGHT - t_w) / 2,
                         (FIGURE_HEIGHT + t_h) / 2,
                         str(self.n))

    def boundingRect(self):
        return QRectF(0, 0, FIGURE_WIDTH, FIGURE_HEIGHT)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene(0, 0, 500, 500)
    scene.addItem(Figure(8))
    view.setScene(scene)
    view.show()
    app.exec_()

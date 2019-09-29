from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
import sys
from search.ui.tower import Tower, TOWER_HEIGHT

DISK_HEIGHT = 20


class Disk(QGraphicsObject):
    def __init__(self, size=100, color=QColor(237, 109, 0),
                 parent=None):
        super(Disk, self).__init__(parent)
        self.setZValue(-1)
        self.size = size
        self.color = color

    def paint(self, painter, option, widget):
        painter.setBrush(self.color)
        painter.drawRoundedRect(-self.size / 2, -DISK_HEIGHT-1,
                                self.size, DISK_HEIGHT, 10, 10)

    def boundingRect(self):
        return QRectF(-self.size / 2, -DISK_HEIGHT-1,
                      self.size, DISK_HEIGHT)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene()
    view.setScene(scene)
    scene.addItem(Tower())
    disk = Disk(300)
    disk.setPos(150, TOWER_HEIGHT)
    scene.addItem(disk)
    view.show()
    app.exec_()
